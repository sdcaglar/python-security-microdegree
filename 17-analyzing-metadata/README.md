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

#### Commands used in chapters
```
python3 -m venv env
source env/bin/activate
pip3 install exif
python3 exif_metadata.py
```
### 17.3 - Extracting Metadata from MP3

- 01 | Audio Files
    - MP3 are the classic digital audio file, so there is a lot of
      support for them. Newer or less common files aren't as well
      supported.
- 02 | Security Issues
    - MP3 metadata is not locked down, so potentially any text
      information could be included in the tags.
- 03 | Data Extraction
    - The wide support for MP3 files in nearly any digital audio
      application, from video games to media players, means it is
      easy to access and update MP3 metadata.

Depending on the data that was embedded in the music file, there
can be a wide variety of information available.
  *  Song title
  *  Artist
  *  Album
  *  Recording data
  *  Track and disc number

#### eyeD3 program
The python program eyeD3 allows analysis of audio files, specifically MP3
files with ID3 tags embedded within the file.

It provides a command-line tool (eyeD3) and a Python library (import eyeD3)
that can be used to write your own applications or plugins that are callable
from the command-line tool.

It not only reads the data, but also allows you to write the data. Therefore
you can programmatically modify or update your music library.

Plugins are supported as well. Actually the entire program is based on plugins.
If no plugin is specified, the default "classic" tag plugin is called.

#### Commands used in chapters
```
python3 -m venv env
source env/bin/activate
pip3 install eyeD3
eyeD3 human.mp3
eyeD3 --help
```

### Helpful Resources

[eyeD3 Documentation](https://eyed3.readthedocs.io/en/latest/)
