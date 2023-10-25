
# Python Keylogger with Email Functionality

This is a simple keylogger written in Python that records keystrokes and emails log files to a specified recipient's email address. The program can be used for educational purposes and understanding keylogging techniques. Please use it responsibly and with proper authorization.

## Usage

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/your-keylogger-repo.git
   ```

2. Navigate to the project directory:

   ```shell
   cd your-keylogger-repo
   ```

3. Run the keylogger script:

   ```shell
   python keylogger.py
   ```

4. Follow the on-screen prompts to input the log file directory, email credentials, and recipient's email address.

5. The keylogger will start recording keystrokes and send log files via email at the specified intervals.

## Configuration

You can configure the keylogger by modifying the following variables in the `keylogger.py` script:

- `log_dir`: The directory where log files will be stored.
- `log_interval`: The interval (in seconds) for creating new log files.
- `email_interval`: The interval (in log files) for sending log files via email.
- `email_address`: Your email address for sending log files.
- `email_password`: Your email password (Make sure to handle this securely).
- `recipient_email`: The recipient's email address.

## Disclaimer

This keylogger is intended for educational and research purposes only. Ensure that you have appropriate authorization before using it. Unauthorized use can have legal and ethical consequences.

## License

[MIT LICENSE](https://github.com/Ashhar-Azim/Email-Based-Keylogger-For-Python/blob/main/LICENSE)


## Acknowledgments

- [Pynput](https://pypi.org/project/pynput/): The library used for keyboard monitoring.
- [Python Email Library](https://docs.python.org/3/library/email.html): For sending emails.
