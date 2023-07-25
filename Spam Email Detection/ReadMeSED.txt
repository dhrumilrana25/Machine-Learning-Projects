To create a simple spam email detection system using machine learning, follow these steps:

Data Collection: Gather a labeled dataset containing spam and non-spam (ham) emails.

Data Preprocessing: Clean the emails by removing headers, HTML tags, and special characters. Convert the text to lowercase and tokenize the words.

Feature Extraction: Convert text data into numerical features. Use techniques like Bag-of-words or TF-IDF to represent emails as feature vectors.

Splitting the Dataset: Divide the preprocessed data into a training set (80%) and a testing set (20%).

Model Selection and Training: Choose a simple machine learning algorithm like Naive Bayes or Support Vector Machines. Train the model using the training set.

Model Evaluation: Evaluate the model's performance on the testing set using accuracy, precision, recall, and F1-score.

Hyperparameter Tuning: Fine-tune the model's hyperparameters to improve its performance.

Deployment: Integrate the trained model into an email client or server for automatic spam filtering.

Updating the Model: Periodically update the model with new data to adapt to emerging spam patterns.

By following these steps, you can create a basic spam email detection system using machine learning. Keep in mind that more sophisticated models and techniques can be applied for better performance, but this simple approach should give you a functional spam filter.