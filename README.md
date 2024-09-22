# MedicalChatbot
This project is a medical chatbot built using Google Gemini Pro, specialized in gastroenterology. The chatbot collects symptoms from patients, provides triage and potential diagnosis, and can read and interpret health reports to assist in identifying possible conditions.

Features
Symptom Collection: Interactive chat-based symptom collection tailored to gastroenterology.
Triage and Diagnosis: Uses AI to analyze symptoms and suggest possible diagnoses based on clinical data.
Health Report Reading: Capable of interpreting health reports (PDFs, text, etc.) to enhance symptom analysis and provide more accurate diagnosis.
AI Model: Powered by Google Gemini Pro, which provides robust natural language understanding, especially in the medical field.
Secure and Compliant: Ensures data privacy and follows HIPAA compliance for handling patient data.
Installation
Clone the Repository:

bash
git clone https://github.com/your-username/gastro-medical-chatbot.git
cd gastro-medical-chatbot
Set Up Virtual Environment:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
pip install -r requirements.txt
API Keys and Configuration:

Create a .env file in the root directory to store your API keys for Google Gemini and other services.

env
GOOGLE_GEMINI_API_KEY=your-google-gemini-api-key
Run the Application:

bash
streamlit run app.py


Usage
Open the chatbot UI by running the application as described above.
Engage with the chatbot by providing your gastroenterology-related symptoms.
Upload a health report (PDF) to enhance the diagnostic capability.
The chatbot will respond with possible diagnoses and triage suggestions based on the information provided.
Features Overview
1. Symptom Collection
The chatbot uses a conversational interface to collect detailed symptoms from the user, focusing on gastroenterological conditions like abdominal pain, digestive issues, nausea, and more.

2. Triage and Diagnosis
Leveraging Google Gemini Pro, the chatbot analyzes the symptoms and suggests possible conditions that match the user's inputs, offering guidance for further medical consultations.

3. Health Report Reading
The chatbot can read and interpret health reports, especially laboratory and diagnostic reports, enhancing its diagnostic ability by cross-referencing with user-provided symptoms.

Project Structure
bash
Copy code
gastro-medical-chatbot/
│
├── app.py                # Main entry point of the Streamlit app
├── utils/
│   ├── symptom_analysis.py  # Symptom analysis logic
│   ├── report_reader.py     # Health report parsing and analysis
│   └── ...
├── models/
│   └── google_gemini.py    # Google Gemini integration
├── data/
│   └── sample_reports/     # Example health reports for testing
├── .env                    # API keys and environment variables
├── README.md               # This README file
└── requirements.txt        # Project dependencies
Tech Stack
Frontend: Streamlit
AI Model: Google Gemini Pro
Backend: Python (FastAPI)
Health Data Analysis: Custom NLP models using Google Gemini's API

Contributing
We welcome contributions! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

