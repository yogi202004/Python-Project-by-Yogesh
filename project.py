import random
import string
from operator import length_hint

#predefined list of adjectives and nouns
adjectives = ["Cool","Happy","Brave","Swift","Clever","Mighty","Silly","Fierce"]
nouns = ["Tiger","Dragon","Eagle","Lion","Shark","Wolf","Falcon","Panther"]

def generate_username(include_numbers=True, include_special_chars=True, length=12):
    #combine a random adjective and noun
    username = random.choice(adjectives) + random.choice(nouns)

    #Add random numbers if selected
    if include_numbers:
        username += str(random.randint(0 , 999))

    #Add special characters if selected
    if include_special_chars:
        username += random.choice(['!','@','#','$','%'])

    #Trim or extend username to the desired length
    if len(username) > length:
        username = username[:length]
    else:
        while len(username) < length:
            username += random.choice(string.ascii_letters + string.digits)

    return username
def save_username_to_file(username, filename="usernames.txt"):
    try:
        with open(filename, "a") as file:
            file.write(username + "\n")
        print(f"username '{username}' saved to {filename}")
    except Exception as e :
        print("Error saving username:", e)

def main():
    print("Welcome to the Random Username Generator!")

    # User customization options
    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() =='yes'
        length = int(input("Preferred username length (minimum 8); "))
        if length < 8:
            print("Length too short, setting to 8.")
            length = 8
    except ValueError:
        print("Invalid input. Using default settings.")
        num_usernames = 5
        include_numbers = True
        include_special_chars = True
        length = 12

    # Generate and save usernames
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars, length)
        print("Generated Username:", username)
        save_username_to_file(username)

    print("Username generation complete!")

if __name__ == "__main__":
    main()




