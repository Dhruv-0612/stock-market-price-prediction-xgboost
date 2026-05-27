
````md
# 📈 Stock Market Prediction using XGBoost and Technical Indicators

> Machine learning-based stock market forecasting system using technical analysis indicators and XGBoost regression.

A research-oriented machine learning project developed to analyze historical stock market data and generate predictive insights using technical indicators and advanced regression techniques.

The system combines financial market analysis with feature engineering and machine learning to predict future stock price movements based on historical trends and technical patterns.

---

## ✨ Features

- 📊 Historical stock market data collection using Yahoo Finance API
- 🧠 Machine learning-based stock prediction pipeline
- 📈 Technical analysis indicator integration
- ⚡ XGBoost regression model
- 🔍 Feature engineering using historical market trends
- 📉 Prediction of:
  - Opening Price
  - Closing Price
  - High Price
  - Low Price
- 📏 Model evaluation using MAPE and MSE
- 🖥️ Flask-based web application integration
- 📚 Research-oriented implementation and analysis

---

## 🛠️ Tech Stack

Backend & Machine Learning:

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- TA (Technical Analysis) Library
- yFinance

Web Framework:

- Flask

---

```md
## 🧠 Project Overview

Stock market prediction is one of the most complex challenges in financial analytics due to the highly dynamic, volatile, and non-linear nature of market behavior. Traditional statistical forecasting methods often struggle to adapt to sudden price fluctuations, changing trends, and evolving market conditions.

This project presents a machine learning-based stock market prediction system developed to analyze historical financial data and generate predictive insights using technical analysis indicators and XGBoost regression.

The system combines:

- Historical stock market data
- Technical indicators
- Feature engineering techniques
- Machine learning-based predictive modeling

to identify hidden market patterns and forecast future stock price movements.

The implementation focuses on building a research-oriented predictive pipeline capable of preprocessing financial data, generating technical indicators, training regression models, and evaluating prediction performance using standard machine learning evaluation metrics.

The project demonstrates how machine learning techniques can be integrated with financial market analysis to support intelligent forecasting and data-driven decision making in stock market applications.
```

---

## 📂 Dataset Information

Historical stock market data is collected using the Yahoo Finance API through the `yfinance` Python library.

The dataset includes:

- Open prices
- Close prices
- High prices
- Low prices
- Trading volume

The data is preprocessed and transformed into machine learning-ready features for predictive modeling.

---

## ⚙️ Feature Engineering

Feature engineering plays a critical role in improving prediction performance.

The project generates several engineered features including:

- Previous closing prices
- Previous opening prices
- Previous high and low prices
- Previous trading volume
- Technical analysis indicators
- Moving averages

These features help the model capture historical patterns, momentum, and market volatility.

---

## 📊 Technical Indicators Used

### MACD (Moving Average Convergence Divergence)

Used for identifying market momentum and trend direction.

### RSI (Relative Strength Index)

Measures the speed and magnitude of stock price movements to identify overbought or oversold conditions.

### Bollinger Bands

Used to analyze market volatility and potential trend reversals.

### Moving Averages

Used to smooth historical price data and identify long-term trends.

---

## 🤖 Why XGBoost?

XGBoost was selected as the primary machine learning model due to its:

- Strong performance on tabular datasets
- Ability to capture non-linear relationships
- Robustness against overfitting
- Fast and scalable training
- High predictive performance
- Effective handling of engineered financial features

Compared to traditional regression and time-series models, XGBoost demonstrated better capability in handling complex financial market patterns and technical indicators.

---

## 🔀 Why Hybrid Approach?

This project follows a hybrid prediction approach by combining:

- Historical stock market data
- Technical analysis indicators
- Machine learning algorithms

This hybrid methodology improves prediction quality by leveraging both statistical market behavior and machine learning-based pattern recognition.

---

## ⚖️ Comparison with Other Models

| Model                | Limitation                                                             |
| -------------------- | ---------------------------------------------------------------------- |
| Linear Regression    | Unable to capture complex non-linear patterns                          |
| ARIMA / SARIMA       | Limited adaptability to sudden market volatility                       |
| LSTM                 | Requires larger sequential datasets and higher computational resources |
| Sentiment Analysis   | High noise and inconsistency in textual data                           |
| Fundamental Analysis | Difficulty in maintaining structured real-time financial data          |

After experimentation and analysis, XGBoost combined with technical indicators provided the most stable and effective results for this implementation.

---

## 🧩 Machine Learning Workflow

Historical Data Collection  
→ Data Preprocessing  
→ Feature Engineering  
→ Technical Indicator Generation  
→ Train-Test Split  
→ Data Scaling & Imputation  
→ XGBoost Model Training  
→ Prediction Generation  
→ Model Evaluation

---

## 📏 Evaluation Metrics

The project evaluates prediction performance using:

### Mean Absolute Percentage Error (MAPE)

Measures the average percentage difference between predicted and actual values.

### Mean Squared Error (MSE)

Measures the average squared prediction error.

These metrics help evaluate prediction reliability and model effectiveness.

---

## 📈 Results

The model demonstrated promising capability in identifying historical stock market patterns and generating predictive insights using technical indicators and machine learning techniques.

Prediction performance varied across different stocks and market conditions due to the inherently volatile nature of financial markets.

The project successfully demonstrated the effectiveness of machine learning approaches in stock market forecasting applications.

---

## ⚠️ Limitations

- Financial markets are highly volatile and unpredictable
- Prediction accuracy varies across different market conditions
- The model primarily relies on historical market behavior
- External geopolitical and economic factors are not directly incorporated
- Real-time trading environments may impact prediction consistency

---

## 📈 Future Improvements

Potential future enhancements include:

- Reinforcement learning-based prediction systems
- Real-time market prediction dashboard
- Automated trading strategies
- Integration of sentiment analysis
- Fundamental analysis integration
- Process automation
- Live market monitoring
- Deep learning models such as LSTM

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Dhruv-0612/stock-market-price-prediction-xgboost.git
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the prediction script:

```bash
python prediction.py
```

Enter the stock symbol when prompted.

Example:

```text
AAPL
```

The model will generate predicted:

- Opening Price
- Closing Price
- High Price
- Low Price

---

## 📁 Folder Structure

```text
stock-market-price-prediction-xgboost/
│
├── prediction.py
├── README.md
├── requirements.txt
└── thesis-report.pdf
```

---

## 📚 Thesis Report

The complete project thesis and implementation documentation are included in:

```text
thesis-report.pdf
```

The report contains:

- Research and analysis
- System architecture
- Technical implementation
- Feature engineering methodology
- Testing procedures
- Accuracy evaluation
- Future scope and innovation

---

## 👨‍💻 Contributors

- Dhruv Mistry
- Keval Mod
- Vishal Makwana

Bachelor of Engineering in Computer Engineering  
Sardar Vallabhbhai Patel Institute of Technology, Vasad  
Gujarat Technological University

---

## 📖 References

- Yahoo Finance
- Python Documentation
- Scikit-learn Documentation
- XGBoost Documentation
- TA Library Documentation
- Flask Documentation
- GitHub
- NeuralNine
````
