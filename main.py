from weather import get_weather


print("=" * 40)
print("      WEATHER API APPLICATION")
print("=" * 40)

city = input("\nEnter City Name: ")

weather = get_weather(city)

if weather:

    print("\nWeather Report")
    print("-" * 40)

    print(f"City         : {weather['city']}")
    print(f"Country      : {weather['country']}")
    print(f"Condition    : {weather['condition']}")
    print(f"Temperature  : {weather['temperature']} °C")
    print(f"Feels Like   : {weather['feels_like']} °C")
    print(f"Humidity     : {weather['humidity']} %")
    print(f"Pressure     : {weather['pressure']} hPa")
    print(f"Wind Speed   : {weather['wind']} m/s")
    print(f"Visibility   : {weather['visibility']} m")
    print(f"Sunrise      : {weather['sunrise']}")
    print(f"Sunset       : {weather['sunset']}")

else:

    print("\nCity Not Found!")
