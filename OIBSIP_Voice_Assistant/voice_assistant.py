# Simple Voice Assistant (Text Based)
# Oasis Infobyte Internship Project

import datetime
import webbrowser

print("----------- SIMPLE VOICE ASSISTANT -----------\n")

name = input("Hello! What is your name? : ").strip()
if name == "":
    name = "User"

print(f"\nHi {name}! I am your assistant.")
print("You can ask me:")
print("- time")
print("- date")
print("- open google")
print("- open youtube")
print("- search <your text>")
print("- exit\n")


def get_command():
    """Reads a command from the user."""
    return input("Your command: ").lower().strip()


while True:
    command = get_command()

    # if user just presses enter
    if command == "":
        print("Please say something.\n")
        continue

    # tell time
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time is:", current_time)

    # tell date
    elif "date" in command:
        today = datetime.date.today().strftime("%d %B %Y")
        print("Today's date is:", today)

    # open google
    elif "open google" in command:
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    # open youtube
    elif "open youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    # google search
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query == "":
            query = input("What do you want to search? : ").strip()
        if query:
            print(f"Searching '{query}' on Google...")
            url = "https://www.google.com/search?q=" + query
            webbrowser.open(url)
        else:
            print("Nothing to search.\n")

    # exit
    elif "exit" in command or "quit" in command or "bye" in command:
        print(f"Goodbye {name}! Have a great day :)")
        break

    # unknown command
    else:
        print("Sorry, I did not understand that.\n")
