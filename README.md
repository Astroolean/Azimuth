# Azimuth V1.2

![a2fc77103252e85d0a913d83fa730da4](https://github.com/user-attachments/assets/830f8bc9-d3fc-42df-955f-6e864232ca47)


**Azimuth** is a Python-based multitool designed for penetration testing and cybersecurity. It features a collection of tools for various security assessments, including user account management, registration, login, and logout functionalities. This README provides instructions on how to run the application, including the necessary requirements. This is still within its beginning stages and most tools are not available yet. This is something that was once a school project; turned into a side project over the years. This was created for educational purposes; at no point did I mention anywhere this is for malicious activity. Keep in mind I am not responsible for anything done with this program.

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

2. **Install ANY/ALL Requirenments**:
   - Install all the neccessary fucking bullshit or this will not work.

3. **Run the Application**:
   - Double-click the `Azimuth.exe` file to launch the application.

## Usage

**Azimuth** offers a range of penetration testing tools organized into 10 distinct tabs, each providing access to different functionalities. Additionally, there are user management buttons for account actions. Below are the details on how to use these features:

### User Account Management

1. **Registering an Account**:
   - Enter a desired username in the "Username" field.
   - Enter a password in the "Password" field.
   - Click the "Register" button to create an account.

2. **Logging into an Account**:
   - Enter your registered username in the "Username" field.
   - Enter your password in the "Password" field.
   - Click the "Login" button to access your account.

3. **Logging Out**:
   - Click the "Logout" button to log out from your account.

4. **Deleting an Account**:
   - Click the "Delete Account" button to permanently remove your account. You will be prompted to confirm this action.

### Toolkits Overview

Azimuth features 10 tabs, each dedicated to specific toolkits for various penetration testing tasks. Here’s a brief overview of what each tab includes:

1. **Tab 1: Information Gathering**
   - Tools for reconnaissance, such as WHOIS lookups and DNS enumeration.

2. **Tab 2: Vulnerability Scanning**
   - Utilities for scanning networks and applications for known vulnerabilities.

3. **Tab 3: Exploitation**
   - Tools for testing and exploiting vulnerabilities in systems.

4. **Tab 4: Post-Exploitation**
   - Techniques and scripts for maintaining access and data extraction after exploitation.

5. **Tab 5: Web Application Testing**
   - Tools specifically designed for testing the security of web applications.

6. **Tab 6: Wireless Network Testing**
   - Utilities for assessing the security of wireless networks.

7. **Tab 7: Social Engineering**
   - Tools for conducting social engineering attacks and awareness training.

8. **Tab 8: Password Cracking**
   - Utilities for cracking passwords using various algorithms and techniques.

9. **Tab 9: Reporting**
   - Tools for generating reports based on your findings during testing.

10. **Tab 10: Miscellaneous Tools**
   - A collection of additional tools that do not fit into the above categories.

### Navigation

- To navigate between toolkits, simply click on the desired tab at the top of the application interface.
- Each toolkit may contain additional buttons and features specific to that toolkit's purpose.

## Troubleshooting

- **Database Issues**: If the database file (`main.db`) is not created automatically, please ensure you have write permissions in the folder where the executable is located.
- **Login Failure**: If you encounter login failures, double-check that you are using the correct username and password. Ensure the account is registered before attempting to log in.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [astroolean@gmail.com](mailto:astroolean@gmail.com).

