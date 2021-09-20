import smtplib


def send_mail(message, from_email, from_password, to_email):

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=from_email, password=from_password)

        connection.sendmail(
            from_addr=username,
            to_addrs=to_email,
            msg="Subject: Happy Birthday"
                f"\n\n{message}."
        )
        print("\tEmail Sent!")


if __name__ == "__main__":
    from configparser import ConfigParser

    parser = ConfigParser()

    parser.read("secrets.ini", encoding="utf-8")
    username = parser.get("email", "username")
    password = parser.get("email", "password")

    send_mail(message="Hello there.", from_email=username, from_password=password, to_email=username)
