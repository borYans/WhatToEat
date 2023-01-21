import smtplib
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')
sent_from = config['MAIL_CREDENTIALS']['my_email']
login_pass = config['PASS_CREDENTIALS']['my_pass']
emails = config['EMAILS']['e_mails'].split(',')


def send_mail(subject, body):
    for mail_address in emails:
        print("Mail successfully sent.\n\n")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # this will make the connection secure
            connection.login(user=sent_from, password=login_pass)
            connection.sendmail(
                from_addr=sent_from,
                to_addrs=mail_address,
                msg=f"Subject: {subject}\n\n{body}"
            )
        time.sleep(1)
