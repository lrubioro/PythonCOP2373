# Lory Rubio Programming Assignment 1
# This program is intended to sell a total of 20 cinema tickets for a pre-sell, in which each buyer can only buy up to 4 tickets at a time.
# The program will prompt the user for the desired number of tickets and then display the number of remaining tickets after their purchase.
# This will all be repeated until all tickets have been sold. Then it will display the total number of buyers.

# defining constant values
MAX_TICKETS = 20
MAX_TICKETS_PER_BUYER = 4

# Creating the first function that will deal with ticket sales, prompting user for input and updating quantity of tickets remaining.
def sell_tickets():

    # Beginning the variables inorder to track remaining tickets and the total buyers
    tickets_remaining = MAX_TICKETS
    buyers_total = 0

    # Creating a while loop because we want to keep asking the user for input regarding the purchase of tickets while there some still available
    while tickets_remaining > 0:
        tickets_wanted = int(input('Please enter the number of tickets you would like to purchase (max amount 4 tickets per buyer):'))

    # If statement used to check if the number of requested tickets is no more than tickets remaining in inventory
        if 1 <= tickets_wanted <= MAX_TICKETS_PER_BUYER and tickets_wanted <= tickets_remaining:
            # Updating the values of remaining tickets and buyers
            tickets_remaining -= tickets_wanted
            buyers_total += 1
            print('Tickets remaining:',tickets_remaining)

        else:
            # Tell the user their request is invalid
            print('Your request cannot be processed since the number you have entered has reach the max amount of tickets that you can purchase, or that are remaining.')

    #ensure that the number ofr total buyers is returned
    return buyers_total


# Creating the second function that will display the results of the ticket sale, in terms of buyers.
def display_results (buyers_total):
    print('All tickets have been sold. The total of buyers were:',buyers_total)

#Call back main functions
buyers_total=sell_tickets()
display_results(buyers_total)
