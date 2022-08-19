# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:13:29 2022

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys 
import time
import requests
import re
import bs4
import os
import webbrowser
import ffmpeg
# from urllib.request import urlretrieve
web=Chrome()
web.get("https://www.bilibili.com/")
web.find_element_by_xpath('//*[@id="nav-searchform"]/div[1]/input').send_keys("f450无人机",Keys.ENTER)
"""搜索框输入"""
time.sleep(5)
web.switch_to.window(web.window_handles[-1])
# print(web.page_source)
for i in range(3,4):
    button=web.find_element_by_xpath(f'//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button[{i}]')
    button.click()
    time.sleep(3)
    if i==2:
        lis=web.find_elements_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]')
    else:
        lis=web.find_elements_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[1]/div')
    for li in lis:
        text=li.find_element_by_xpath('./div/div[2]/div/div/a/h3').text
        url=li.find_element_by_xpath('./div/div[2]/div/div/a')
        urllink=url.get_attribute('href')
        print(text)
        # print(urllink)
        url=urllink
        res=requests.get(url)
        # print(res.text)
        obj=re.compile('"codecid":7},{"id":32,"baseUrl":"(?P<info>.*?)","base_url":".*?',re.S)
        page=obj.finditer(res.text)
        for li in page:
            vudiourl=li.group("info")
            # print(li.group("info"))
        musobj=re.compile('{"id":30280,"baseUrl":"(?P<mus>.*?)","base_url":.*?')    
        muspage=musobj.finditer(res.text)
        for li in muspage:
            audiourl=li.group("mus")
            # print(audiourl)
        head={
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
              "Referer":url,
              }
        vudiores=requests.get(vudiourl,headers=head)
        audiores=requests.get(audiourl,headers=head)
        # print(vudiores)
        # print(audiores)
        vudio=vudiores.content
        music=audiores.content
        try:
            os.makedirs(f"./{text}")
        except:
            pass
        with open(f"{text}//video.mp4",'wb') as fie:
            fie.write(vudio)
        with open(f"{text}//audio.mp3",'wb') as fie:
            fie.write(music)
        file1=f"{text}//video.mp4"
        file2=f"{text}//audio.mp3"
        result=f"{text}//output.mp4"
        print("下载中...")
        os.system(f"E:\\ffmpeg-4.4.1-full_build\\ffmpeg-4.4.1-full_build\\bin\\ffmpeg.exe -i {file1} -i {file2} -c:v copy -c:a copy -bsf:a aac_adtstoasc {result}")
        time.sleep(7)
        print("下载完成...")


# web=Chrome()
# web.get("https://www.bilibili.com/")
# web.find_element_by_xpath('//*[@id="nav-searchform"]/div[1]/input').send_keys("穿越机",Keys.ENTER)
# """搜索框输入"""
# time.sleep(5)
# web.switch_to.window(web.window_handles[-1])
# # print(web.page_source)
# for i in range(2,3):
#     button=web.find_element_by_xpath(f'//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button[{i}]')
#     button.click()
#     time.sleep(3)
#     if i==2:
#         lis=web.find_elements_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]')
#     # else:
#     #     lis=web.find_elements_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[1]/div')
#     for li in lis:
#         text=li.find_element_by_xpath('./div/div[2]/div/div/a/h3').text
#         url=li.find_element_by_xpath('./div/div[2]/div/div/a')
#         urllink=url.get_attribute('href')
#         print(text)
#         # print(urllink)
#         url=urllink
#         res=requests.get(url)
#         # print(res.text)
#         playinfos=bs4.BeautifulSoup(res.text,'html.parser')
#         playinfo=playinfos.select('script')
#         obj=re.compile('<script>window.__playinfo__=(?P<info>.*?)</script>')
#         print(playinfo[3])
#         # obj=re.compile('"codecid":7},{"id":32,"baseUrl":"(?P<info>.*?)","base_url":".*?',re.S)
#         # page=obj.finditer(res.text)
#         # for li in page:
#         #     vudiourl=li.group("info")
#         #     # print(li.group("info"))
            
            
        
#         # musobj=re.compile('{"id":30280,"baseUrl":"(?P<mus>.*?)","base_url":.*?')    
#         # muspage=musobj.finditer(res.text)
#         # for li in muspage:
#         #     audiourl=li.group("mus")
#             # print(audiourl)
#         # head={
#         #       "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
#         #       "Referer":url,
#         #       }
#         # vudiores=requests.get(vudiourl,headers=head)
        
        
        
        
        
        
# #         audiores=requests.get(audiourl,headers=head)
# #         # print(vudiores)
# #         # print(audiores)
# #         vudio=vudiores.content
# #         music=audiores.content
# #         try:
# #             os.makedirs(f"./{text}")
# #         except:
# #             pass
# #         with open(f"{text}//video.mp4",'wb') as fie:
# #             fie.write(vudio)
# #         with open(f"{text}//audio.mp3",'wb') as fie:
# #             fie.write(music)
# #         file1=f"{text}//video.mp4"
# #         file2=f"{text}//audio.mp3"
# #         result=f"{text}//output.mp4"
# #         print("下载中...")
# #         os.system(f"E:\\ffmpeg-4.4.1-full_build\\ffmpeg-4.4.1-full_build\\bin\\ffmpeg.exe -i {file1} -i {file2} -c:v copy -c:a copy -bsf:a aac_adtstoasc {result}")
# #         time.sleep(7)
# #         print("下载完成...")













