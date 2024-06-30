import re
from pdfminer.high_level import extract_pages, extract_text


for page_layout in extract_pages("PDF-Bearbeitung/Beispiel.pdf"):
    for element in page_layout:
        print(element)

text = extract_text("PDF-Bearbeitung/Beispiel.pdf")
print(text)

pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)


page = extract_pages("PDF-Bearbeitung/Beispiel.pdf")
print(page)
