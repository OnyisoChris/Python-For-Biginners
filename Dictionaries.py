monthConversions = {
    "Jan": "January",  #Here, Jan is the key and January is the value and the keys have to be unique.
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October"
    #11: "November",
    #12: "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("May"))
print(monthConversions.get("lua", "Not a valid key"))