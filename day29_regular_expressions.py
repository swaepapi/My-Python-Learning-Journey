# A regular expression (regex) is a sequence of characters that form a search pattern. You can use this pattern to match, search, and manipulate text.

# Importing the module 
import re

# Using re.match()

pattern = r'^Hello'
text = "Hello, world!"

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("No match.")


# Using re.search()

pattern = r'world'
text = "Hello, world!"

search = re.search(pattern, text)
if search:
    print(f"Match found: {search.group()}")
else:
    print("No match.")


# Using re.findall()

pattern = r'\d+'  # Matches one or more digits
text = "I have 3 apples and 10 bananas."

matches = re.findall(pattern, text)
print(f"Matches: {matches}")

# Using re.sub()

pattern = r'\d+'
text = "I have 3 apples and 10 bananas."

new_text = re.sub(pattern, 'X', text)
print(new_text)



# Example code 

import re

# Sample text containing an email address
text = """
Hello, my name is Fidel Barasa. You can contact me at fidelbarasa@gmail.com or through my other email at example@test.com.
"""

# Regular expression pattern for matching email addresses
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Find all email addresses in the text
emails = re.findall(email_pattern, text)

# Output the extracted emails
if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email addresses found.")
