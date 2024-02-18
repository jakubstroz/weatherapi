import sys
import requests

def get_data():
    data = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/?format=json')
    return data.json()
def main():
    response = get_data()
    codes = [rate['code'] for rate in response[0]['rates']]

    while True:
        a = int(input("""
        1    SPRAWDZ KURS WSZYSTKICH WALUT
        2    SPRAWDZ KURS DANEJ WALUTY
                      
        4    SPRZEDAJ WALUTĘ
                      
        0    WYJSCIE
: """))
        if a == 1:
            for rate in response[0]['rates']:
                print(rate['code'], rate['mid'], rate['currency'])
                print()
        if a == 2:
            print(', '.join(codes),'\n')
            code = input('podaj kod waluty którą chcesz wyświetlić \n : ')
            code = code.upper()
            if code in codes:
                print("\n",' '.join(rate['code'] + str(rate['mid']) + rate['currency'] for rate in response[0]['rates'] if rate['code'] == code))
            else:
                raise ValueError('błędny kod waluty')
        if a == 4:
            print(', '.join(codes),'\n')
            code = input('podaj kod waluty którą chcesz sprzedać \n : ')
            code = code.upper()
            if code in codes:
                value = int(input(f'Ile {code} chcesz sprzedać? \n: '))
                if value <= 0:
                    raise ValueError('musisz mieć więcej niż 0')
                else:
                    for rates in response[0]['rates']:
                        if rates['code'] == code:
                            saldo = value * rates['mid']
                            print('\n', f'za {value} : {code} otrzymasz {saldo} PLN')
                            return f"wedlug kursu z dnia {response[0]['effectiveDate']} NBP"
                            
            else:
                raise ValueError('błędny kod waluty')

        if a == 0:
            sys.exit(0)
if __name__ == '__main__':
    print(main())