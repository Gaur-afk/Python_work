def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


my_outback = make_car('Mercedes-Benz', 'GLK 350', color='red',)
print(my_outback)