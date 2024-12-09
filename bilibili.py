# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:13:29 2022

@author: Administrator
"""
import time
import requests
import re
import bs4
import os
import webbrowser
import subprocess
def DownLoad(url):
    print("""bilibili视频下载程序""")
    print(f"下载{url}")
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
    # 伪造浏览器请求头
    res=requests.get(url,headers=headers)
    res.encoding = res.apparent_encoding
    # 自动选择合适的编码方式
    name=bs4.BeautifulSoup(res.text,'html.parser')
    text_name=name.find('title').text
    if " " in text_name:
        text_name=text_name.replace(" ","-")
    print(text_name)
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
            os.makedirs(f"{text_name}")
        except:
            pass
        with open(f"{text_name}//vudio.mp4",'wb') as fie:
            fie.write(vudio)
        with open(f"{text_name}//audio.mp3",'wb') as fie:
            fie.write(music)
        # print(os.listdir(f"{text_name}"))
        file1=f"{text_name}//vudio.mp4"
        file2=f"{text_name}//audio.mp3"
        result=f"{text_name}//output.mp4"
        print("下载中...")
        # os.system(f"ffmpeg.exe -i {file1} -i {file2} -c:v copy -c:a copy {result}")
        process = subprocess.Popen(
            [
                'ffmpeg',
                '-y',
                '-i', file1,
                '-i', file2,
                '-c:v', 'copy',
                '-c:a', 'copy',
                '-strict', 'experimental',
                '-shortest',
                result
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        if process.returncode:
            print(f"视频合成失败: {stderr}")
        else:
            print("视频合成成功")
        time.sleep(2)
url = input("请输入链接：")
DownLoad(url)












