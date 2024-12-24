def check_bad_weather(temperature, wind_speed, precipitation_probability, humidity):
    if temperature < -10 or temperature > 35:
        return "Плохие погодные условия"
    if wind_speed > 40:
        return "Плохие погодные условия"
    if precipitation_probability > 70:
        return "Плохие погодные условия"
    if humidity > 90:
        return "Плохие погодные условия"
    if temperature > 30 and humidity > 70:
        return "Плохие погодные условия (риск теплового удара)"
    
    return "Хорошие погодные условия"