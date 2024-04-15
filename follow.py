import requests
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
BB = '\x1b[2;36m'
Y = '\x1b[1;34m'
all = '_._._._._.'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
Bl = '\x1b[1;34m'
P = '\x1b[1;35m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
E = '\x1b[0;90m'
print(('\033[92m—'*25)+'\n• DEV BY @S_J_O_D •\n'+('—'*25))
print(f'''{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-

    𓆩‹ 𝐾𝐼𝑁𝐺 𝑂𝐹 𝐸𝑁𝐺𓆪

                              ███████╗  █████╗       ██╗      ██╗  █████╗  ██████╗  
                              ██╔════╝ ██╔══██╗      ██║      ██║ ██╔══██╗ ██╔══██╗ 
                              ███████╗ ███████║      ██║      ██║ ███████║ ██║  ██║ 
                              ╚════██║ ██╔══██║ ██   ██║ ██   ██║ ██╔══██║ ██║  ██║ 
                              ███████║ ██║  ██║ ╚█████╔╝ ╚█████╔╝ ██║  ██║ ██████╔╝ 
                              ╚══════╝ ╚═╝  ╚═╝  ╚════╝   ╚════╝  ╚═╝  ╚═╝ ╚═════╝  
                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ 
                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D 
                            DEV-INFO : https://t.me/KING_OF_ENG  』
                            
                            
{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-
  {Y}[{P}*{Y}]{C}Code By :{W} 𓆩𝑬𝑵𝑮-𝑺𝑨𝑱𝑱𝑨𝑫𓆪
  {Y}[{P}*{Y}]{C}DEV-INFO : {W}@KING_OF_ENG
{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-''')
dead = (C+"""▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬~𓆩𝑬𝑵𝑮-𝑺𝑨𝑱𝑱𝑨𝑫𓆪~▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬""")
print(dead)
# Your personal access token
access_token = input(
    '  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m [+] Entre PERSONAL ACCESS TOKEN : )  \x1b[1;38;5;121m ๛   \x1b[38;5;117m')


# Set the authorization header
headers = {'Authorization': f'token {access_token}'}

# Function to follow a user


def follow_user(username):
    response = requests.put(
        f"https://api.github.com/user/following/{username}", headers=headers)
    if response.status_code == 204:
        print(f"Successfully followed {username}.")
    else:
        print(f"Failed to follow {username}.")


# Read the list of usernames from the text file
usernames_file = 'users.txt'
with open(usernames_file, 'r') as file:
    usernames = [line.strip() for line in file if line.strip()]

# Follow each user and report their departments
for username in usernames:
    follow_user(username)
    print(f"Following {username}.")
