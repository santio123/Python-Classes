# get the country code

country = {
    "India" : "0091",
    "pakistan" : "0092",
    "quatar" : "0974",
    "USA" : "001"
}

print("the country code for India is ",country.get("India","not found"))
print("the country code for Australia is ",country.get("Australia","not found"))
