from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"        #기본 url 지정
    request = requests.get(url, headers={"User-Agent": "Kimchi"})       #user-agent 추가해야지 정상적 작동
    results = []        #결과를 받을 빈 리스트 생성
    if request.status_code == 200:      #정상 응답이면
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")    #tr태그중 "job"인 클래스 찾음
        for job in jobs:
            company = job.find("h3", itemprop="name")       #company <= "h3"태그 중 itemprop이 name
            position = job.find("h2", itemprop="title")     #position <= "h2"태그 중 itemprop이 title
            location = job.find("div", class_="location")   #location <= "div"태그 중 class가 location
            if company:
                company = company.string.strip()    #company는 문자열전환 & 공백삭제
            if position:
                position = position.string.strip()
            if location:
                location = location.string.strip()
            if company and position and location:
                job = {         #딕셔너리 형태로 job에 저장 
                    'company': company,
                    'position': position,
                    'location': location
                }
                results.append(job)     #리스트에 딕셔너리 형태로 만든 job 저장
    else:
        print("Can't get jobs.")
    return results      #반환


print(extract_jobs("rust"))     #함수호출 & 결과값 출력

