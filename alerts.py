import smtplib

def send_email_alert(subject, message, recipient_email):
    """ Sends an email alert for trade signals """
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")
