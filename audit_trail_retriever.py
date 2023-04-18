import requests

# Ask the user to input the envelope ID
envelope_id = input("Enter the envelope ID: ")

# Define the API endpoint and headers for the first request
url = f"https://latam.esignanywhere.net/api/v4/envelope/{envelope_id}"
headers = {
    "apiToken": "{insert_it_here}"
}

# Send the first GET request with the headers
response = requests.get(url, headers=headers)

# Retrieve the Bulks list from the response
bulks_list = response.json().get("Bulks")

# Extract the first dictionary from the list
bulk_dict = bulks_list[0]

# Retrieve the LogDocumentId from the bulk_dict dictionary
log_document_id = bulk_dict.get("LogDocumentId")

# Define the API endpoint and headers for the second request
download_url = f"https://latam.esignanywhere.net/api/v4/envelope/downloadCompletedDocument/{log_document_id}"
download_headers = {
    "apiToken": "{insert_it_here}"
}

# Send the second GET request with the headers and download the response
download_response = requests.get(download_url, headers=download_headers)

# Save the downloaded document to a file
with open(f"{log_document_id}.pdf", "wb") as f:
    f.write(download_response.content)

print(f"Document saved as {log_document_id}.pdf")
