import instaloader
import getpass
f = open("followers.txt","r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()
L = instaloader.Instaloader()
username = input("enter username: ")
password = getpass.getpass("enter password: ")
L.login(username,"password")
print("vasle")

profile = instaloader.Profile.from_username(L.context,"babak_chalakii")

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)
    
f = open("followers.txt","w")
for follower in new_followers:
    f.write(follower + "\n")
f.close     