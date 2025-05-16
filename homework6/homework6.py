import re

text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

# Regular expression to find email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Regular expression to find text
email_addresses = re.findall(email_pattern, text)

# print email address
print(email_addresses)