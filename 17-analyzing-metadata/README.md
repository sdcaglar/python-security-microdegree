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

### 17.2 - Extracting Photo Data

- 01 | EXIF
    - Digital cameras include a lot of metadata by default.
- 02 | Security Issues
    - EXIF data can leak potentially sensitive information,
      such as PII, location information, etc.
- 03 | Data Extraction
    - Web sites, browser plugins and simply programs can extract
      EXIF data from images.
      
#### Extracting Metadata from Photos
EXIF (Exchangeable Image File Format) is most common metadata
associated with digital photos.

EXIF data includes ISO speed, shutter speed, aperture, white
balance, camera make and model, etc.

Embedded within the image file itself, i.e. not part of the image
but part of the file's data. Data can be modified or deleted to keep
file sizes small, protect IP associated with the image, remove sensitive
information like GPS coordinates, etc.
```
python3 -m venv env
source env/bin/activate
pip3 install exif
python3 exif_metadata.py
```
