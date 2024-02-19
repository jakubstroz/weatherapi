from requests import get
from terminaltables import AsciiTable
from json import loads
CITIES = ['Gdańsk', 'Poznań', 'Warszawa']
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop/'

    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura']
    ]
    for row in loads(response.text):
        if row['stacja'] in CITIES:
           rows.append([row['stacja'],row['godzina_pomiaru'], row['temperatura']])

    table = AsciiTable(rows)       
    print(table.table)
if __name__ == '__main__':
    main()
