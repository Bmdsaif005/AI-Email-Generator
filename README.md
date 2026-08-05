# AI Email Generator

## Overview

AI Email Generator is a web application that generates professional emails based on user input using Amazon Bedrock and the Amazon Nova Lite foundation model. Users can specify the purpose of the email, recipient, tone, and key points, and the application generates a well-structured email in seconds.

The project was built to explore Generative AI application development using AWS services while learning prompt engineering, Amazon Bedrock, and Python.

---

## Features

* Generate professional emails using AI
* Choose different email tones (Formal, Friendly, Professional)
* Enter custom purpose, recipient, and key points
* AI-powered email generation using Amazon Bedrock
* Simple and responsive Streamlit interface
* Download generated emails as a text file
* Input validation and error handling

---

## Tech Stack

### Languages

* Python

### Framework

* Streamlit

### Cloud & AI

* Amazon Bedrock
* Amazon Nova Lite (`amazon.nova-lite-v1:0`)

### SDK

* boto3

### Version Control

* Git
* GitHub

---

## Project Structure

```text
AI-Email-Generator/
│
├── app.py               # Streamlit user interface
├── ai.py                # Amazon Bedrock integration
├── requirements.txt     # Project dependencies
├── README.md
└── .gitignore
```

---

## How It Works

1. The user enters:

   * Purpose
   * Recipient
   * Tone
   * Key Points

2. A prompt is dynamically generated based on the user's input.

3. The prompt is sent to Amazon Bedrock using the Amazon Nova Lite model.

4. The model generates a professional email.

5. The generated email is displayed in the application and can be downloaded as a text file.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Bmdsaif005/AI-Email-Generator.git
cd AI-Email-Generator
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## AWS Configuration

Configure your AWS credentials before running the application.

```bash
aws configure
```

Provide:

* AWS Access Key ID
* AWS Secret Access Key
* Default Region (recommended: `ap-south-1`)
* Output Format (`json`)

Ensure your AWS account has access to Amazon Bedrock and the Amazon Nova Lite model.

---

## Run the Application

```bash
streamlit run app.py
```

The application will be available in your browser at:

```
http://localhost:8501
```

---

## Screenshots

image1 - HOME
<img width="1468" height="952" alt="ai email generator 1" src="https://github.com/user-attachments/assets/4660a58c-569a-45ca-a1b1-448c15212061" />

image2 - GENERATED EMAIL
<img width="1463" height="947" alt="ai email generator 2" src="https://github.com/user-attachments/assets/ffbc7948-545b-4cc0-88e5-a0aff3967f0c" />



---

## Future Improvements

* Email templates for common use cases
* Temperature and maximum word controls
* Copy-to-clipboard functionality
* PDF download support
* Improved UI and layout
* Email history using session state
* Support for multiple AI models

---

## Learning Outcomes

This project helped me understand:

* Streamlit application development
* Prompt engineering
* Amazon Bedrock integration
* Amazon Nova Lite
* boto3 SDK
* AWS authentication and configuration
* Building AI-powered applications with Python

---

## Author

**Mohammed Saif**

GitHub: https://github.com/Bmdsaif005
