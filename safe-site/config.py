from dotenv import load_dotenv
from os import getenv


load_dotenv()

api_key = getenv("API_KEY", "f1b76db88366373016efe614824c3aadae45e70fe36b2b199b6c9771fb9584f3")
site_risks = getenv("SITE_RISKS", ['malware', 'phishing', 'malicious'])
