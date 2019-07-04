favorite_languages = {
    'Jen': 'python',
    'Sarah': 'c',
    'Edward': 'ruby',
    'Phil': 'python',
    }
people = ["Sarah", "Phil", "Bob", "Katie"]
for person in people:
    if person in favorite_languages:
        print ("Thank you for taking the poll " + person + "!")
    else:
        print (person + ", please take this poll.")