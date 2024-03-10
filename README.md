# Phishing Detector Extension 🛡️🕵️

## Introduction
Welcome to the Phishing Detector Extension repository! This powerful tool utilizes OpenAI's large language models (LLMs) to assess websites and predict whether they are phishing sites. Providing simple "Yes" or "No" responses, it integrates seamlessly as a browser extension to enhance your web security.

## Table of Contents
- [Introduction](#introduction)
- [Structure](#structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Structure
The project consists of two main folders:
- `frontend`: Contains the Chrome extension's UI code.
- `backend`: Holds the server code that interfaces with the OpenAI API.

## Prerequisites
Ensure you have the following before setting up the Phishing Detector Extension:
- Python 3.6 or higher
- Latest version of Node.js (for the frontend)
- OpenAI API key

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/atulX7/Phishing-Detector.git
   cd Phishing-Detector
   npm run build
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip3 install -r requirements.txt
   OPENAI_API_KEY=your_api_key_here

2. **Load the built extension into Chrome using Developer mode & Start the backend server:
   ```bash
   uvicorn main:app --reload

## Contributing
We welcome contributions to the Phishing Detector! 🌟 Here's how you can contribute:
1. Fork the repository to your account.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure all tests pass.
4. Submit a pull request detailing your changes.
5. After review, your contributions may be merged into the main codebase.

## License
This project is licensed under the [MIT License](License).
