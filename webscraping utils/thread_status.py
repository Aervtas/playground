import requests

def get_thread_status(board, thread_id):
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        thread_data = response.json()
        
        if "closed" in thread_data["posts"][0]:
            status = thread_data["posts"][0]["closed"]
            if status:
                print("Thread is closed.")
            else:
                print("Thread is open.")
        else:
            print("Thread is open.")

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

# Specify the board and thread ID
board = "wg"
thread_id = 7968529

# Call the function to get the thread status
get_thread_status(board, thread_id)
