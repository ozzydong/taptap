import requests
import pandas as pd
from time import sleep

# 使用Session保持连接，提升效率
session = requests.Session()
lst = []

# 统一配置参数
cookies = {
    'acw_tc': '2760820617495586116875508ea1ec1116652aec008593192241f4735ebefa',
    'web_app_uuid': 'b55fb62c-d477-4472-a9c1-95a3e4bb81cf',
    'Hm_lvt_536e39e029b26af67aecbc444cdbd996': '1749558613',
    'HMACCOUNT': 'E331DCB5BCDFA382',
    'XSRF-TOKEN': 'dwfz3hnniafe4ihdicye',
    'apk_download_url_postfix': '/organic-direct_index',
    '_ga': 'GA1.1.1722777370.1749558613',
    '_clck': 'fufnyw%7C2%7Cfwn%7C0%7C1987',
    '_clsk': 'o5m007%7C1749559345646%7C1%7C0%7Ce.clarity.ms%2Fcollect',
    'Hm_lpvt_536e39e029b26af67aecbc444cdbd996': '1749559361',
    '_ga_6G9NWP07QM': 'GS2.1.s1749558613$o1$g1$t1749559361$j40$l0$h0',
    'ssxmod_itna': 'YqfxyQKQq7qiqY5PYQiQiqx4YLUx0DYK07DzxC5iOhDu6xjKidqDUAiTjaFOerAcBqDCQ07vw1DBL4hbDnqD82DQeDv3Puh0NM77BqxIaFIDbpwt/me4qcZQjlwwxoaLU+wnLOQ7yODHxi8DBI4ZahrDeWaDCeDQxirDD4DADibq4D1EDDkD0+m7UovW4GWDmbADYHGj78fDGa3bRAfTDDCiPBYjWg5DGy54d5qoRifDiWGfIRYOfDRaWhmD75dDlPxHVhmy+69sD3RidZEo2YDXhtDv2gj7t4=a38vvFRDtme/p0cD4a4xF+4fGiGi88Db3Dr7i7bT4hGif0D7G4i0hByt0YD84wChdt0ipY1ju1h8i2LeVkGohhc2pCE+TeQQGYiYwl05Dh+iD4Zrqj2xYGDZODZq44D',
    'ssxmod_itna2': 'YqfxyQKQq7qiqY5PYQiQiqx4YLUx0DYK07DzxC5iOhDu6xjKidqDUAiTjaFOerAcBqDCQ07vwbD8fnvbQ1/jOu3MSxgveK3GDOinXseD',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://www.taptap.cn/top/download/strategy',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'acw_tc=2760820617495586116875508ea1ec1116652aec008593192241f4735ebefa; web_app_uuid=b55fb62c-d477-4472-a9c1-95a3e4bb81cf; Hm_lvt_536e39e029b26af67aecbc444cdbd996=1749558613; HMACCOUNT=E331DCB5BCDFA382; XSRF-TOKEN=dwfz3hnniafe4ihdicye; apk_download_url_postfix=/organic-direct_index; _ga=GA1.1.1722777370.1749558613; _clck=fufnyw%7C2%7Cfwn%7C0%7C1987; _clsk=o5m007%7C1749559345646%7C1%7C0%7Ce.clarity.ms%2Fcollect; Hm_lpvt_536e39e029b26af67aecbc444cdbd996=1749559361; _ga_6G9NWP07QM=GS2.1.s1749558613$o1$g1$t1749559361$j40$l0$h0; ssxmod_itna=YqfxyQKQq7qiqY5PYQiQiqx4YLUx0DYK07DzxC5iOhDu6xjKidqDUAiTjaFOerAcBqDCQ07vw1DBL4hbDnqD82DQeDv3Puh0NM77BqxIaFIDbpwt/me4qcZQjlwwxoaLU+wnLOQ7yODHxi8DBI4ZahrDeWaDCeDQxirDD4DADibq4D1EDDkD0+m7UovW4GWDmbADYHGj78fDGa3bRAfTDDCiPBYjWg5DGy54d5qoRifDiWGfIRYOfDRaWhmD75dDlPxHVhmy+69sD3RidZEo2YDXhtDv2gj7t4=a38vvFRDtme/p0cD4a4xF+4fGiGi88Db3Dr7i7bT4hGif0D7G4i0hByt0YD84wChdt0ipY1ju1h8i2LeVkGohhc2pCE+TeQQGYiYwl05Dh+iD4Zrqj2xYGDZODZq44D; ssxmod_itna2=YqfxyQKQq7qiqY5PYQiQiqx4YLUx0DYK07DzxC5iOhDu6xjKidqDUAiTjaFOerAcBqDCQ07vwbD8fnvbQ1/jOu3MSxgveK3GDOinXseD',
}

