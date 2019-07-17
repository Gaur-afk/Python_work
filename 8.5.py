def describe_city(city, country="america"):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city("chicago")
describe_city("noida", "india")
describe_city("edina")