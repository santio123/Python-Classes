# get rid of duplicates

student = {
    "id1" :
    { 
        "name" : "sara",
        "age" : 13,
        "subject" : ["math","science","english"]
    },
    "id2" :
    { 
        "name" : "john",
        "age" : 14,
        "subject" : ["math","compuet science","english"]
    },
    "id3" :
    { 
        "name" : "sara",
        "age" : 13,
        "subject" : ["math","science","english"]
    },
    "id4" :
    { 
        "name" : "mathew",
        "age" : 15,
        "subject" : ["music","science","english"]
    }
}

result = {}
for key,value in student.items():
    if value not in result.values():
        result[key] =  value

print("without duplicates")
print(result)
