def FIFO():
    """
    Simulates cache memory management with FIFO eviction policy.
    """
    cache = []
    requests = []

    # Collecting user input for requests
    while 0 not in requests:
        page_input = input(
            "What page would you like? Please type pages as integers and end your requests by typing [0], "
            "to end the program use command [Q]: "
        )
        
        # Validate user input as able to convert into integers
        if page_input.isdigit(): 
            requests.append(int(page_input))
        elif page_input == "Q":
                exit()  # Exiting the program
        else:
            print("This is not a valid input.")

    # Removing the terminating 0 from the requests
    requests.remove(0)

    # Displaying the requested pages and initial cache state
    print("Requested pages are the following:", requests)
    print("Starting cache is", cache)

    # Processing each request
    for request in requests:
        if request in cache:
            print("hit")
        else:
            print("miss")
            if len(cache) < 8:
                cache.append(request) # There is still room in cache memory
            else: # There is no more room in cache memory
                cache.pop(0)  # Remove the first page (FIFO)
                cache.append(request)

    print("Current cache state:", cache) # Printing final state of cache

    # Emptying the lists for the next iteration of the function
    cache.clear() 
    requests.clear()

# Call the function to run the simulation
while True:
    FIFO()

