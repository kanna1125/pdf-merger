import sys
from pypdf import PdfReader, PdfWriter

output_file = sys.argv[-1]  # last argument is output file
input_files = sys.argv[1:-2]  # all other arguments are input PDFs

writer = PdfWriter()
for pdf_file in input_files:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open(output_file, "wb") as f:
    writer.write(f)

print(f"Merged PDF saved as {output_file}")
