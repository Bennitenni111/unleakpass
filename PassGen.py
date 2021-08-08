import random
import string
import sys, time, threading
import time
import os
import requests
from bs4 import BeautifulSoup


def rand_pass_generator():
    pswdlen = 15
    letters = string.ascii_letters
    while True:
        generated_pass = ''.join(random.choice(letters) for i in range(pswdlen))
        if is_pass_safe(generated_pass):
            break
    print("We've found you secure password (unused) and non-leaked")
    print("safe Password : ",generated_pass)

#checking from the website
def is_pass_safe(password):
    safe_msg = 'Good news — no pwnage found!'
    is_safe = False
    #issue in sending post request in this website
    response = requests.post('https://haveibeenpwned.com/Passwords',data={'Password':password})
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    pwd_title = soup.find('div',class_='pwnTitle')
    print(f"password: {password}\n{pwd_title.h2.text}")
    if(pwd_title.h2.text == safe_msg):
        is_safe = True
    else:
        is_safe = False
        print(f"{pwd_title.h3.text}")
    return is_safe

def loading_screen():
    print("Loading:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

#Testing method
if __name__ == '__main__':
    password = input('Type password to check is it safe? \nOr just press enter to generate:')
    if password:
        if not is_pass_safe(password):
            rand_pass_generator()
    else:
        rand_pass_generator()

    