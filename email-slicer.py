email = input("Enter your email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]

print(f"Your username is {username} and your domain is {domain}")


def email_slicer(email):
    username = email[:email.index('@')]
    domain = email[email.index('@')+1:]
    return username, domain  # tuple unpacking  

def main():
    email = input("Enter your email: ").strip()
    username, domain = email_slicer(email)
    print(f"Your username is {username} and your domain is {domain}")

if __name__ == "__main__":
    main()
