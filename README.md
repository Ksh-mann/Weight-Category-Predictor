#Weight-Category Predictor
This project aims to predict weight categories of individuals based on their gender, height, and weight. The weight categories range from 'Extremely Weak' to 'Extremely Obese'. The predictor uses a Random Forest classifier to make these predictions.

#Motivation
The original dataset had limited data, which could potentially lead to poor model performance and overfitting. To address this limitation, data augmentation techniques were employed to increase the size of the dataset. Data augmentation involves creating variations of existing data by applying transformations while preserving the original meaning. This helps the model learn more robust and generalized patterns.

#Getting Started
Dataset: The dataset contains information about individuals, including their gender, height, weight, and weight category index. The index is mapped to human-readable weight categories. This data is crucial for training and evaluating the predictor.

#Data Augmentation: The original dataset was augmented to create additional samples. This involved applying minor variations to the 'Height' and 'Weight' attributes while maintaining the 'Gender' and 'Index' values. Data augmentation enhances the model's ability to handle different scenarios and improve its performance.

#Model Training: The predictor utilizes a Random Forest classifier to predict weight categories based on the augmented dataset. The model is trained on the augmented data, and hyperparameter tuning is performed to optimize its performance.

#Evaluation: The model's performance is evaluated using metrics such as accuracy, classification report, and confusion matrix on a test set. These metrics provide insights into the model's predictive capabilities.

#Live Predictor: The developed model includes a live predictor function that takes inputs (gender, height, weight) and predicts the corresponding weight category. This function showcases the model's real-world applicability.

#Code Overview
The code involves the following steps:

Data Loading and Preprocessing: The dataset is loaded, and the 'Index' values are mapped to weight category names. Gender is transformed into dummy variables for modeling.

Feature Scaling and Data Splitting: The features are scaled using StandardScaler, and the data is split into training and testing sets.

Hyperparameter Tuning: GridSearchCV is used for hyperparameter tuning to find the optimal number of estimators for the Random Forest classifier.

Model Training and Evaluation: The model is trained on the training set and evaluated using various metrics on the test set.

Live Predictor: A function is created to predict weight categories for live input. The function preprocesses the input and uses the trained model to make predictions.

#Usage
Clone the repository to your local machine.
Ensure you have the required libraries installed (numpy, pandas, sklearn).
Run the code file (weight_category_predictor.py) to train the model and see its performance.
Modify the your_details variable in the code to test the live predictor.

#Conclusion
The Weight-Category Predictor demonstrates how data augmentation can improve model performance and enhance its real-world usability. By predicting weight categories, the model could contribute to health and fitness assessments, personalized recommendations, and more.