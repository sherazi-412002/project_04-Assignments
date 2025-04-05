
from hashlib import sha256

def login(email,stored_logins,passward_to_check):

    if stored_logins.get(email) == hash_passward(passward_to_check):
        return True
    return False


def hash_passward(passward):

    return sha256(passward.encode()).hexdigest()


def main():
    stored_logins = {
        "abcexample@gmail.com": "486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    print(login("abcexample@gmail.com",stored_logins,"world"))
    print(login("abcexample@gmail.com",stored_logins,"hello"))


if __name__ == "__main__":
    main()