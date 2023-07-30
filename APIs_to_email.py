import sys
import re
import urllib.request
import json
import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

API_CATS = "https://meowfacts.herokuapp.com/"
API_DOGS = "http://dog-api.kinduff.com//api/facts?number=1"

def main(argv):

    email_from_command, API_from_command = command_line_input(argv)
    receiving_adress = valid_email(email_from_command)
    topic = API_validation(API_from_command)

    if topic == "cats":
        message = cat_message(access_selected_API(API_CATS))
    elif topic == "dogs":
        message = dog_message(access_selected_API(API_DOGS))

    send_email(receiving_adress, message)


# check if correct number of command line arguments is passed, expected 3 total
def command_line_input(argv):
    if len(argv) < 3:
        sys.exit("Missing command line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command line arguments")
    else:
        return argv[1], argv[2]


# check if email provided in command line is valid, using regular expressions
def valid_email(email):
    email_format = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    if re.fullmatch(email_format, email):
        return email
    else:
        sys.exit("Provided email address is not valid")


# implement 2 APIs to be available from command line
# user can enter whole API url link to command line ar use variables API_cats or API_dogs
def API_validation(api_from_command):
    if (
        api_from_command.lower() == "cats"
        or api_from_command == API_CATS
    ):
        return "cats"
    elif (
        api_from_command.lower() == "dogs"
        or api_from_command == API_DOGS
    ):
        return "dogs"
    else:
        sys.exit("Provided API is unrecognized")


# call selected API and get response
# tried out python's in built library urllib.request
def access_selected_API(API):
    try:
        response = urllib.request.urlopen(API)
        if response.status == 200:
            response_data = response.read().decode()
            parsed_data = json.loads(response_data)
            return parsed_data
        else:
            sys.exit(f"API request failed with status code: {response.status}")
    except:
        sys.exit("Can't open provided API's URL address")


# format response from API into readable text,
# depending if API for cats' or dogs' facts is used
def cat_message(parsed_data):
    return parsed_data["data"][0]


def dog_message(parsed_data):
    return parsed_data["facts"][0]


# send message with readable text from API to email
def send_email(email_adress, message):
    email_sender = os.getenv("EMAIL_SENDER_ADDRESS")
    email_password = os.getenv("EMAIL_SENDER_PASSWORD")
    email_receiver = email_adress

    subject = "API to Email!"
    body = f"""
    {message}
    """
    email_obj = EmailMessage()
    email_obj["From"] = email_sender
    email_obj["To"] = email_receiver
    email_obj["Subject"] = subject
    email_obj.set_content(body)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, email_obj.as_string())
            print("Email is sent successfully!")
    except:
        print("Error occured while trying to send email")


if __name__ == "__main__":
    main(sys.argv)

