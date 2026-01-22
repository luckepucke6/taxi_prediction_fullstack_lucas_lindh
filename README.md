# Taxi Price Prediction (Taxipred lab)

This project implements a complete machine learning pipeline for predicting taxi trip prices. The workflow covers the full process from exploratory data analysis and model training to a production-like setup with a backend API and a frontend application.

The final system allows a user to input trip details and receive a price prediction through a Streamlit interface that communicates with FastAPI backend.

## Model evaluation

Three different regression models were evaluated using MAE and RMSE.

- Linear regression:
    - MAE = ~17.6
    - RMSE = ~24.8

- Random forest:
    - MAE: ~16.4
    - RMSE: 21.3

- KNN:
    - MAE: ~19.5
    - RMSE: ~32.9


### Label choice

The target variable for this project is 'Trip_Price', which represents the final taxi fare. The model predicts prices in USD. Conversion to SEK is handled at the application level.


### Feature choice
The following features were selected:

- Time_of_Day: string -> this affects both the traffic and the demand, which affects the price.
- Day_of_Week_ string -> this affects if its a weekday or a weekend, weekends usually are a bit more pricy.
- Passenger_Count (REMOVED)-> if theres more passagers, there will be a bigger car. A bigger car -> more pricy.
- Traffic_Conditions: string -> if theres for example more traffic, the ride will be longer. Longer rides -> more pricy.
- Trip_Distance_km: float -> The most obvious one. The longer the ride, the pricier it gets.

All selected features are:
- known before the trip begins.
- nable for a user to input.
- relevant for price estimation


## Target leakage

Some of the columns were excluded to avoid target leakage or because they are not available to know before the trip is over.

## Missing values

Missing values were analysed thru comparing columns. No systematic correlation were found. I decided to remove them because there were very few of them.

## Data types

After handling the NULLS I fixed the datatypes. Categorical columns where changed from objects to strings.



# MODEL DEVELOPMENT - Linear Regression

The goal of the model development was to get a baseline model for predicting the taxi prices and a establish a reference point for evaluating models later.

### Outlier analysis

Potential outliers in Trip_Price were investigated using different plots. Some trips showed pretty high prices, but the more I looked in to it I could see that those trips also were very long.

Since they were realistic I decided to keep them and not remove them from the dataset.

## Scikit-learn workflow

The model dev. followed a standard scikit-learn workflow:
1. Split data
The dataset were split into train|test sets.

2. Preprocessing
Categorical features were one-hot encoded and numerical features were passed through using a 'ColumnTransformer'. The preprocessing was fitted on the training data only and then applied to both train and test sets to prevent data leakage.

3. Model training
A linear regression model was trained using the preprocessed training data.

4. Prediction
The trained model was used to predict taxi prices on the test set.

5. Evaluation
Model performance was evaluated using MSE and RMSE.

BASELINE RESULT
The linear regression model achieved a MAE of ~17.6 and RMSE ~24.8, which I will be using as a baseline for comparing with other models.

# MODEL DEVELOPMENT - Random Forest

Random Forest was used to get a more flexible model to catch non-linear connection in the data. The model was trained on the same train|test split and same feature encoding as the linear regression to secure a fair comparison.

The result for random forest was a MAE of ~16.4 and a RMSE of ~21.3.

The random forest model have a better performance than the linear regression, which indicates that the model better can handle more complex connection between features and taxi price.

# MODEL DEVELOPMENT - KNN

In addition to linear regression and random forest, a KNN regressor was trained as a comparison model. Since KNN is a distance-based algorithm, feature scaling was applied before training. Several values of 'k' were evaluated using the same train|test split and evaluation metrics as the other models.

The result for KNN was a MAE of ~19.5 and a RMSE of ~32.9.

## Model comparison

All model were evaluated using MAE and RMSE with an identical feature set and preprocessing pipeline. KNN achieved similar performance to the linear regression baseline but did not outperform Random Forest, which showed lower error metrics and more robust performance.

## Final model selection and export

Random forest was selected as the final model due to its superior performance and ability to capture non-linear relationships in the data. The trained model and the fitted preprocessing pipeline were exported using 'joblib' and used directly in the backend application.


## Backend and API

The trained model and preprocessing pipeline are loaded into a FastAPI backend.

The backend exposes a '/predict' endpoint that:
- receives trip information as JSON
- validates input using Pydantic
- applies the same preprocessing used during training
- returns a predicted taxi price

The model predicts prices in USD. For presentation purpose, the backend also converts the price to SEK using a fixed exchange rate.


## Frontend

A Streamlit application serves as the frontend for the system. Users can input trip details and request a price prediction, which is retrieved by sending an HTTP request to the FastAPI backend.

The frontend focuses on clarity and ease.


## End-to-end flow

The complete application flow is as follows:

1. The user enters trip details in the Streamlit frontend.
2. The frontend sends a POST request to the FastAPI '/predict' endpoint.
3. The backend validates the input, applies preprocessing, and runs the trained model.
4. A price prediction is returned to the frontend and displayed to the user.


## Reflections

This project provided experience in building a complete machine learning pipeline, from data analysis and model training to deployment through an API and frontend.

An important learning was the need for consistency between training and inference, especially regarding preprocessing. Exporting both the model and preprocessing pipeline ensured reliable predictions in the backend.

## Challenges

One challenge was selecting features that were both predictive and realistically available before a trip begins, while avoiding target leakage.

Another challenge was structuring the project to maintain a clear separation between the machine learning logic, backend API and frontend application. This required careful planning and incremental testing.

## LLM usage

LLM were used as a support tool for conceptual guidance and debugging. 