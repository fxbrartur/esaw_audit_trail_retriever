# eSignAnywhere Audit Trail Retriever

This script downloads a completed document from a Namirial envelope using the Envelope ID.

### Requirements
- Python 3.x
- Requests library

### Installation
- Download and install Python from the official website: https://www.python.org/downloads/
- Install the Requests library using pip:
```
pip install requests
```

### Usage
- Replace the apiToken value in the headers dictionary with your own API token.
- Verify that the URLs in the script point to the correct eSAW instance and API version for your use case.
- Run the script and enter the Envelope ID when prompted:
```
python audit_trail_retriever.py
```
The script will download the completed document to your current working directory.

### Support
If you encounter any issues or have any questions, please reach out to my support email at a.barbosa@external.namirial.com

