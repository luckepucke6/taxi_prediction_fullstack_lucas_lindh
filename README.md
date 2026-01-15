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
