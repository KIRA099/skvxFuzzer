# Simple HTTP Fuzzer Tool

This is a basic Python tool to perform fuzzing on a target web server.  
It sends HTTP GET requests to a given URL with words from a user-provided wordlist,  
waiting a specified time between each request.

---

## Features

- Sends HTTP GET requests to URLs constructed by appending words from a wordlist.
- Prints out words that respond with status code 200 (OK).
- Allows setting a delay between requests to avoid overwhelming the server.

---

## Requirements

- Python 3.x  
- `requests` library (`pip install requests`)

---

## Usage

Run the script and provide the following inputs when prompted:

```bash
python fuzzer.py
