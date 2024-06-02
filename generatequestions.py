import pymysql
import json

# Connect to the MySQL database
def connect_to_database():
    return pymysql.connect(host='127.0.0.1',  # Replace 'localhost' with your MySQL server host
                           user='root',  # Replace with your MySQL username
                           password='',  # Replace with your MySQL password
                           database='scholarship_demo',  # Replace with your MySQL database name
                           cursorclass=pymysql.cursors.DictCursor)


# Fetch scholarship data from the database
def fetch_scholarship_data(connection):
    print("Fetching scholarship data from database...")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM scholarships")
        data = cursor.fetchall()
        print(f"Fetched {len(data)} rows.")
        return data

# Convert scholarship data to JSON format
def convert_to_json(scholarship_data):
    print("Converting scholarship data to JSON format...")
    scholarships = []
    for row in scholarship_data:
        scholarship = {
            "title": row.get('title', 'N/A'),
            "award": row.get('award', 'N/A'),
            "criteria": row.get('criteria', 'N/A'),
            "deadline": str(row.get('deadline', 'N/A')),  # Convert to string if not already
            "url": row.get('url', 'N/A'),
            "graduation": row.get('graduation', 'N/A'),
            "gender": row.get('gender', 'N/A'),
            "state": row.get('state', 'N/A'),
            "eligibility_description": row.get('eligibility_description', 'N/A'),
            "test": row.get('test', 'N/A'),
            "questions": {
                "title_questions": [
                    "What is the title of the scholarship? ({} title)".format(row.get('title', 'N/A')),
                    "Can you provide more details about the scholarship title? ({} title)".format(row.get('title', 'N/A')),
                    "What makes {} scholarship unique?".format(row.get('title', 'N/A')),
                    "How does {} scholarship contribute to the field of study?".format(row.get('title', 'N/A')),
                    "Who is offering {} scholarship?".format(row.get('title', 'N/A')),
                    "How long has {} scholarship been available?".format(row.get('title', 'N/A')),
                    "What are the key features of {} scholarship?".format(row.get('title', 'N/A')),
                    "How can one apply for {} scholarship?".format(row.get('title', 'N/A')),
                    "What is the history behind {} scholarship?".format(row.get('title', 'N/A')),
                    "What are the benefits of receiving {} scholarship?".format(row.get('title', 'N/A')),
                    "Who can benefit from {} scholarship?".format(row.get('title', 'N/A')),
                    "How does {} scholarship impact the community?".format(row.get('title', 'N/A')),
                    "What inspired the creation of {} scholarship?".format(row.get('title', 'N/A')),
                    "What are the selection criteria for {} scholarship?".format(row.get('title', 'N/A')),
                    "Is {} scholarship renewable?".format(row.get('title', 'N/A')),
                    "How can recipients maintain {} scholarship?".format(row.get('title', 'N/A')),
                    "Are there any alumni of {} scholarship?".format(row.get('title', 'N/A')),
                    "What are the success stories associated with {} scholarship?".format(row.get('title', 'N/A')),
                    "How is {} scholarship funded?".format(row.get('title', 'N/A')),
                    "What partnerships are involved in {} scholarship?".format(row.get('title', 'N/A')),
                ],
                "award_questions": [
                    "What is the award amount for {}?".format(row.get('title', 'N/A')),
                    "Can you provide details about the award for {}?".format(row.get('title', 'N/A')),
                    "How much financial support does {} provide?".format(row.get('title', 'N/A')),
                    "What are the benefits of receiving the award for {}?".format(row.get('title', 'N/A')),
                    "How is the award amount determined for {}?".format(row.get('title', 'N/A')),
                    "Are there any additional benefits associated with the award for {}?".format(row.get('title', 'N/A')),
                    "How will recipients receive the award for {}?".format(row.get('title', 'N/A')),
                    "Are there any conditions for receiving the award for {}?".format(row.get('title', 'N/A')),
                    "Can recipients use the award for any purpose?".format(row.get('title', 'N/A')),
                    "Is the award for {} renewable or one-time?".format(row.get('title', 'N/A')),
                    "How does the award for {} benefit the recipients?".format(row.get('title', 'N/A')),
                    "What impact does the award for {} have on the recipients' education?".format(row.get('title', 'N/A')),
                    "Are there any alumni who have received the award for {}?".format(row.get('title', 'N/A')),
                    "How does the award for {} contribute to the recipients' career goals?".format(row.get('title', 'N/A')),
                    "How does the award for {} support the recipients' research or projects?".format(row.get('title', 'N/A')),
                    "What recognition comes with the award for {}?".format(row.get('title', 'N/A')),
                    "How does the award for {} help recipients overcome financial barriers?".format(row.get('title', 'N/A')),
                    "What role does the award for {} play in the recipients' personal development?".format(row.get('title', 'N/A')),
                    "How does the award for {} contribute to the recipients' professional network?".format(row.get('title', 'N/A')),
                    "What testimonials exist regarding the impact of the award for {}?".format(row.get('title', 'N/A')),
                ],
                "criteria_questions": [
                    "What are the eligibility criteria for {}?".format(row.get('title', 'N/A')),
                    "Can you provide details about eligibility for {}?".format(row.get('title', 'N/A')),
                    "What qualifications are needed for {}?".format(row.get('title', 'N/A')),
                    "What are the specific requirements for eligibility for {}?".format(row.get('title', 'N/A')),
                    "Who is eligible to apply for {}?".format(row.get('title', 'N/A')),
                    "How can one meet the eligibility criteria for {}?".format(row.get('title', 'N/A')),
                    "Are there any specific restrictions on eligibility for {}?".format(row.get('title', 'N/A')),
                    "What are the key factors considered for eligibility for {}?".format(row.get('title', 'N/A')),
                    "Is there an age limit for eligibility for {}?".format(row.get('title', 'N/A')),
                    "Are international students eligible for {}?".format(row.get('title', 'N/A')),
                    "What documents are required for eligibility for {}?".format(row.get('title', 'N/A')),
                    "Are there any exceptions to the eligibility criteria for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility criteria for {} differ from other scholarships?".format(row.get('title', 'N/A')),
                    "What impact do the eligibility criteria for {} have on the applicant pool?".format(row.get('title', 'N/A')),
                    "How does meeting the eligibility criteria for {} increase the chances of receiving the scholarship?".format(row.get('title', 'N/A')),
                    "What role does eligibility play in the selection process for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility criteria for {} reflect the values of the scholarship?".format(row.get('title', 'N/A')),
                    "What support is available to help applicants meet the eligibility criteria for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility criteria for {} align with the scholarship's goals?".format(row.get('title', 'N/A')),
                    "What feedback has been provided regarding the eligibility criteria for {}?".format(row.get('title', 'N/A')),
                ],
                "deadline_questions": [
                    "What is the deadline for applying to {}?".format(row.get('title', 'N/A')),
                    "When is the application deadline for {}?".format(row.get('title', 'N/A')),
                    "Can you provide the application deadline for {}?".format(row.get('title', 'N/A')),
                    "How much time do applicants have before the deadline for {}?".format(row.get('title', 'N/A')),
                    "Is there an early application deadline for {}?".format(row.get('title', 'N/A')),
                    "What happens if an applicant misses the deadline for {}?".format(row.get('title', 'N/A')),
                    "Can the deadline for {} be extended under special circumstances?".format(row.get('title', 'N/A')),
                    "How can applicants ensure they meet the deadline for {}?".format(row.get('title', 'N/A')),
                    "What is the process for submitting applications before the deadline for {}?".format(row.get('title', 'N/A')),
                    "Are there any time zone considerations for the deadline for {}?".format(row.get('title', 'N/A')),
                    "How strict is the deadline for {}?".format(row.get('title', 'N/A')),
                    "What support is available to help meet the deadline for {}?".format(row.get('title', 'N/A')),
                    "How is the deadline for {} communicated to applicants?".format(row.get('title', 'N/A')),
                    "What are the consequences of missing the deadline for {}?".format(row.get('title', 'N/A')),
                    "Are there any reminders for the deadline for {}?".format(row.get('title', 'N/A')),
                    "How does the deadline for {} impact the selection process?".format(row.get('title', 'N/A')),
                    "What is the timeline for the application process for {}?".format(row.get('title', 'N/A')),
                    "What strategies can applicants use to meet the deadline for {}?".format(row.get('title', 'N/A')),
                    "How does the deadline for {} compare to other scholarships?".format(row.get('title', 'N/A')),
                    "What factors influenced the setting of the deadline for {}?".format(row.get('title', 'N/A')),
                ],
                "test_questions": [
                    "Is there a test required for {}?".format(row.get('title', 'N/A')),
                    "What kind of test is required for {}?".format(row.get('title', 'N/A')),
                    "Can you provide details about the test for {}?".format(row.get('title', 'N/A')),
                    "How can applicants prepare for the test for {}?".format(row.get('title', 'N/A')),
                    "What resources are available for test preparation for {}?".format(row.get('title', 'N/A')),
                    "Are there any sample questions available for the test for {}?".format(row.get('title', 'N/A')),
                    "How is the test for {} administered?".format(row.get('title', 'N/A')),
                    "Are there any fees associated with the test for {}?".format(row.get('title', 'N/A')),
                    "What is the format of the test for {}?".format(row.get('title', 'N/A')),
                    "How long is the test for {}?".format(row.get('title', 'N/A')),
                    "What accommodations are available for the test for {}?".format(row.get('title', 'N/A')),
                    "How soon are test results available for {}?".format(row.get('title', 'N/A')),
                    "What happens if an applicant does not pass the test for {}?".format(row.get('title', 'N/A')),
                    "Can the test for {} be retaken?".format(row.get('title', 'N/A')),
                    "How does the test for {} compare to other scholarship tests?".format(row.get('title', 'N/A')),
                    "What feedback is provided after the test for {}?".format(row.get('title', 'N/A')),
                    "How does the test for {} reflect the scholarship's goals?".format(row.get('title', 'N/A')),
                ],
                "url_questions": [
                    "What is the URL for more information about {}?".format(row.get('title', 'N/A')),
                    "Can you provide the website link for {}?".format(row.get('title', 'N/A')),
                    "Where can applicants find more details about {} online?".format(row.get('title', 'N/A')),
                    "Is there a webpage dedicated to {}?".format(row.get('title', 'N/A')),
                    "How can applicants access the official website for {}?".format(row.get('title', 'N/A')),
                    "Are there any additional resources available on the website for {}?".format(row.get('title', 'N/A')),
                    "What information is available on the URL provided for {}?".format(row.get('title', 'N/A')),
                    "Is there an online application portal linked to the URL for {}?".format(row.get('title', 'N/A')),
                    "Are there any updates or announcements available on the website for {}?".format(row.get('title', 'N/A')),
                    "Can applicants contact the scholarship provider through the website provided for {}?".format(row.get('title', 'N/A')),
                    "How often is the website for {} updated?".format(row.get('title', 'N/A')),
                    "What features are available on the website for {}?".format(row.get('title', 'N/A')),
                    "How user-friendly is the website for {}?".format(row.get('title', 'N/A')),
                    "What feedback has been provided regarding the website for {}?".format(row.get('title', 'N/A')),
                    "How does the website for {} support the application process?".format(row.get('title', 'N/A')),
                    "What role does the website for {} play in providing information to applicants?".format(row.get('title', 'N/A')),
                    "How does the website for {} align with the scholarship's goals?".format(row.get('title', 'N/A')),
                    "What improvements have been made to the website for {} over time?".format(row.get('title', 'N/A')),
                    "How can applicants navigate the website for {} effectively?".format(row.get('title', 'N/A')),
                    "What role does the website for {} play in promoting transparency?".format(row.get('title', 'N/A')),
                ],
                "eligibility_description_questions": [
                    "What is the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "Can you provide details about the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "What specific qualifications are outlined in the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility description for {} define the target applicants?".format(row.get('title', 'N/A')),
                    "What are the key components of the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility description for {} align with the scholarship's mission?".format(row.get('title', 'N/A')),
                    "Are there any notable requirements in the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How can applicants interpret the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "What support is available to help understand the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility description for {} impact the application process?".format(row.get('title', 'N/A')),
                    "What role does the eligibility description for {} play in the selection criteria?".format(row.get('title', 'N/A')),
                    "How does the eligibility description for {} compare to other scholarships?".format(row.get('title', 'N/A')),
                    "What feedback has been received regarding the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How often is the eligibility description for {} reviewed or updated?".format(row.get('title', 'N/A')),
                    "What changes have been made to the eligibility description for {} over time?".format(row.get('title', 'N/A')),
                    "How can applicants ensure they meet the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "What resources are available to help applicants meet the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility description for {} impact the number of applicants?".format(row.get('title', 'N/A')),
                    "What success stories are associated with the eligibility description for {}?".format(row.get('title', 'N/A')),
                    "How does the eligibility description for {} align with the scholarship's goals?".format(row.get('title', 'N/A')),
                ],
            }
        }
        scholarships.append(scholarship)
    print(f"Converted {len(scholarships)} scholarships to JSON format.")
    return scholarships

# Write scholarship data to a JSON file
def write_to_json(scholarships, file_name='scholarships_data.json'):
    print(f"Writing data to {file_name}...")
    with open(file_name, 'w') as json_file:
        json.dump(scholarships, json_file, indent=4)
    print(f"Data successfully written to {file_name}.")

# Main function to execute the process
def main():
    connection = connect_to_database()
    try:
        scholarship_data = fetch_scholarship_data(connection)
        scholarships = convert_to_json(scholarship_data)
        write_to_json(scholarships)
    finally:
        connection.close()

if __name__ == "__main__":
    main()
