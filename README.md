# Instagram-Username-Auto-Claimer
Fast and multi-threaded script to automatically claim targeted username

**This script is an educational demonstration of how to use Python, the Requests library, and threading to attempt to claim a list of usernames on Instagram**

## Disclaimer

This script is for educational purposes only. Using automated tools to interact with Instagram's API could violate their terms of service and could result in your account being suspended or permanently banned. Additionally, building an automated tool like this requires advanced programming knowledge and could potentially put your account's security at risk.

## How it Works

The script works by defining a base URL for the Instagram API and creating a function that will attempt to claim a username by sending a POST request to the API. The function takes a single argument, which is the username to be claimed.

The script also defines a list of usernames to attempt to claim and creates a loop that will spawn a new thread for each username in the list. Each thread will execute the `claim_username` function with the corresponding username as an argument.

When executed, the script will attempt to claim each username in the list concurrently using multiple threads.

## How to Use

To use this script, simply copy the code into a Python file and replace the `usernames` list with a list of usernames that you wish to attempt to claim. Then run the script in your preferred Python environment.

## Dependencies

This script requires the Requests library to be installed. You can install it using pip:

