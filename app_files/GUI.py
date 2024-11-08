from email_evaluator import predict_email
import tkinter as tk

def evaluate_email():
    subject = subject_entry.get()
    message = message_entry.get("1.0", "end-1c")

    if not subject or not message:
        message.showwarning("Input ERROR!")
        return
    
    result = predict_email(subject=subject, message=message)

    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title = ("Spam Detection Personal Project")
root.geometry("400x400")

tk.Label(root, text="Email Subject: ").pack(pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Email Message: ").pack(pady=5)
message_entry = tk.Text(root, width=50, height=10)
message_entry.pack()

evaluate_button = tk.Button(root, text="Evaluate", command=evaluate_email)
evaluate_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Halvetica, 14"))
result_label.pack(pady=10)

signature_label = tk.Label(root, text="Rafal Mazurek 2024")
signature_label.pack(side="bottom", pady=2)

root.focus_force()

root.mainloop()