import json
import requests


from config import settings
from problem import Problem

base_url = "https://api.notion.com/v1/databases/"
database_id = settings.db_id
request_headers = {"Authorization": settings.api_key, "Notion-Version": "2022-06-28"}

next_cursor = ""
has_more = None
query1 = {"filter": {"property": "Done", "checkbox": {"equals": True}}}
query2 = {
    "filter": {"property": "Done", "checkbox": {"equals": True}},
    "start_cursor": next_cursor,
}

pagination_list = []
problem_map = {}
problem_list = []


# Check for connectivity with notion API
def check_connectivity():

    # Send get request to API and capture response
    response = requests.get(base_url + database_id, headers=request_headers)

    # If response status code is 2000 i.e. the response is successfull
    # continue and leave the function
    if response.status_code == 200:
        return True

    # In case if the response is incorrect
    else:
        # Check for internet connectivity
        try:
            # Trying to send a get request to google.com to check what happens
            resp = requests.get("https://www.google.com")

            # If we are able to connect to google.com, this means internet conenction is present
            # Which means, there must be something wrong with database ID or integration token
            if resp.status_code == 200:
                print("Something is wrong with you database Id or intergation token.")
                print("Please check it and try again.")

            # If we are unable to connect to google.com, it means there is no internet connection
            # available
            else:
                print("Unable to connect to the internet.")
                print("Please check your internet connection and try again")

            return False
        # Exception handling
        except Exception as err:
            print("Some exception occured...please try again", err)
            return False


def check_query(next_cursor: str):
    if not len(next_cursor):
        query = {
            "filter": {
                "and": [
                    {"property": "Done", "checkbox": {"equals": True}},
                    {
                        "property": "Data Structures",
                        "multi_select": {"contains": "Linked List"},
                    },
                ]
            }
        }
    else:
        query = {
            "filter": {
                "and": [
                    {"property": "Done", "checkbox": {"equals": True}},
                    {
                        "property": "Data Structures",
                        "multi_select": {"contains": "Linked List"},
                    },
                ]
            },
            "start_cursor": next_cursor,
        }
    return query


def retrieve_data(query: str):
    # This is how the curl GET request should be
    """
    curl -X GET https://api.notion.com/v1/database/{database_id} \
    -H "Authorization: Bearer {INEGRATION_TOKEN}" \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2021-05-13" \
    """

    # We will use the response generated above to get the data
    response_data = requests.post(
        base_url + database_id + "/query", headers=request_headers, json=query
    )

    # Get json data from response
    data = response_data.json()

    # Return json data
    return data


def get_all_records():
    start_cursor = ""
    response = retrieve_data(check_query(start_cursor))

    has_more = response["has_more"]
    pagination_list.append(response)
    start_cursor = response["next_cursor"]

    while has_more:
        new_response = retrieve_data(check_query(start_cursor))
        has_more = new_response["has_more"]
        pagination_list.append(new_response)

    for i in range(len(pagination_list)):
        print(Problem.decode_data(pagination_list[i]))


def dict_decoder(x):
    return [i for i in x]


response1 = retrieve_data(query1)

muti_select = response1["results"][6]["properties"]["Data Structures"]["multi_select"]
response1_str = json.dumps(muti_select, indent=4)
print(Problem.get_patterns(muti_select))

# date = response1["results"][0]["last_edited_time"]
# dt = parser.parse(date)
# print(dt.date())


# problem = dict_decoder(response1["results"][0]["properties"]["Problem"]["title"][0]["plain_text"])
# problem = response1_str
# print(problem)
get_all_records()
print(len(pagination_list))
# print(dict_decoder(response1))
print(len(problem_list))
# print(problem_map)
# check_connectivity()
