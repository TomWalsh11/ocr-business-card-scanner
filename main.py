from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
from openai import OpenAI
import os

# Azure credentials
load_dotenv()
subscription_key = os.getenv('AZURE_KEY')
endpoint = os.getenv('AZURE_ENDPOINT')
print(subscription_key)
print(endpoint)
# Authenticate the client
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Path to your image
image_path = os.getenv('IMAGE_PATH')

# Open the image file
with open(image_path, "rb") as image_stream:
    # Call the Azure OCR API
    ocr_result = client.recognize_printed_text_in_stream(image_stream, language="en")

# Extract text from OCR result
extracted_text = "\n".join(
    [" ".join([word.text for word in line.words]) for region in ocr_result.regions for line in region.lines]
)

# Print the extracted text
print(extracted_text)

# OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Function to parse the extracted OCR text using OpenAI's GPT model
def extract_info(text):
    # Query OpenAI API with the provided text using gpt-3.5-turbo-instruct model
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt = f"""
        Extract the following fields from the text below: 
        - Name
        - Title
        - Company
        - Phone
        - Email
        
        If a field is not found, return "Not found." 
        Here's the text: 

        {extracted_text}
        """,
        max_tokens=150,
        temperature=0
    )
    
    # Extract the result from the response
    result = response.choices[0].text.strip()
    
    # Parse the result into variables
    name = "Not found"
    title = "Not found"
    company = "Not found"
    phone = "Not found"
    email = "Not found"
    
    # Split the result into lines and assign values to variables
    for line in result.split("\n"):
        if line.startswith("Name:"):
            name = line.replace("Name:", "").strip()
        elif line.startswith("Title:"):
            title = line.replace("Title:", "").strip()
        elif line.startswith("Company:"):
            company = line.replace("Company:", "").strip()
        elif line.startswith("Phone:"):
            phone = line.replace("Phone:", "").strip()
        elif line.startswith("Email:"):
            email = line.replace("Email:", "").strip()
    
    return name, title, company, phone, email

# Example usage
name, title, company, phone, email = extract_info(extracted_text)

print(f"Name: {name}")
print(f"Title: {title}")
print(f"Company: {company}")
print(f"Phone: {phone}")
print(f"Email: {email}")