# 配置请求参数模板
params_template = {
    'limit': '10',
    'platform': 'android',
    'type_name': 'strategy',
    'X-UA': 'V=1&PN=WebApp&LANG=zh_CN&VN_CODE=102&LOC=CN&PLT=PC&DS=Android&UID=b55fb62c-d477-4472-a9c1-95a3e4bb81cf&OS=Windows&OSV=10&DT=PC',
}

# 设置请求重试机制
retries = 3  # 设置最大重试次数

for page in range(1,6):  # 更直观的页码显示（1-6页）
    for attempt in range(retries):
        try:
            # 配置动态参数
            params = {
                **params_template,
                'from': (page-1)*10  # 自动计算起始位置
            }
            
            response = session.get(
                'https://www.taptap.cn/webapiv2/app-top/v2/hits',
                params=params,
                cookies=cookies,
                headers=headers,
                timeout=10  # 添加超时设置
            )
            
            # 增加请求间隔防止被封
            sleep(0.5)
            
            data = response.json()
            if data['data']['list']:
                for index, item in enumerate(data['data']['list'], start=1):
                    app_info = item.get("app", {})
                    stat_info = app_info.get("stat", {})
                    rating_info = stat_info.get("rating", {})
                    
                    id_ = app_info.get("id")
                    
                    # id_ = 717836

                    params1 = {
                        'X-UA': 'V=1&PN=WebApp&LANG=zh_CN&VN_CODE=102&LOC=CN&PLT=PC&DS=Android&UID=b55fb62c-d477-4472-a9c1-95a3e4bb81cf&OS=Windows&OSV=10&DT=PC',
                        'id': str(id_),
                    }
                    
                    response1 = requests.get('https://www.taptap.cn/webapiv2/app/v6/detail', params=params1, cookies=cookies, headers=headers)
                            
                    sj1 = response1.json()['data']['app']
                    
                    
                    publisher = sj1.get("developers")[0].get("name")
                    
                    try:
                        author = sj1.get("developers")[1].get("name")
                    except:
                        author = ''
                        
                    
                    # 使用字典推导式创建数据记录
                    record = {
                        'app_name': app_info.get("title"),
                        'tag': '·'.join([t.get("value") for t in app_info.get("tags", [])]),
                        'rec_text': app_info.get("rec_text"),
                        'rating': rating_info.get("score"),
                        'publisher': publisher,
                        'author': author
                    }
                    lst.append(record)
                # 
                print(f'✅ 成功获取第 {page} 页数据，共 {len(data["data"]["list"])} 条')
                break  # 成功则跳出重试循环
                
        except Exception as e:
            if attempt < retries - 1:
                print(f'⚠️ 第 {page} 页请求失败，正在重试...（{attempt+1}/{retries}）')
                sleep(2)
                continue
            else:
                print(f'❌ 第 {page} 页请求失败，已达到最大重试次数')
                break

# 创建DataFrame并添加自增序号
df = pd.DataFrame(lst)
df.insert(0, '序号', range(1, len(df)+1))  # 在首列插入从1开始的序号

# 保存数据
try:
    df.to_excel('tag_action.xlsx', index=None)
    print(f'🎉 数据已保存成功，共 {len(df)} 条记录')
except Exception as e:
    print(f'❌ 文件保存失败：{str(e)}')