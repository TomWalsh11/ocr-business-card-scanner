# OCR & GPT Info Extraction 🖼️🤖

This repository contains a project that combines **Azure's OCR API** and **OpenAI's GPT model** to extract and process text from images. The extracted text is parsed to identify key information, including:  
- **Name**  
- **Title**  
- **Company**  
- **Phone**  
- **Email**

---

## 📂 Repo Structure

- **`main.py`**: Main script that processes images and extracts information.
- **`.env`**: Stores environment variables required for Azure OCR and OpenAI GPT APIs.
- **`.gitignore`**: Specifies files and directories to be ignored by Git (e.g., `.env` and other sensitive files).
- **`contact.jpg`**: Example image file used for testing the OCR functionality.
- **`LICENSE`**: MIT license for the project.
- **`requirements.txt`**: Specifies the dependencies required to run the project.

---

## 🚀 Features

1. **OCR with Azure Cognitive Services**: Extracts text from images using Azure's Computer Vision API.  
2. **Information Parsing with OpenAI GPT**: Processes the extracted text and identifies structured information fields like Name, Title, Company, etc.  
3. **Customizable Environment**: Easily configure API keys and image paths via the `.env` file.  

---

## 🛠️ Requirements

### Prerequisites
- **Python 3.x**  
- Azure Cognitive Services Subscription (Key and Endpoint)  
- OpenAI API Key  

### Installation
1. Clone the repository:  

   ```bash
   git clone https://github.com/TomWalsh11/ocr-business-card-scanner.git
   cd ocr-gpt-project

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Create a .env file with your credentials:

   ```bash
   AZURE_KEY=your_azure_subscription_key
   AZURE_ENDPOINT=your_azure_endpoint
   IMAGE_PATH=path_to_your_image
   OPENAI_API_KEY=your_openai_api_key

---

## ▶️ Usage

1. Add your image file path to the `IMAGE_PATH` variable in `.env`.

2. Run the script:
   
   ```bash
   python main.py

3. View the extracted information in the console:

   ```bash
   Name: [extracted_name]
   Title: [extracted_title]
   Company: [extracted_company]
   Phone: [extracted_phone]
   Email: [extracted_email]

---

## 🔧 Customization

- Modify the prompt in the `extract_info` function to adjust how the GPT model parses the text.
- Change the image file dynamically by updating the `IMAGE_PATH` in the `.env` file.

---

## 📋 Results

This project demonstrates:
- Seamless integration of Azure OCR and OpenAI GPT for text extraction and processing.
- Automated information parsing from unstructured text data.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📧 Contact

For questions or support, reach out at [tdjwalsh@hotmail.com](mailto:tdjwalsh@hotmail.com).
