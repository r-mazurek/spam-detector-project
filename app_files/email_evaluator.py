from joblib import load

model = load('app_files\\spam_detection_best_model.joblib')
vectorizer = load('app_files\\vectorizer.joblib')

def preprocess_text(subject, message):
    email_contents = subject + ' ' + message
    return vectorizer.transform([email_contents])


def predict_email(subject, message):
    email_contents = preprocess_text(subject, message)
    prediction = model.predict(email_contents)
    return "Spam" if prediction == 1 else "Ham"