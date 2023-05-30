FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc9wqcS-lget4dsuGuX26-LT-pHla558_nL3Cc032N1gr9Syg/viewform?usp=sf_link"
API = 'YOUR API'
import requests

class SheetySetter:
    def __init__(self):
        self.api = API
        self.form_url = FORM_URL
    def get_current_sheet():
        response = requests.get(url=API)
        print(response.json())
    def set_params(self,ZD,AP,PPM,LP):
        params = {'sayfa1': {
            'zamanDamgasi': ZD,
            'whatIsTheAddressOfTheProperty?': AP,
            'whatIsThePricePerMonth?': PPM,
            'whatIsTheLinkToTheProperty?': LP
            }
        }
        #paramsi json= e sabitlemeyi unutma bunu farkli da yapabiliyon arastir sikilirsan.
        potst = requests.post(url=self.api, json=params)
        print(potst.text)

