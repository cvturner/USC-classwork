'''
Catherine Turner
ITP125, Spring 2019
cvturner@usc.edu
Final Project
'''


# String will make it easier to make a list of all letters, digits, and punctuation
import string

# Itertools will make it easier to cycle through every possible password
import itertools

# Hashlib will help us to convert passwords to MD5 hashes
import hashlib

# Time will help us to record how long it took to crack each hash
import time


# Define function to match password to MD5 hash and record time to crack
def getHashInfo(hash, length=8):

    # Set default password in case it can't be cracked
    password = "Not found."

    # Initialize value to help break loop when password has been found
    complete = 0

    # Create string of all letters, digits, and punctuation
    # This will be used to form all combinations / all potential passwords
    chars = string.ascii_letters + string.digits + string.punctuation

    # Start timing!
    start = time.time()

    # Create every password up to a certain length
    # If the created password's hash matches the hash from the file, it's cracked --> break loop
    for x in range(1, length + 1):
        for item in itertools.product(chars, repeat=x):
            guess = ''.join(item)
            hexform = hashlib.md5(guess.encode()).hexdigest() # Translate password to MD5 hash
            if hexform == hash:
                password = guess
                complete = 1
                break
        if complete == 1:
            break

    # Stop timing after the password has been cracked
    end = time.time()
    # Calculate the time it took to crack the password
    count = end - start

    # Because we don't expect all passwords to be cracked, the final table won't be printed
    # To record results, print password and time to crack as you go
    print("Password found!")
    print("{}\t{} s".format(password, count))

    # Return the password corresponding to the hash and the time it took to crack it (in seconds)
    return password, count


# Function that converts file of password hashes into strings for program
def fileToStrings(file):

    # Create empty list
    hashesList = []

    # Try to read file
    try:
        fileIn = open(file, "r")

    # If any exception occurs, return False
    except:
        return False

    # If no exception occurs, load hashes
    else:

        # Cycle through lines in hashes file, append each line to the list
        for line in fileIn:
            newLine = line.replace("\n", "") # Make sure that new line isn't factored into string
            hashesList.append(str(newLine))

        # Return hashes list
        return hashesList


# Main executable code
def main():

    # Prompt user for file with password hashes to crack
    file = input("Hash file: ")

    # Loop until told to break
    while True:

        # If the file doesn't load correctly, prompt user for valid file
        if fileToStrings(file) == False:
            file = input("Invalid file – try again.\nHash file: ")

        # If the file loads correctly, enter information into hashes list and break loop
        else:
            hashesList = fileToStrings(file)
            break

    # For each hash in the list...
    # Run getHashInfo to create passwords until password's hash matches the desired hash
    for hash in hashesList:
        hashInfo = getHashInfo(hash)


# Execute main code
main()
