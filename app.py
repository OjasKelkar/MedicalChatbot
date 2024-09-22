import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model for chat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to handle symptoms and provide diagnosis/triage
def get_gastro_response(question, image=None):
    try:
        # If image is provided, include in the prompt
        if image:
            question += " The patient has also provided an image that might be relevant."

        # Send message to the model and get the response
        response = chat.send_message(
            f"You are a personalized doctor assisatant you have speciality in gastroenterology .A patient is describing the following symptoms: {question}. Please provide a diagnosis or a potential triage path in gastroenterology.",
            stream=True
        )
        return response
    except Exception as e:
        return [f"Error: {str(e)}"]

# Initialize Streamlit app
st.set_page_config(page_title="Gastroenterology Symptom Checker")

st.header("Gastroenterology Symptom Collection & Diagnosis")

# Input area for patients to describe symptoms
input = st.text_area("Please describe your symptoms in detail:", key="input")

# Image uploader for relevant visuals (e.g., medical images)
uploaded_image = st.file_uploader("Attach an image if relevant (optional):", type=["jpg", "jpeg", "png"])

# Display uploaded image (if any)
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Submit")

# If submit button is clicked
if submit:
    if input:
        response = get_gastro_response(input, image=uploaded_image)

        st.subheader("Possible Diagnosis and Triage Plan")
        
        for chunk in response:
            # Display only the text portion of the model's response
            st.write(chunk.text)

        st.write("_" * 80)  # Separator for readability

    else:
        st.error("Please enter your symptoms before submitting.")
