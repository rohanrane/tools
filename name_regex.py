import re

string = "John F. Kennedy and Jane O'Connor-Smith are attending the conference."

# Define the regular expression pattern to match the first and last names
#pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)?(?:\s[A-Z]\.)?(?:\s[A-Z][a-z]+(?:[-\'][A-Z][a-z]+)?)\b'
pattern = r"\b([A-Z][a-z'-]+)\s+([A-Z][a-z'-]+)(?:\s+([A-Z])\.)?\b"

# Use the findall() function from the re module to find all matches in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches)
