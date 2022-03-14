## Section Topics

### 17.1 - Capturing PDF Text

- 01 | PDF
    - Binary files that have plain text contained within them.
- 02 | Text
    - Copy/paste and OCR are commonly used to capture text.
      Software can programmatically do it as well.
- 03 | Common Elements
    - Author, title, sotware used and version, creation date,
      modification date, etc
    
Normally, PDF text is highlight, copy and paste.
The Python library __pdfminer__ can extract text from a PDF file.
It can also pull metadata as well, such as author, creation date,
PDF software name and version, etc.

#### Commands used in chapters
```
python3 -m venv env
source env/bin/activate
pip3 install pdfminer
python3 pdf_reader.py lorem-ipsum.pdf -t
python3 pdf_reader.py lorem-ipsum.pdf -m
```