# Azimuth V1.2

**Azimuth** is a Python-based multitool designed for penetration testing and cybersecurity. It features a collection of tools for various security assessments, including user account management, registration, login, and logout functionalities. This README provides instructions on how to run the application, including the necessary requirements. This is still within its beginning stages and most tools are not available yet. This is something that was once a school project; turned into a side project over the years.

## Requirements

Before running the executable, ensure you have the following:

- **Operating System**: Windows (The application is built to run on Windows OS).
- **Python**: The application was developed using Python 3.x. Make sure you have Python installed for development purposes, although it's not required to run the executable.
- **SQLite**: The application uses SQLite for the database. No additional installation is required as SQLite is included in the Python standard library.
- **Tkinter**: The GUI framework used is Tkinter, which comes bundled with Python installations.
- **Additional Libraries**: The following libraries are used in the application and should be included in your environment:
  - `hashlib`: For secure password hashing.
  - `itertools`: For efficient looping and cycling through values.
  - `customtkinter`: For a modernized Tkinter interface.
  - `PIL` (Pillow): For image handling and display.
  - `time`: For managing time-related functions.
  - `warnings`: For issuing warnings during runtime.
  - `math`: For mathematical operations (e.g., cosine).
  - `random`: For generating random values.
  - `os`: For operating system-related tasks.

## How to Run the Executable

1. **Download the Executable**:
   - Go to the [Releases](https://github.com/Astroolean/Azimuth/releases) section of this repository
   - Download the `Azimuth.exe` file.

2. **Extract the Files**:
   - If the executable is packaged in a ZIP file, extract it to your desired location on your computer.

3. **Run the Application**:
   - Double-click the `Azimuth.exe` file to launch the application.

## Usage

### Registering an Account

1. Enter a desired username in the "Username" field.
2. Enter a password in the "Password" field.
3. Click the "Register" button to create an account.

### Logging into an Account

1. Enter your registered username in the "Username" field.
2. Enter your password in the "Password" field.
3. Click the "Login" button to access your account.

### Logging Out

- Click the "Logout" button to log out from your account.

## Troubleshooting

- **Database Issues**: If the database file (`main.db`) is not created automatically, please ensure you have write permissions in the folder where the executable is located.
- **Login Failure**: If you encounter login failures, double-check that you are using the correct username and password. Ensure the account is registered before attempting to log in.

## Contributing

If you'd like to contribute to the development of Azimuth, feel free to fork the repository and submit a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [astroolean@gmail.com](mailto:astroolean@gmail.com).

