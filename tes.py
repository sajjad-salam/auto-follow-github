import requests

access_token = input('Enter PERSONAL ACCESS TOKEN: ')

friend_username = input('Enter the username to extract followers from: ')

headers = {'Authorization': f'token {access_token}'}

def get_followers(username):
    followers = []
    page = 1
    while True:
        response = requests.get(
            f"https://api.github.com/users/{username}/followers?page={page}&per_page=100", headers=headers)
        if response.status_code == 200:
            data = response.json()
            if not data:
                break
            followers.extend([user['login'] for user in data])
            page += 1
        else:
            print(f"Failed to fetch followers for user {username}.")
            break
    return followers

followers = get_followers(friend_username)

if followers:
    with open('users.txt', 'w') as file:
        for user in followers:
            file.write(user + '\n')
    print(f"The list of users following {friend_username} has been saved to users.txt.")
else:
    print(f"No users found that are following {friend_username}.")
