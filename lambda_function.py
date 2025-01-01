from patreon.fetch_all_post_ids import fetch_all_post_ids
from patreon.fetch_impression import fetch_impression
from google.add_data_to_google_sheet import add_data_to_google_sheet
import os
from dotenv import load_dotenv

load_dotenv("patreon/.env")

# Main lambda handler
def lambda_handler(event, context):
    try:
        # Fetch all post IDs
        post_ids = fetch_all_post_ids()

        # Declare Patreon session ID
        session_id = os.getenv("PATRON_SESSION_ID")

        # List to store post IDs and impressions
        impression_data = []

        # Fetch impressions for each post and store the data
        for post_id in post_ids:
            impression = fetch_impression(post_id, session_id)
            if impression:
                impression_data.append(impression)

        # Add the data to Google Sheets
        if impression_data:
            sheet_id = add_data_to_google_sheet(impression_data)
            print(f"Data added to Google Sheet with ID: {sheet_id}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Test the lambda_handler function
lambda_handler("", "")
