class Thermostat:
    def __init__(self):
        self.__temperature = 20
        self.__min_temp = 10    # In Celsius
        self.__max_temp = 30    # In Celsius

    def set_temperature(self, temp_celsius):
        if self.__is_valid_temp:
            self.__temperature = temp_celsius
        else:
            print("ERROR: Can only set temperature between 10°C and 30°C")

    def get_temperature_celsius(self):
        return self.__temperature

    def get_temperature_fahrenheit(self):
        return self.__celsius_to_fahrenheit(self.__temperature)

    def increase_temp(self):
        if self.__temperature < self.__max_temp:
            self.__temperature += 1
        
    def decrease_temp(self):
        if self.__temperature > self.__min_temp:
            self.__temperature -= 1

    def __celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    def __is_valid_temp(self, temp):
        if self.__min_temp <= temp <= self.__max_temp:
            return True
        else:
            return False

thermostat = Thermostat()
print(thermostat.get_temperature_celsius())  # 20
print(thermostat.get_temperature_fahrenheit())  # 68

print(thermostat.set_temperature(19))
# print(thermostat.get_temperature_fahrenheit())  # 77

# thermostat.set_temperature(50)  # Error: out of range
# print(thermostat.get_temperature_celsius())  # Still 25

# thermostat.increase_temp()
# print(thermostat.get_temperature_celsius())  # 26