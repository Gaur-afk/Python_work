def describe_city(city, country="america"):
    msg = city.title() + ", " + country.title() + "."
    print(msg)

describe_city("chicago", "america")
describe_city("noida", "india")
describe_city("edina", "america")
