import facebook

def is_valid_access_token(access_token):
    try:
        graph = facebook.GraphAPI(access_token)
        # make a request to /me to check if the token is valid
        graph.request("/me")
        return True
    except facebook.GraphAPIError as e:
        print(f"An error occurred: {e}")
        return False

access_token = "YOUR_ACCESS_TOKEN"
if is_valid_access_token(access_token):
    print("Access Token is valid")
else:
    print("Access Token is invalid")