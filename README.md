# may24-team03

This repository belongs to Team 3. Team 3 is made up of Chen Lin Ying, Clarissa & Tay Min Hui Jolene. The chosen final model is CatBoost with the following parameters:
{'random_strength': 0.5, 'learning_rate': 0.03, 'l2_leaf_reg': 3, 'iterations': 400, 'depth': 6, 'colsample_bylevel': 0.7, 'border_count': 128, 'bagging_temperature': 2}
The CatBoost model has a final AUC score of 0.911, taking into account only the top 10 features, training the model on the full dataset using cross-validation.

Website URL of deployed Flask web application: http://ec2-3-27-115-174.ap-southeast-2.compute.amazonaws.com 

# TA Feedback
Amazing work on the capstone Clarissa & Jolene! Like the comprehensive work the team has done on the model training. Here are some pointers for improvement:
1. Use .env files to store sensitive credentials such as database connection details, especially when you publish your own public repository as there are malicious users who would misuse these credentials that you have published to the public and sometimes it might even cost you money. Just take note on that.
2. In software engineering, we would also do input validation. What this means is that if your form field only accepts an int type, your application should prevent users from submitting an input of type string or any other data types that may cause the application to fail
3. Do also clean up your code and delete unwanted comments in notebooks or unused code to make your code cleaner and more presentable so that it is easier to read and process, especially when collaborating in a larger team.

All in all, Excellent job on the capstone and congrats on completing AI300! Wishing you the very best in your future endeavours!
