from patreon.fetch_sessionid import fetch_session_id
from patreon.fetch_all_post_ids import fetch_all_post_ids
from patreon.fetch_impression import fetch_impression
from google.create_google_sheet_add_data import create_google_sheet_add_data

# Main lambda handler
def lambda_handler(event, context):
    try:
        # Fetch all post IDs
        post_ids = fetch_all_post_ids()

        # Fetch session ID
        session_id = fetch_session_id()

        # List to store post IDs and impressions
        impression_data = []

        # Fetch impressions for each post and store the data
        for post_id in post_ids:
            impression = fetch_impression(post_id, session_id)
            if impression:
                impression_data.append(impression)

        # Add the data to Google Sheets
        if impression_data:
            sheet_id = create_google_sheet_add_data(impression_data)
            print(f"Data added to Google Sheet with ID: {sheet_id}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Test the lambda_handler function
lambda_handler("", "")
