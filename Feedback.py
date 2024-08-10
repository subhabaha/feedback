import google.generativeai as genai
import os
import streamlit as st
from fpdf import FPDF
import tempfile

os.environ["API_KEY"]='AIzaSyBGo6U2he1QpppItMKpSW2jzy5BI_mKRnE'

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()

    # Replace with correct PDF content formatting
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Feedback Questions for External Stakeholders", ln=1, align='C')
    pdf.multi_cell(0, 5, txt=text)

    pdf_file = "Feedback Questions.pdf"
    pdf.output(pdf_file)
    return pdf_file

    # Use a temporary file for PDF creation
    #with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
     #   pdf.output(temp_file.name)
      #  return temp_file.name



def main():
    st.title("Feedback Question Generator")
    course_outcomes = st.text_area("Enter course outcomes (one per line):")
    course_outcomes = course_outcomes.strip().split("\n")

    if st.button("Generate Feedback Questions"):
        genai.configure(api_key=os.environ["API_KEY"])
        model = genai.GenerativeModel('gemini-1.0-pro')
        prompt = (f"create one feedback MCQ question each for each Course outcomes with 4 options of MCQs as 0 Dont Agree 1 - Neutral 2 - Somewhat Agree 3 Strongly Agree. The course outcomes are: {course_outcomes}. The way feedback question is asked should match the MCQ options. display the feedback questons along with options ")
        response = model.generate_content(prompt)
        st.write(response.text)

        # Generate and download PDF
        pdf_file = generate_pdf(response.text)
        st.write("Download the combined report:")
        with open(pdf_file, "rb") as file:
            st.download_button(label="Download PDF", data=file, file_name=pdf_file, mime='application/pdf')


if __name__ == "__main__":
  main()

