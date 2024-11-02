from joblib import load

model = load('spam_detection_best_model.joblib')
vectorizer = load('vectorizer.joblib')

def preprocess_text(subject, message):
    email_contents = subject + ' ' + message
    return vectorizer.transform([email_contents])


def predict_email(subject, message):
    email_contents = preprocess_text(subject, message)
    prediction = model.predict(email_contents)
    return "Spam" if prediction == 1 else "Ham"