"""
Given the dictionary below:

artist = {
    "first": "Neil",
    "last": "Young",
}
Declare a variable called full_name  that is equal to artist's first  and last  names 
with a space between. You must reference the values associated 
with those keys in the artist dictionary.

print(full_name)
# Neil Young
"""

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = (artist["first"] + " " + artist["last"])

print(full_name)