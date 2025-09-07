import streamlit as st
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.title("PDF Merger")

uploaded_files = st.file_uploader(
    "Upload PDFs", accept_multiple_files=True, type="pdf"
)

if uploaded_files:
    writer = PdfWriter()

    # Read each uploaded PDF and add pages
    for uploaded_file in uploaded_files:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            writer.add_page(page)

    # Save merged PDF to a bytes buffer instead of disk
    merged_pdf = BytesIO()
    writer.write(merged_pdf)
    merged_pdf.seek(0)  # move to start of buffer

    st.success("PDFs merged successfully!")

    # Provide a proper download button
    st.download_button(
        label="Download Merged PDF",
        data=merged_pdf,
        file_name="merged.pdf",
        mime="application/pdf"
    )
