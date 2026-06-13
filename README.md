IDOR-FuZz
IDOR-FuZz is a simple and effective Python tool for fuzzing IDOR (Insecure Direct Object References) vulnerabilities by testing common endpoint paths after an organization or user ID.

How It Works
The script iterates through a list of potential endpoint names and sends GET requests to:

text
https://example.com/api/organizations/{org_id}/{endpoint}
It then reports any responses that are not 404 Not Found, helping you identify which endpoints may be accessible with your ID.

Features
Customizable headers (Cookie, User-Agent)

Predefined list of common sensitive endpoints

Detects 200, 403, 405, and other non-404 responses

Prints response previews for quick analysis

Usage
Clone the repository

bash
git clone https://github.com/yourusername/IDOR-FuZz.git
cd IDOR-FuZz
Install dependencies

bash
pip install requests
Edit the script
Open the Python file and replace:

[cookiehat] → your actual session cookie

org_id → your target organization/user ID

Run the tool

bash
python idor_fuzz.py
Example Output
text
[200] /api/organizations/{org}/members
  → {"id":"7bda4b04-...","role":"admin"...
[403] /api/organizations/{org}/secrets
  → {"error":"access denied"}
[405] /api/organizations/{org}/logs
Customization
You can easily:

Add or remove endpoints in the endpoints list

Modify the base URL for other targets (not just claude.ai)

Change HTTP method (POST, PUT, etc.) if needed

Important Notes
Always have proper authorization before testing any system

Use this only on applications you own or have explicit permission to test

The author is not responsible for any misuse or illegal activity

License
MIT License – use freely, but responsibly.

