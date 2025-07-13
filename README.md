# FILE-INTEGRITY-CHECKER

COMPANY: CODTECH IT SOLUTIONS

NAME: YUSUF IRFAN M

INTERN ID: CT04DH428

DOMAIN: CYBERSECURITY & ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Objective:

--> To build a Python-based tool that monitors changes in a file over time.

--> It works by calculating and comparing the file’s SHA-256 hash value.

--> Detects if a file has been tampered with, modified, or corrupted.

Tools and Technologies Used:

--> Python 3.13+
Used as the primary programming language for building the integrity logic and server.

--> Flask (Web Framework)
Creates a simple web interface where users can upload files and check integrity directly in a browser.

--> hashlib
Python’s built-in cryptographic library used to compute the SHA-256 hash of uploaded files.

--> VS Code (Visual Studio Code)
Used for writing, organizing, and executing Python code and HTML templates.

--> HTML
Used to build a clean upload form inside index.html using Flask’s Jinja2 templating.

--> Google Chrome
Used to access the web interface and view real-time results of file integrity scans.

Folder Structure:

File Integrity Checker/
├── app.py                → Flask server (routes, logic, result rendering)
├── integrity_checker.py  → Function to calculate file hash
└── templates/
    └── index.html        → Web interface (upload form + results)

How It Works (Step-by-Step):

1. User runs python app.py in VS Code terminal.


2. A local Flask server starts at http://127.0.0.1:5000.


3. User opens the URL in Google Chrome.


4. A file upload form is shown in the browser.


5. User uploads a file (e.g., report.pdf or notes.txt).


6. The application reads the file and calculates its SHA-256 hash.


7. On first upload: hash is stored as the “original”.


8. On second upload (same or modified file):

9. The new file’s hash is compared with the stored one.

--> If it matches →  File is unchanged.

--> If it differs → File has been modified!

Key Features:

--> Fast, lightweight, and accurate file checking tool.

--> Shows results clearly in Google Chrome, not just terminal.

--> Works for any file type: .txt, .pdf, .docx, .jpg, etc.

--> Uses strong SHA-256 hashing, same algorithm used in blockchain & digital signatures.

--> Supports multiple upload checks in one session.

Real-Life Use Cases:

--> Check if a sensitive document has been modified.

--> Detect file corruption after downloading or copying.

--> Monitor critical config files in penetration testing or sysadmin work.

--> Use in software development pipelines to verify binary integrity.

How to Run:

pip install flask
python app.py

Then visit:

http://127.0.0.1:5000

Upload a file → hash is saved → re-upload same or modified file → check result.

Output:


