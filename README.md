Overview

This exercise focuses on building and enhancing a secure web application using Python's Flask framework. The task involves adding a password update form, implementing advanced password validation based on NIST SP 800-63B guidelines, and incorporating user registration and login functionality. The goal is to ensure users can securely reset their passwords, meet strict security criteria, log failed login attempts, and improve user interaction with additional web features. The project emphasizes modern web security standards and enhanced protection for sensitive data.

Flask Template Integration

Objective: Use Flask templates to separate HTML content from Python code, making the application more modular and maintainable.
Functionality:
Create HTML pages outside of the Python code using Flask’s Jinja templates.
Render the templates from within the Python code to display content dynamically.
Include static assets such as images, tables, and forms.


User Registration and Login Functionality
Objective: Implement secure user registration and login functionality using Flask routes.

Key Features:

User Registration: Create a registration form where new users can create an account.
User Login: Implement a login form that allows registered users to authenticate.
Password Complexity Enforcement: Enforce the following password rules:
Minimum of 12 characters
At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character (e.g., @, #, !)
Additional Security:

Only the registration and login routes are accessible without authentication.
All other routes require a successful login to access.

Password Update Form
Objective: Create a password update form to allow users to reset their password.
The form will only be accessible after the user is logged in.
Password validation will ensure that the updated password meets the complexity criteria and is not part of a common password list.

Additional Flask Functionality
Objective: Enhance the web application by incorporating additional features such as images, tables, and forms.
These elements should be part of the Flask template structure, allowing for dynamic rendering based on user interactions.

Web Security Measures
Objective: Address security vulnerabilities within the web application.

Security Considerations:

Password Complexity: Ensure strong passwords by implementing the complexity rules defined above.

Logs: Implement logging to track user activities, particularly failed login attempts. The log should include:
Date and time of the event
IP address
Cryptographic Algorithms: Secure user credentials and other sensitive data using cryptographic techniques such as hashing and salting.
Web Application Vulnerabilities:

Prevent common vulnerabilities such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF) using best practices.

Common Password Validation
Objective: Ensure that passwords are checked against a list of commonly-used passwords (from CommonPasswords.txt).
If the password matches an entry in the list, the user will be prompted to choose a different one.

Conclusion
This project aims to build a secure and dynamic web application using Flask. The key focus areas include user authentication, password security, logging, and addressing web vulnerabilities. By integrating Flask templates, routes, and enforcing security standards, the web application will provide a robust platform for users while protecting sensitive information through best practices in cryptographic algorithms and password management.
