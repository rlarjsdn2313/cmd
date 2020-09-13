from bs4 import BeautifulSoup
import requests

#url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=서울날씨'
#hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
#req = requests.get(url, headers=hdr)
#html = req.text
#soup = BeautifulSoup(html, 'html.parser')

#현재 온도 긁기
def nowtemp(cmd):
    if cmd == 'nowtemp':
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=서울날씨'
        hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        NowTemp1 = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class' : 'tempmark'}).text[2:]
        NowTemp = 'Now tmep: ' + NowTemp1
        return NowTemp
    elif cmd[:10] == 'nowtemp -l':
        location = cmd[11:]
        inallocation = location + '날씨'
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + str(inallocation)
        hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        NowTemp1 = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class' : 'tempmark'}).text[2:]
        NowTemp = str(inallocation) + ': ' + NowTemp1
        return NowTemp
    elif cmd[:10] == 'nowtemp -h':
        result = 'nowtemp command is getting temp data\nnowtemp is getting data of 서울\nnowtemp -l [location] is getting data of [location]'

def finedust(cmd):
    if cmd == 'finedust':
        #여러가지 변수들...
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=서울날씨'
        hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        CheckDust = []
        #긁어오기
        fine_dust1 = soup.find('div', {'class': 'sub_info'})
        fine_dust = fine_dust1.find('div', {'class': 'detail_box'})
        for i in fine_dust.select('dd'):
            CheckDust.append(i.text)
        Fine_Dust = CheckDust[0][:-2] + " " + CheckDust[0][-2:]
        Ultra_Fine_Dust = CheckDust[1][:-2] + " " + CheckDust[1][-2:]
        #정리
        NowTemp = '서울fine_dust: ' + str(Fine_Dust) + "\n" + '서울Ultra_Fine_Dust: ' + str(Ultra_Fine_Dust)
        return NowTemp
    elif cmd[:11] == 'finedust -l':
        location = cmd[11:]
        inallocation = location + '날씨'
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + str(inallocation)
        hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        CheckDust = []
        fine_dust1 = soup.find('div', {'class': 'sub_info'})
        fine_dust = fine_dust1.find('div', {'class': 'detail_box'})
        for i in fine_dust.select('dd'):
            CheckDust.append(i.text)
        Fine_Dust = CheckDust[0][:-2] + " " + CheckDust[0][-2:]
        Ultra_Fine_Dust = CheckDust[1][:-2] + " " + CheckDust[1][-2:]
        #정리
        NowTemp = str(location) + "\n" +' fine_dust: ' + str(Fine_Dust) + "\n" +  ' Ultra_Fine_Dust: ' + str(Ultra_Fine_Dust)
        return NowTemp
