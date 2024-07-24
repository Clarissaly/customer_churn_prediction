# Portfolio 1: E2E ML Pipeline

This repository showcases an End-to-End ML Pipeline. This project aims to build a customer churn prediction model for a Telecommunications company in the United States, TrustTelecom to identify customers who are likely to “churn”. (i.e. switch to another service provider in the next month) 
This helps the customer care team reach out promptly to understand user frustrations and extend the necessary discounts, offers and refunds in a bid to retain these customers in the long run.

EDA, Feature Engineering was conducted to optimise the performance of the ML model. 

The chosen final model is CatBoost with the following parameters:
{'random_strength': 0.5, 'learning_rate': 0.03, 'l2_leaf_reg': 3, 'iterations': 400, 'depth': 6, 'colsample_bylevel': 0.7, 'border_count': 128, 'bagging_temperature': 2}
The CatBoost model has a final AUC score of 0.911, taking into account only the top 10 features, training the model on the full dataset using cross-validation.

To see the final product:
Website URL of deployed web application: http://ec2-3-27-115-174.ap-southeast-2.compute.amazonaws.com 
