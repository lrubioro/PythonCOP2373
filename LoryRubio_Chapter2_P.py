# Lory Rubio Programming Assignment 2
# This program will ask the user to enter an email message.
# Then the application will scan the message for each of the 30 keywords or phrases that are commonly found in spam mail.
# For each occurrence of one of these within the message, a point will be added to the message's "spam score".
# Next, the likelihood that the message is spam will be rated, based on the number of points received.

#define the scan for words function
def scan_for_words (email,spam_words):

#initialize the score accumulator and words found list
    score = 0
    words_found = []

    #create a loop that will scan for possible spam words and also considers case sensative
    for word in spam_words:

        #creating a method where even lower case words are considered
        if word in email.lower():
            score += 1
            words_found.append(word)

    return score,words_found

#define the function that will rate the spamability of the email
def rate_email (score):

#begin by creating if statements and setting conditions for the different prompts
    if score == 0:
        return "This email is not spam"

    #if found words are less than 15
    elif score <=15:
        return "Maybe spam"

    else:
        return "This email is very likely to be spam"

#now the main function that will set the list of spam words and call back the other functions
def main():
    spam_words = [
        "best price",
        "billion",
        "cash bonus",
        "additional income",
        "free info",
        "free investment",
        "free trial",
        "full refund",
        "get paid",
        "lower rates",
        "lowest price",
        "make money",
        "one time",
        "prize",
        "promise",
        "pure profit",
        "urgent",
        "instant",
        "limited time",
        "warranty",
        "winner",
        "cures",
        "no catch",
        "no cost",
        "no fees",
        "obligation",
        "passwords",
        "cash",
        "certified",
        "deal",
    ]

    # call the other functions
    user_email = input("Enter your email:").strip()
    score, words_found = scan_for_words(user_email,spam_words)
    spam_rating = rate_email(score)

    #print the results to the user
    print ("Spam score for the email was:",score)
    print ("The likelihood of spam in the email is:",spam_rating)

    # create if statement if words were found
    if words_found:
        print("Words that cause spam score are:", words_found)

# call back main
main()