basic.show_number(weatherbit.temperature())

def on_forever():
    weatherbit.start_weather_monitoring()
basic.forever(on_forever)
