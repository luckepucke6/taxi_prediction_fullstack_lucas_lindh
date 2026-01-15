# Taxipred labb

The label for this lab will be the column 'Trip_Price'.

The users for this app will be the taxi customers.

The amount of inputs for the user I will have will be around 5.

## EDA and Data Cleaning
The point of this EDA was to understand the datasets structure, identify a label and features, and also to see if there we're any NULLS etc.

With the EDA I analysed the columns, datatypes, if there we're any outliers and what to do with the NULLS.

### Label choice
This represents the actual taxi price and that is what the application will predict for the user.

### Feature choice
I choose these features:
- Time_of_Day -> this affects both the traffic and the demand, which affects the price.
- Day_of_Week -> this affects if its a weekday or a weekend, weekends usually are a bit more pricy.
- Passenger_Count -> if theres more passagers, there will be a bigger car. A bigger car -> more pricy.
- Traffic_Conditions -> if theres for example more traffic, the ride will be longer. Longer rides -> more pricy.
- Trip_Distance_km -> The most obvious one. The longer the ride, the pricier it gets.

They are reasonable to know before the taxi ride begins.
They are possible for the user to put in.
And also do have a influence on the price.

## Target leakage
Some of the columns we're excluded to avoid target leakage or becuase they are not available to know before the trip is over.

## NULLS
Missing values we're analysed thru comparing columns. No systematic correlation were found. I decided to remove them becuase there were very few of them.

## Datatypes
After handling the NULLS I fixed the datatypes. Categorical columns where changed from objects to strings.


# MODEL DEVELOPMENT (linear regression)
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
Model performance was evaluated using MSE.

BASELINE RESULT
The linear regression model achieved a MAE of ~17.7, which I will be using as a baseline for comparising with other models.