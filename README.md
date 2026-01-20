Model evaluation
- Linear regression:
    - MAE = ~17.6
    - RMSE = ~24.8

- Random forest:
    - MAE: ~16.4
    - RMSE: 21.3

- KNN:
    - MAE: ~19.5
    - RMSE: ~32.9

# Taxipred labb

The label for this lab will be the column 'Trip_Price'.

The users for this app will be the taxi customers.

The amount of inputs for the user I will have will be around 5.

## EDA and Data Cleaning
The point of this EDA was to understand the datasets structure, identify a label and features, and also to see if there we're any NULLS etc.

With the EDA I analysed the columns, datatypes, if there we're any outliers and what to do with the NULLS.

### Label choice
This represents the actual taxi price and that is what the application will predict for the user. The taxi price is in USD. The model predicts prices in USD, while conversion to SEK is handled at the application level.

### Feature choice
I choose these features:
- Time_of_Day: string -> this affects both the traffic and the demand, which affects the price.
- Day_of_Week_ string -> this affects if its a weekday or a weekend, weekends usually are a bit more pricy.
- Passenger_Count (REMOVED)-> if theres more passagers, there will be a bigger car. A bigger car -> more pricy.
- Traffic_Conditions: string -> if theres for example more traffic, the ride will be longer. Longer rides -> more pricy.
- Trip_Distance_km: float -> The most obvious one. The longer the ride, the pricier it gets.

They are reasonable to know before the taxi ride begins.
They are possible for the user to put in.
And also do have a influence on the price.

## Target leakage
Some of the columns we're excluded to avoid target leakage or becuase they are not available to know before the trip is over.

## NULLS
Missing values we're analysed thru comparing columns. No systematic correlation were found. I decided to remove them becuase there were very few of them.

## Datatypes
After handling the NULLS I fixed the datatypes. Categorical columns where changed from objects to strings.


# MODEL DEVELOPMENT - Linear Regression
The goal of the model development was to get a baseline model for predicting the taxi prices and a establish a reference point for evaluating models later.

### Outlier analysis
Potential outliers in Trip_Price were investigated using different plots. Some trips showed pretty high prices, but the more I looked in to it I could see that those trips also were very long.

Since they were realistic I decided to keep them and not remove them from the dataset.

## Scikit-learn workflow
The model dev. followed a standard sci-kit learn workflow:
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
The linear regression model achieved a MAE of ~17.6 and RMSE ~24.8, which I will be using as a baseline for comparising with other models.

# MODEL DEVELOPMENT - Random Forest
Random Forest was used to get a more flexible model to catch non-linear connection in the data. The model was trained on the same train|test split and same feature encoding as the linear regression to secure a fair comparison.

The result for random forest was a MAE of ~16.4 and a RMSE of ~21.3.

The random forest model have a better performance than the linear regression, which indicates that the model better can handle more complex connection between features and taxi price.

# MODEL DEVELOPMENT - KNN
In addition to linear regression and random forest, a KNN regressor was trained as a comparison model. Since KNN is a distance-based algorithm, feature scaling was applied before training. Several values of 'k' were evaluated using the same train|test split and evaluation metrics as the other models.

The result for KNN was a MAE of ~19.5 and a RMSE of ~32.9.

## Model comparison
All model were evaluated using MAE and RMSE with an identical feature set and preprocessing pipeline. KNN achieved similair performance to the linear regression baseline but did not outperform Random Forest, which showed lower error metrics and more robust performance.

## Final model selection and export
Random forest was selected as the final model due to its superior performance and ability to capture non-linear relationships in the data. The trained mdoel and the fitted preprocessing pipeline were exportet using joblib.

## Backend and API
The trained model and preprocessing were saved using joblib and loaded into the fastapi backend.

The backend exposes a '/predict' endpoint that:
- recives trip information as JSON
- validates input using Pydantic
- applies the same preprocessing used during training
- returns a predicted taxi price

The model predicts prices in USD. For presentation purpose, the backend also converts the price to SEK using a fixed exchange rate.