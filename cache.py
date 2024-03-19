"""
In computers, memory is located in different parts of the computer; 
memory on disk is far away from the CPU and takes a long time to access, but offers a large amount of storage; 
cache memory is close to the CPU, so it is faster to access, but does not offer a lot of storage space.

It is therefore wise to use the cache memory in a smart way, so that pages of memory that are more likely to be accessed are already in the cache. 
This means that there are fewer accesses to disk memory, and the memory transaction is ultimately quicker.

In this project, I have used Python to simulate a cache with two management techniques, which are explained below. 

1) First in First Out (FIFO)
In a First in First Out (FIFO) cache memory, the page that is evicted is the one that has the longest time since it was added.

2)Least Frequently Used (LFU)
In a Least Frequently Used (LFU) cache memory, the page that is evicted is the page that has had the fewest requests so far. 
In case of two pages having the same amount of requests, the lowest numbered page should be evicted. 
The number of requests that a page has had is maintained throughout the parsing of the whole set of requests, and it is not "forgotten" once a page has been removed from the cache memory.

"""
# Global variables
cache = []
requests = []

# Function for FIFO algorithm
def fifo():

    for page in requests:
        if page in cache:
            print("hit")  # Prints hit if page is already in cache memory
        else:
            print("miss")  # Prints miss if page is not in cache memory
            if len(cache) < 8:
                cache.append(page)  # This function will add new page to cache memory if cache length is less than 8
            else:
                cache.pop(0)
                '''Above function will remove the page that has longest time since added
                if cache length is greater than or equal to 8'''

                cache.append(page)
    print(cache)  # Prints the final cache memory data

# Function for LFU algorithm
def lfu():

    page_counts = {}
    actual_counts = {}
    for page in requests:
        if page in cache:
            print("hit")  # Print hit if page is already in cache memory
        else:
            print("miss")  # Print miss if page is not in cache memory
            if len(cache) < 8:
                cache.append(page)
            else:
                actual_counts = {}
                '''Below loop will generate disctionary actual_count for pages that are avilable in cache'''
                for pages, count in page_counts.items():
                    if pages in cache:
                        actual_counts[pages]=count

                '''Below line of code will get the minimum value from actual_count and store in variable min_count'''
                min_count = min(actual_counts.values())
                pages_with_min_count = []  # list for pages with minimum counts

                '''Below loop will store page numbers in disctionary pages_with_min_count which has had the fewest requests'''
                for pages, count in page_counts.items():
                    if count == min_count:
                        if pages in cache:
                            pages_with_min_count.append(pages)

                min_page = min(pages_with_min_count)  # This will get the lowest numbered page which has fewest requests

                '''Below function will remove lowest numbered page with fewest requests from cache memory'''
                cache.remove(min_page)
                cache.append(page)  # This function will add new page to cache memory

        '''Below line of code will add 1 to value of page(Key) in page_counts dictionary everytime that page occure and
        save defult value 0 for page that is not found in dictionoary then 1 is added to that page value'''
        page_counts[page] = page_counts.get(page, 0) + 1
    print(cache)  # Prints the final cache memory data

# Main function
while True:
    while True:
        ''' This will get the integer input from user and store it in veriable request.'''
        request = int(input("Enter page number (or 0 to end input): "))
        if request == 0:
            break  # If request is 0 then current while loop will be ended
        requests.append(request)  # This will append value of request variable into requests list
    print("Select eviction algorithm:")
    print("1. FIFO")
    print("2. LFU")
    print("Q. Quit")
    choice = input("Enter your choice: ").upper()  # Take the input from user and covert it into upper case
    if choice == '1':
        fifo()  # If chioce is 1 then fifo fuction will be called
        cache.clear()  # This will clear the cache memory
        requests.clear()  # This will clear the requests list
    elif choice == '2':
        lfu()  # If chioce is 2 then lfu fuction will be called
        cache.clear()
        requests.clear()
    elif choice == 'Q':
        break  # If chioce is Q then current while loop will be ended
    else:
        print("Invalid choice. Please try again.")  # If any other input is given then this will show Invalid input
