from selenium import webdriver
import time
import re
import os
import pandas as pd
import csv

# TODO: MODIFY THIS TO YOUR CSV FILENAME
file = pd.read_csv('test.csv')
# file= file.drop(file[file.stkcd == 'stkcd'].index)
file = file.astype(str)
href = file['href'].values.tolist()
code = file['stkcd'].values.tolist()
year = file['year'].values.tolist()

for i in range(len(href)):
    href[i] = 'http://www.cninfo.com.cn' + href[i]
    href[i] = re.sub('amp;', '', href[i])
    print(href[i])

#content = []

for i in range(len(href)):
    #content.append(href[i])
    complete = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless') # 设置option
    path = os.path.join('data', year[i], code[i])
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}  # 这边你可以修改文件储存的位置
    chrome_options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    browser.get(href[i])
    try:
        time.sleep(5)
        if(os.path.exists(path)):
            n=len(os.listdir(path))
        else:
            n=0
        browser.find_element_by_xpath('//*[@id="noticeDetail"]/div/div[1]/div[3]/div[1]/button/span').click()
        time.sleep(8)  # 这个一定要加，因为下载需要一点时间
        if (len(os.listdir(path))==n+1):
            print(str(i + 1) + '.' + href[i] + '下载完毕')
            complete.append('success')
        else:
            print(str(i + 1) + '.' + href[i] + '下载失败')
            complete.append('bug')
        browser.quit()             
    except:
        complete.append('fail')

    df = pd.DataFrame()
    df['number'] = [str(i+1)]
    df['stkcd'] = [code[i]]
    df['year'] = [year[i]]
    df['href'] = [href[i]]
    df['complete'] = complete
    df.to_csv('result.csv',mode='a',index=False,header=False)