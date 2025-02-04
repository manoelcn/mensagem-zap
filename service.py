import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CallMeBot:

    def __init__(self):
        self.__base_url='https://api.callmebot.com/whatsapp.php'
        self.__phone=os.getenv('PHONE')
        self.__api_key=os.getenv('API_KEY')

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__phone}&text={message}&apikey={self.__api_key}'
        )
        return response.text
