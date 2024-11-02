import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import dump

# Load the dataset

print("Loading data...")

data = pd.read_csv('enron_spam_data.csv')

nltk.data.path.append('nltk_data')

data = data.drop(columns=['Message ID', 'Date'])
data = data.dropna()

print("Data loaded successfully.")

def preprocess_text(text):
    text = text.lower().strip()
    
    tokens = word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    
    return ' '.join(tokens)

print("Preprocessing data...")

data['cleaned_subject'] = data['Subject'].apply(preprocess_text)
data['cleaned_message'] = data['Message'].apply(preprocess_text)

X = data['cleaned_subject'] + ' ' + data['cleaned_message']
y = data['Spam/Ham']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['cleaned_subject'] + ' ' + data['cleaned_message'])

le = LabelEncoder()
y_encoded = le.fit_transform(y)

print("Data preproccessed successfully")

print("Splitting data into train/test portions...")

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.1)

#X_train_dense = X_train.toarray() if hasattr(X_train, 'toarray') else X_train
#X_test_dense = X_test.toarray() if hasattr(X_test, 'toarray') else X_test

print("Data splitted successfully")

model = MultinomialNB()

print("Training the model... ")

model.fit(X_train, y_train)

print("Model trained successfully.")

# ∨∨ ONLY RUN IF YOU WANT TO FIND THE BEST SETTINGS, TAKES OVER 40 MINS ∨∨

# param_distributions = {
#     'alpha': np.linspace(0.1, 2.0, 10)  # Adjust for a balance between performance and speed
# }

# random_search = RandomizedSearchCV(estimator=model, param_distributions=param_distributions, 
#                                    n_iter=10, scoring='accuracy', cv=3, verbose=1, random_state=42)

# random_search.fit(X_train_dense, y_train)  # Make sure to fit the model with your training data

# print("Best Parameters:", random_search.best_params_)
# print("Best Cross-validation Score:", random_search.best_score_)

# ∧∧ ONLY RUN IF YOU WANT TO FIND THE BEST SETTINGS, TAKES OVER 40 MINS ∧∧

print("Testing the model's accurracy...")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Testing finished successfully, heres the report: \n")

print(f"Accuracy: {accuracy}%")
# print(classification_report(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))

# best_model = random_search.best_estimator_
# test_accuracy = best_model.score(X_test_dense, y_test)
# print("Test Accuracy with Best Parameters:", test_accuracy)


## TEST THE MODEL YOURSELF!

print("Performing custom test...")

def predict_email(subject, message):
    cleaned_subject = preprocess_text(subject)
    cleaned_message = preprocess_text(message)
    custom_email = cleaned_subject + ' ' + cleaned_message
    custom_email_vectorized = vectorizer.transform([custom_email]).toarray()
    prediction = model.predict(custom_email_vectorized)
    return le.inverse_transform(prediction)[0]

result = predict_email("Coffee invitation", "Hello you fine specimen, mind going for a coffee with me?")

print("Custom test finished successfully. Here's the result: ")

print(f"The email is predicted to be: {result}")

# SAVE THE BEST MODEL AND USE LATER

# dump(best_model, 'spam_detection_best_model.joblib')
# dump(vectorizer, 'vectorizer.joblib')
