"""from requests import get    #request라이브러리에서 get 함수를 불러옴
from bs4 import BeautifulSoup       #bs4 라이브러리 불러옴

base_url = "https://weworkremotely.com/remote-jobs/search?term="      
search_term = "python"

response = get(f"{base_url},{search_term}")
if response.status_code != 200:
    print("'Can't reach website")
else:
    soup = BeautifulSoup(response.text,"html.parser")   #html 파싱 => 파이썬 객체 변환
    print(soup.find_all('section',class_ = "jobs"))     #soup모듈로 class가 "jobs"인 section을 찾음
"""
def say_hello(name,age):
    print(f"Hello {name} you are {age} years old")
    
say_hello("nico", 12)       #순서대로 인수 지정
say_hello(name = "nico", age = 12)      #인수 순서지정 => 순서 상관 X