from requests import get #request라이브러리에서 get 함수를 불러옴

websites = (
    "google.com",
    "https://airbnb.com",
    "facebook.com"
)       

for website in websites:     
    if not website.startswith("https://"):      
        website = f"https://{website}"      
    response = get(website) #get(using requests) take response
    print(response)     #print the result
