# Using curly braces (most common)
user_profile = {
    "username": "coder123",
    "email": "coder123@example.com",
    "joined_year": 2024
}

# Using the dict() constructor
empty_dict = dict()
setup_dict = dict(brand="Ford", model="Mustang", year=1964)
# Accessing via square brackets
print(user_profile["username"])  # Output: coder123

# Safe accessing via .get()
print(user_profile.get("age"))  # Output: None
print(user_profile.get("age", 25))  # Output: 25 (fallback default)
print("\n code runs")