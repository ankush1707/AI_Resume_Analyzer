
from pypdf import PdfReader


def extract_resume_text(pdf_file):

    """
    Extract text from an uploaded PDF resume.
    """

    try:
        # Read uploaded PDF
        reader = PdfReader(pdf_file)

        extracted_text = ""

        # Iterate through all PDF pages
        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        return extracted_text

    except Exception as e:
        print("Error while reading PDF:", e)
        return ""
