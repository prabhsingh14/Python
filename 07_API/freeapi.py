import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url).json()

    if response["success"] and "data" in response:
        user_data =  response["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]

        return username, country
    
    else:
        raise Exception("Failed to Fetch User Data")
    
def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"{username} from {country}")
    except Exception as ex:
        print(str(ex))

if __name__ == "__main__":
    main()