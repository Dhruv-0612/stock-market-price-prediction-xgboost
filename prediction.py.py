import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
import xgboost as xgb
import yfinance as yf
from flask import Flask, request, render_template
import datetime

# Function to download historical stock price data based on company symbol
def download_stock_data(symbol):
    data = yf.download(symbol, start='2021-01-01', end='2024-02-28')
    return data

# Function to prepare technical indicators and additional features
def prepare_features(data):
    macd = MACD(data['Close']).macd()
    rsi = RSIIndicator(data['Close']).rsi()
    bb_bands = BollingerBands(data['Close']).bollinger_mavg()

    data['Prev_Close'] = data['Close'].shift(1)
    data['Prev_High'] = data['High'].shift(1)
    data['Prev_Low'] = data['Low'].shift(1)
    data['Prev_Open'] = data['Open'].shift(1)
    data['Prev_Volume'] = data['Volume'].shift(1)
    data['MACD'] = macd.shift(1)
    data['RSI'] = rsi.shift(1)
    data['BB_Middle'] = bb_bands.shift(1)

    data = data.dropna()

    return data

# Function to make stock price predictions
def predict_stock_price(symbol):
    data = download_stock_data(symbol)
    data = prepare_features(data)

    features = data[['Close', 'High', 'Low', 'Open', 'Volume', 'Prev_Close', 'Prev_High', 'Prev_Low', 'Prev_Open', 'Prev_Volume', 'MACD', 'RSI', 'BB_Middle']]
    target = data[['Close', 'High', 'Low', 'Open']].shift(-1)

    features = features[:-1]
    target = target[:-1]

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.05, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    imputer = SimpleImputer(strategy='mean')
    X_train_scaled_imputed = imputer.fit_transform(X_train_scaled)
    X_test_scaled_imputed = imputer.transform(X_test_scaled)

    model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    model.fit(X_train_scaled_imputed, y_train)

    y_pred = model.predict(X_test_scaled_imputed)
    mape = mean_absolute_percentage_error(y_test, y_pred)

    last_day_data = features.iloc[[-1]].values
    last_day_data_scaled = scaler.transform(last_day_data)
    last_day_data_scaled_imputed = imputer.transform(last_day_data_scaled)

    predicted_values = model.predict(last_day_data_scaled_imputed)[0]

    predicted_close, predicted_high, predicted_low, predicted_open = predicted_values

    # Cleanly return the values so run.py can send them to the HTML page
    return {
        'mape': round(float(mape) * 100, 2), 
        'predicted_close': round(float(predicted_close), 2),
        'predicted_high': round(float(predicted_high), 2),
        'predicted_low': round(float(predicted_low), 2),
        'predicted_open': round(float(predicted_open), 2)
    }