# **Predictive-Food-Price-Modeling**
### **Authors**
- Cynthia Nasimiyu 
- Julius Charles 
- Wambui Thuku 
- John Karanja 
- Ismail Ibrahim 
- Mariacharlote Mbiyu

## **Business Understanding**
**Overview:** This repository features a food price prediction model capable of forecasting future food prices, particularly for two key commodities, maize and beans. The model provides predictions for various time horizons, ranging from short-term (e.g., next week, next month) to medium-term (e.g., next quarter, next year)<br>
**Objective**
The food security and agricultural sector's crucial role in Kenya's well-being and economy underscores the need for accurate food price forecasting. With staple crops like maize and beans forming the backbone of the nation's agriculture, this project focuses on assisting Kenyan farmers and retailers in making informed decisions by utilizing advanced data science methodologies. The objectives encompass identifying price trends, regional segmentation, analysis of various food categories, geospatial insights, correlation investigations, time series modeling, market basket analysis, and the deployment of pricing models, ultimately benefitting Kenyan farmers and retailers striving to improve their economic prospects through data-driven insights.

## **Data Understanding**
The main dataset sourced from the World Food Programme Price Database comprises food price information for Kenya spanning from January 15, 2006, to February 15, 2024. The dataset contains 14 columns, 18,578 rows, and a comprehensive range of food categories, commodities, and region-specific data and it occupies approximately 2.0+ megabytes of memory.

External datasets, including inflation rates from the Central Bank of Kenya and weather patterns from dataviz.vam.wfp.org, were integrated into the primary dataset to enhance predictive accuracy.

## **Data Preparation**
Data Preparation involved several crucial steps. These steps collectively helped prepare the data for analysis and modeling, ensuring it is clean, informative, and structured for accurate and meaningful insights or predictions.
_Data Cleaning_: This step included handling missing values, removing duplicates, and addressing any inconsistencies in the dataset. 

_EDA (Exploratory Data Analysis)_: Here we explored the data to gain a better understanding of its characteristics. Univariate analysis focused on individual variables, examining their distributions and characteristics. Bivariate analysis explored relationships between pairs of variables, identifying correlations or patterns. Multivariate analysis delved into interactions between multiple variables to uncover complex relationships within the data.

_Feature Engineering_: Feature engineering involved creating new features and transforming existing ones to improve the performance of machine learning models. This step included creating seasons from weather patterns, factor analysis, and selection of commodities to proceed with.

_Data Preprocessing_: This step involved standardization, normalization, splitting the data into training and testing sets, changing the date to datetime, and encoding categorical variables. It ensured that the data was in a format suitable for time series modeling.

## **Modeling**
In the modeling phase, two distinct modeling techniques were employed for the prediction task:

**Time Series (SARIMA):** 
In the baseline SARIMA model, the Augmented Dickey-Fuller (ADF) test was initially used to assess stationarity, followed by differencing to achieve stationarity. The time series was further decomposed into trend, seasonal, and residual components. Autocorrelation and partial autocorrelation plots were employed to determine the appropriate order of a Seasonal Autoregressive Integrated Moving Average (SARIMA) model, which was then fitted to the stationary data

The second model used hyperparameter tuning using grid search to find the best hyperparameters to use to improve the model. The model's performance metrics indicate a Mean Absolute Error (MAE) of 9.30, a Mean Absolute Percentage Error (MAPE) of 15.77%, a Mean Squared Error (MSE) of 148.20, a Root Mean Squared Error (RMSE) of 12.17, and an R-squared (R2) value of 0.51, suggesting a moderate level of accuracy in capturing the variance in the data. The improved model was used to forecast the prices of maize and beans for the next 12 months and the results were as follows:
![image](https://github.com/CynthiaWanyonyi/Predictive-Food-Price-Modeling/assets/128204639/0b7214a8-b9b8-45ae-a5bf-9c9906cd1a23)
![image](https://github.com/CynthiaWanyonyi/Predictive-Food-Price-Modeling/assets/128204639/45da5d26-0a9c-4a8c-9a37-f3a5c5a9b06f)



**LSTM Model:** 
The baseline LSTM model used default parameters. Two key strategies were implemented to enhance the initial LSTM baseline model's performance. First, Early Stopping was introduced to mitigate overfitting by monitoring and halting training when performance on a validation dataset deteriorates. Second, Monte Carlo Dropout was incorporated, enabling the model to estimate prediction uncertainty by applying dropout during inference and generating multiple predictions with varying dropout states. 
![image](https://github.com/CynthiaWanyonyi/Predictive-Food-Price-Modeling/assets/128204639/0c83f141-0788-41dd-a0a1-032854c41b70)


However, the baseline model still outperformed the improved model therefore the baseline was used to make predictions for the next 12 months.

## **Conclusions & Recommendations**
**Conclusions:** Our study on predicting Kenyan food prices unveiled insights about price variability, inflation effects, and consumer preferences. We adopted LSTM models for maize and beans, reducing RMSE and enhancing forecasting accuracy. Our predictions empower stakeholders for better planning and decision-making in the agricultural sector.

**Recommendations:**

- Farmers and Retailers: Use forecasts for optimized production and sales strategies, and consider crop diversification.
- Government and Policymakers: Integrate price forecasts into food security policies and secure food commodities in anticipation of price hikes.
- Consumers: Stay informed about potential price fluctuations to manage your food budget effectively.

## **Determine next steps**
_Data Expansion:_ Acquire data from remote areas like North Eastern Kenya where price information is limited. Enhance the dataset's comprehensiveness.

_Model Diversification_: Extend predictive models to encompass a broader spectrum of essential food commodities in Kenya, offering more comprehensive insights.

_Collaborative Efforts_: Promote cooperation among agricultural sector stakeholders to share insights, best practices, and resources for bolstering food security.

_Advanced Analysis_: Incorporate additional variables like weather conditions and socio-economic factors to refine predictive models for improved accuracy and applicability. This will be valuable for data analysts and researchers.

