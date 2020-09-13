import requests

def get_nmt_translate(context):
    try:
        url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": 'i1KogGqQDvap63jqFQVk', "X-Naver-Client-Secret":'SW3s4JUvSW'}
        params = {"source": "en", "target": "ko", "text": context}
        response = requests.post(url, headers=headers, data=params)
        res = response.json()
        return res['message']['result']['translatedText']
    except:
        return "번역 실패"
            

#print(get_nmt_translate('안녕'))