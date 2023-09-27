#Africa Game

print('----------------------Africa Game----------------------\n\n\n\n')
import time
score=0
countries = ["Algeria", "Angola", "Benin", 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic of the Congo', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome & Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe' ]
print('---Countries of Africa---\n\n')
print(f'Score={score}')

while len(countries) >0:
    print(f'Number of countries to guess:{len(countries)}\nScore={score}\n\n')
    country=input('Enter in the name of an African country you have not named already.\n')
    if country in countries:
        time.sleep(.5)
        print('Good Guess\n')
        time.sleep(.5)
        score +=1
        time.sleep(.5)
        countries.remove(country)
    else:
        print('Invalid Guess\n')
        time.sleep(2)
Print('\nWell Done! You have Completed the Game!')



