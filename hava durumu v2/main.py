from tkinter import *
from PIL import ImageTk, Image
import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = 'b8fcd0b81794134cec45381e26d9a192'
iconUrl = 'https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q': city, 'appid': api_key, 'lang': 'tr'}
    data = requests.get(url, params=params).json()
    print(data)
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city, country, temp, icon, condition)

def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        # Add city and country to the listbox
        cityListbox.insert(END, '{},{}'.format(weather[0], weather[1]))

        locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]), stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon

app = Tk()
app.geometry('300x450')
app.title( 'KK Hava Durumu')

cityEntry = Entry(app, justify='center')
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
cityEntry.focus()

searchButton = Button(app, text='Arama', font=('Arial', 15), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app, font=('Arial', 40))
locationLabel.pack()

tempLabel = Label(app, font=('Arial', 50, 'bold'))
tempLabel.pack()

conditionLabel = Label(app, font=('Arial', 20))
conditionLabel.pack()

# Add a Listbox to show the searched cities
cityListbox = Listbox(app)
cityListbox.pack(fill=BOTH, expand=True)

app.mainloop()