
# Bangla Sentiment Analysis

This project performs sentiment analysis on Bangla text data. The sentiment of the text is classified into two categories: "Depressive" and "Non Depressive". The project uses transformer-based models for text classification, and the sentiment labels are predicted based on the text content.

## Project Overview

This project involves the following steps:
1. **Data Exploration**: The dataset is loaded, and exploratory data analysis (EDA) is performed to check for missing values and examine the distribution of sentiment labels.
2. **Data Preprocessing**: The text data is cleaned, tokenized, and prepared for training.
3. **Model Training**: A transformer-based model is fine-tuned to classify the sentiment of the Bangla text.
4. **Evaluation**: The trained model is evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Dataset

The dataset used in this project contains two columns:
- **Description**: The Bangla text to be analyzed.
- **Label**: The sentiment label, either "Depressive" or "Non Depressive".

### Example:

| Description | Label |
|-------------|-------|
| মানুষ আমাকে সবসময় স্বার্থের জন্য ব্যবহার করে, ভালোবাসার জন্যে নয়। | Depressive |
| ঠিক না থাকা ঠিক আছে। | Non Depressive |

## Features

- **Bangla Sentiment Analysis**: The project predicts whether the given text is "Depressive" or "Non Depressive".
- **Transformer Model**: The model is fine-tuned using the `transformers` library, specifically using pre-trained transformer models like BERT for sequence classification.
- **Data Processing**: Includes steps like text cleaning, tokenization, and model training using a custom dataset.

## Requirements

- Python 3.x
- `transformers` library
- `torch` library
- `datasets` library
- `pandas`, `matplotlib`, and other necessary libraries for data analysis and visualization

You can install the necessary dependencies by running:
```
pip install -r requirements.txt
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/bangla-sentiment-analysis.git
   cd bangla-sentiment-analysis
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook to start exploring the data, preprocessing, and training the model:
   ```
   jupyter notebook Sentiment.ipynb
   ```

## How to Use

1. Load the dataset, clean and preprocess the text.
2. Train the model using the `AutoTokenizer` and `AutoModelForSequenceClassification` from the `transformers` library.
3. Evaluate the model using the provided evaluation metrics.
4. Use the trained model to make predictions on new Bangla text data.


This README provides a clear overview of the project's purpose, setup instructions, and usage. Let me know if you need further modifications or additions!
