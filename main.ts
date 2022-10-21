basic.showNumber(weatherbit.temperature())
basic.forever(function on_forever() {
    weatherbit.startWeatherMonitoring()
})
