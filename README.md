# INFO-B211-Assignment-1
## a) Purpose of the Program

This program is designed to generate pseudo-random passwords in one of two formats:

- **Memorable passwords**, created by combining randomly selected words (from a dedicated word‑list file, up to a user‑specified number) with appended digits and optional casing rules.
- **Random passwords**, created by selecting random characters from user‑specified character sets (letters, digits, optional punctuation) while excluding any characters the user designates as not allowed.

The program supports both interactive password creation and automated generation of 1000 test cases.

---

## b) Input

This program accepts the following inputs:

- Selection of **“1000 Test Cases”** or **“Manual Entry”**
- Selection of **Memorable** or **Random** password type (Manual Entry)
- **Path to a TXT file** containing 100,000 nouns (Memorable)
- **Number of words** to include (Memorable)
- **Case format** for the words (Memorable)
- **Length** of the password (Random)
- **Punctuation allowance** (True/False) (Random)
- **Characters to exclude** from the password (Random)

---

## c) Expected Output

- **Manual Entry:**  
  The program outputs the generated password to the terminal and appends it and a timestamp to the appropriate `Generated_Passwords.txt` file inside either the **Memorable** or **Random** directory.

- **1000 Test Cases:**  
  The program automatically generates 1000 passwords, randomly selecting the password type and its parameters. Each generated password is appended to the correct `Generated_Passwords.txt` file within the **Memorable** or **Random** directory, each entry accompanied by a timestamp.
