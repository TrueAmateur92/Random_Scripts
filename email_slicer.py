
email = input("Enter your email address: ").lower()

def slice_email():
    while True:
        if "@" and "." in email:
            if " " in email:
                return "Invalid email address, please try again."
            else:
                username, address = email.split("@")
                return f"Your username is '{username}' and your domain is '{address}'."
        else:
            return "Invalid email address, please try again."

slice_email()
