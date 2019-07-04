info1 = {'country':"America", 'Fact':"Very crowded."}
info2 = {'country':"America", 'Fact':"Calm and relaxing."}
info3 = {'country':"America", 'Fact':"Open and natural."}
cities = {'Vienna':info1, 'Ashburn':info2, 'Edina':info3}

for city, info in cities.items():
    print ("Info about " + city + " is " + str(info))