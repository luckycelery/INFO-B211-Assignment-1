import datetime
import random
import string
import os

def memorable_password_gen(num_words, words_file, case = "lower"):
    #load words from file in read mode
    with open(words_file, "r") as file:
        #put words into a list
        words = [line.strip() for line in file.readlines()]
    #pick a sample of words (according ot the num_words)
    picked_words = random.sample(words, num_words)

    #Case formatting
    if case == "lower":
            #words within the picked words list are changed into lower case
            picked_words = [word.lower() for word in picked_words]
    elif case == "upper":
            #words within the picked words list are chnaged into upper case
            picked_words = [word.upper() for word in picked_words]
    elif case == "title":
            #words within the picked words list are changed to title case
            picked_words = [word.title() for word in picked_words]

    #add the digits to each of the words within the picked words list
    words_and_numbers = [word + str(random.randint(0,9)) for word in picked_words]

    #join the words witin words_and_numbers together with '-'
    memorable_password = "-".join(words_and_numbers) 

    return memorable_password

def random_password_gen(length, punctuation_allowance = True, not_allowed = None):
        #if no characters/numbers are specified as not allowed then empty list of not alloweds
        if not_allowed is None: 
            not_allowed = []
          
        #allowed characters set is created with initially just letters and numbers
        characters = string.ascii_letters + string.digits

        #checks if punctuation is allowed
        if punctuation_allowance: 
            characters += string.punctuation
        
        #remove any potentially not allowed characters from the characters by checking string and list
        characters = ''.join(char for char in characters if char not in not_allowed)

        #gen the password of specified length by selecting random figures from characters string
        random_password = ''.join(random.choice(characters) for _ in range (length))
        
        return random_password

def save_password(password, folder_name):
    # Get the directory where THIS script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the full path to the folder
    folder_path = os.path.join(base_dir, folder_name)

    # Create folder if missing
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Build full path to the file named Generated_Passwords
    file_path = os.path.join(folder_path, "Generated_Passwords.txt")

    # Timestamp each password that is saved
    timestamp = datetime.datetime.now()

    # Append to file
    with open(file_path, "a") as f:
        f.write(f"{password} — {timestamp}\n")

    
#user imput section
#checks if doing manual entry or doing testing
test_check = input("Are we making 1000 test cases? (Y/N): ").strip().upper()

if test_check == "Y":   
    #generate 1000 random passwords
    for _ in range(1000):
        # randomly choose which type to generate based off of the two types
        password_type = random.choice(["memorable", "random"])

        if password_type == "memorable":
            #randomm selections for testing if memorable password
            # choose random parameters for how many words to choose and which case
            num_words = random.randint(1, 10)
            case = random.choice(["lower", "upper", "title"])

            # dynamic path to word list
            base_dir = os.getcwd()
            words_file = os.path.join(base_dir, "top_english_nouns_lower_100000.txt")

            # generate and save reh generated password
            password = memorable_password_gen(num_words, words_file, case)
            save_password(password, "Memorable")

        else:  # random selections if random password
            length = random.randint(6, 20)
            punctuation_allowance = random.choice([True, False])

            # randomly choose characters to exclude (sometimes none) va a string of all possible characters
            all_chars = string.ascii_letters + string.digits + string.punctuation
            not_allowed = random.sample(all_chars, random.randint(0, 5))

            # generate random pass and save
            password = random_password_gen(length, punctuation_allowance, not_allowed)
            save_password(password, "Random")

else: #manual entry
    #gets rid of any spaces or capitalization discrepancies when recieving password type
    user_type = input("Please enter type of password ('memorable' or 'random'): ").strip().lower()

    #if the user chose a memorable password it asks for variable values
    if user_type == "memorable":
        case = input("Please enter the case type you'd like ('upper', 'lower', 'title'): ").strip().lower()
        num_words = int(input("Please enter how many words you would like (1-10): "))

        # connects word file using dynamic pathing
        base_dir = os.getcwd()
        words_file = os.path.join(base_dir, "top_english_nouns_lower_100000.txt")

        # runs password generator
        password = memorable_password_gen(num_words, words_file, case)
        print(password)

        # saves it to the memorable folder/dir/file
        save_password(password, "Memorable")

    elif user_type == "random": #for a random password
        length = int(input("Please enter how many characters you would like the password to be: "))
        punctuation_allowance = input("Allow punctuation? ('True'/'False'): ").strip().lower() == "true"
        not_allowed = list(input("Enter any characters not to be used (no spaces): "))

        #runs password generator
        password = random_password_gen(length, punctuation_allowance, not_allowed)
        print(password)
        #saves it to the memorable folder/dir/file
        save_password(password, "Random")
        
    else: #error message
        print("Invalid password type.")

