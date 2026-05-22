import requests
 
class User:
    def __init__(self, n, d):
        self.name = n
        self.date_creation = d

    @classmethod
    def create_user(cls, n, d):
        user = User(n, d)
        return user
    
    def view_profile(self):
        print(f"===Your Account Info=== \nName: {self.name} \nAccount created on: {self.date_creation}")

    def get_weather(self):
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
        parameters = {
            "lat": "35.5",
            "lon": "78.5",
            "units":"imperial",
            "lang":"en"
        } 
        headers = {
            "x-rapidapi-host":"weatherbit-v1-mashape.p.rapidapi.com",
            "x-rapidapi-key": "057c5416f3msh2600e30d4834de3p15e909jsn41d7c28e7f6b"
        }

        response = requests.get(url, headers = headers, params= parameters)
        if response.status_code == 200:
            data = response.json()
            city = data["city_name"]
            country = data['country_code']
            temperature = data["data"][1]["app_temp"]
            print(f'This is the weather: \nCity = {city} \nCountry Code = {country}\nTemperature = {temperature}')
        else:
            print(f"Error {response.status_code}")


    def convert_currency(self):
        url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            while True:
                try:
                    eur_amount = int(input("Enter the amount in EUR: "))
                    xof_amount = eur_amount * data["eur"]["xof"]
                    return f"It is equal to {round(xof_amount, 2)} CFA Francs"
                except ValueError:
                    print("Invalid Input!")
        else:
            return f"Error {response.status_code}"



