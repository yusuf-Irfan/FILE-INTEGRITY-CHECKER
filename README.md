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



Tools & Technologies Used:

1. Python 3.10+:

Core programming language used to build the application due to its readability, wide library support, and community backing.



2. hashlib Library:

Standard Python library used to generate cryptographic hash values like SHA-256.

Ensures file data is converted into unique, fixed-size strings that change even with the slightest file modification.



3. VS Code (Visual Studio Code):

Code editor used for writing, editing, and debugging Python scripts.

Integrated terminal and Git support helped with testing and version control.



4. OS and File I/O Libraries (os, sys):

Used for interacting with the file system (reading files, checking paths, etc.).



5. Command-Line Interface (CLI):

The tool runs from the terminal, offering options like scanning files and verifying integrity via arguments or prompts.



6. Optional: JSON / Text File Storage:

To save and compare original file hash values for future verification.


Steps Followed During Development:

1. Planning the Workflow:

Defined the structure: two main functionalities were needed — hashing files and verifying file integrity.

Decided to implement a modular approach, separating logic into functions or modules for scalability.



2. Hash Calculation Module (calculate_hash):

Created a function that takes a file path and returns its SHA-256 hash.

Read the file in binary mode using chunks (buffering) to support large files efficiently.

Used hashlib.sha256() to compute the hash securely.



3. Integrity Verification Module:

Built a function to load original hash values (stored during a secure baseline) and compare them with current file hashes.

If a mismatch is detected, the tool prints an alert indicating possible tampering or corruption.



4. Error Handling & Validation:

Added exceptions for missing files, read errors, or permission issues.

Ensured that invalid paths or corrupted data do not crash the program.



5. User Input Handling (CLI):

Provided options to users:

Save current hash as original

Verify a file's current hash against the saved hash


Used input prompts and command-line arguments for interaction.



6. Testing the Tool:

Created test files to confirm that the tool detects:

No changes (identical hash)

Any modification (different hash)


Tested on multiple file types: .txt, .pdf, .py, .docx.



7. Import Error Fixing:

Solved ImportError for the calculate_hash function by:

Ensuring proper file/module naming

Avoiding circular imports

Correct folder structure (e.g., using _init_.py if needed)



Use Cases:

Security Monitoring: Alerts administrators if a sensitive file is modified.

Digital Forensics: Ensures evidence files have not been altered.

Backup Verification: Confirms that backups remain intact over time.

Software Distribution: Ensures executable files are not tampered with.


Key Takeaways:

Cryptographic hashes are powerful tools for ensuring data integrity.

Even a 1-character change in a file will result in a completely different hash.

Python's hashlib makes implementing such tools efficient and reliable.

File Integrity Checkers are lightweight but important security utilities for organizations and personal use.


Output:

"https://github.com/user-attachments/assets/3c4834bf-f3b7-4828-89ed-bb625e34a26d" />
"https://github.com/user-attachments/assets/5eba3b9a-0925-4caf-a275-96670cfbee93" />
"https://github.com/user-attachments/assets/a74880a8-1842-499e-be2f-e9bbc33c382b" />
"https://github.com/user-attachments/assets/bb6d6963-0222-4c99-a775-40aafcafe968" />
