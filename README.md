# Project Title: API-to-Email

This project is a simple Python script that allows users to retrieve random facts about cats or dogs from two different APIs and send them via email. The script takes command line arguments for email address and the desired API to fetch the facts.

## Technical details:

The "API-to-Email" script fetches random facts about cats or dogs from the respective APIs and sends them to the specified email address. It demonstrates the use of the `urllib.request` library to access APIs, JSON parsing, sending emails using `smtplib` over SSL, and the utilization of environment variables stored in a `.env` file for sensitive information.

## How to Install and Run the Project:

Follow the steps below to install and run the "API-to-Email" project:

1. **Prerequisites:**
   - Python 3.x should be installed on your system.
   - Create a `.env` file in the same directory as the script.

2. **Clone the Repository:**
   ```
   git clone https://github.com/AkvileJank/facts_to_email.git
   ```

3. **Install Dependencies:**
   The script requires the `dotenv` library to read the environment variables from the `.env` file. You can install it using the following command:
   ```
   pip install python-dotenv
   ```

4. **Set Up Environment Variables:**
   In the `.env` file, add the following lines and replace the placeholders with your actual Gmail address and an app password:
   ```
   EMAIL_SENDER_ADDRESS = 'your_email@gmail.com'
   EMAIL_SENDER_PASSWORD = 'your_password'
   ```

   Make sure to enable "Less secure app access" in your Gmail settings and generate an app password for the sender's email.

5. **Run the Script:**
   To run the script, execute the following command in your terminal or command prompt:
   ```
   python script_name.py <email_address> <API_source>
   ```

   Replace `script_name.py` with the actual name of the Python script containing the provided code. `<email_address>` should be a valid Gmail address, and `<API_source>` can be one of the following:
   - `cats`: To fetch cat facts from the "https://meowfacts.herokuapp.com/" API.
   - `dogs`: To fetch dog facts from the "http://dog-api.kinduff.com//api/facts?number=1" API.

   Example:
   ```
   python script_name.py test@example.com cats
   ```

6. **Result:**
   The script will access the selected API, retrieve a random fact, and send it as an email to the specified address.

Feel free to use this script to fetch and share interesting cat or dog facts via email!
