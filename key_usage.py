#Python Program: Extracting Keywords from Text


from rake_nltk import Rake

def extract_keywords(text):
    rake = Rake()  # Uses stopwords for English from NLTK and punctuation
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases()  # List of keywords ranked by relevance
    return keywords

# Example usage
sample_text = """
Python is a powerful programming language used in web development, 
data science, automation, and artificial intelligence.
"""
keywords = extract_keywords(sample_text)

print("Extracted Keywords:")
for kw in keywords:
    print("-", kw)

---

#1. Convert PDF to Text (File Handling + Automation)

import PyPDF2

def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Usage
# print(pdf_to_text("sample.pdf"))

> Install with: pip install PyPDF2




---

#2. Send an Email Automatically (Automation)

import smtplib
from email.message import EmailMessage

def send_email(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = "your_email@example.com"

    # Login details
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@example.com", "your_password")
    server.send_message(msg)
    server.quit()

# Usage
# send_email("Hello", "This is a test email!", "receiver@example.com")

> For Gmail, enable "Less secure apps" or use App Password.




---

#3. Currency Converter Using API

import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_currency.upper()]
    return amount * rate

# Example: print(convert_currency(100, "USD", "INR"))

> Install: pip install requests




---

#4. Generate Strong Passwords (Security)

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example: print(generate_password())


---

#5. Check Internet Speed

import speedtest

def check_speed():
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000  # Mbps
    upload = st.upload() / 1_000_000      # Mbps
    return f"Download: {download:.2f} Mbps, Upload: {upload:.2f} Mbps"

# print(check_speed())

> Install: pip install speedtest-cli




---


