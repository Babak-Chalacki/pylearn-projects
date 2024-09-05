import instaloader
import getpass

username = input("Enter your Instagram username: ")
password = getpass.getpass("Enter your Instagram password: ")
target_username = input("Enter the target username: ")

L = instaloader.Instaloader()
L.login(username, password)

profile = instaloader.Profile.from_username(L.context, target_username)

current_followers = set(follower.username for follower in profile.get_followers())
previous_followers = set()

try:
    with open(f"{target_username}_followers.txt", "r") as file:
        previous_followers = set(file.read().splitlines())
except FileNotFoundError:
    pass

new_followers = current_followers - previous_followers

if new_followers:
    print("New Followers:")
    for follower in new_followers:
        print(follower)
else:
    print("No new followers.")

with open(f"{target_username}_followers.txt", "w") as file:
    for follower in current_followers:
        file.write(f"{follower}\n")