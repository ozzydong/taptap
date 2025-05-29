import requests
import pandas as pd
from time import sleep

# 使用Session保持连接，提升效率
session = requests.Session()
lst = []

# 统一配置参数
cookies = {
    'web_app_uuid': 'ac71f55e-6952-49b3-96fc-619f8d976505',
    'Hm_lvt_536e39e029b26af67aecbc444cdbd996': '1748261706',
    'HMACCOUNT': '8B7740D650E5D4E7',
    'XSRF-TOKEN': '0l1o86c0q4gviztti3bi',
    '_ga': 'GA1.1.648877972.1748261706',
    'apk_download_url_postfix': '/organic-direct_ranking',
    '_clck': '1azrm2y%7C2%7Cfw8%7C0%7C1972',
    'acw_tc': '2760820917482679710101017ef69b6e2bff504a50d1e6723328df00aeb1aa',
    'Hm_lpvt_536e39e029b26af67aecbc444cdbd996': '1748268007',
    '_clsk': 'v5sczg%7C1748268007931%7C5%7C0%7Cb.clarity.ms%2Fcollect',
    '_ga_6G9NWP07QM': 'GS2.1.s1748267974$o2$g1$t1748268008$j0$l0$h0',
    'ssxmod_itna': 'Yq+xB7eDqqnDyD4wDRgEDwO8WG=dDXDUqAQD2DIqGQGcD8OD0PGOAaxoz8QKSQ7SQG4Piq8GqDseDWqYDSxD=HDK4GTGC6TxUtHFbA+RxNAiDHwK3iSr1vOdrbI4bcfoGF6vxPxxB3DExGkuj5x1D4DxaPD5xDTDWeDGDD3DmWGDi5oD0KDjegp8UgmDYPDED3DRZ53p+3D7rbmdI8eDD5WVhx3WfDDB2Gq1G75A4DrVp3o7GgQKqFmD753DlcbWLim9FZc3lE2tqIEY6YDXatDv6EjH+rQWK3vIFWqYOeYk=GxGD5xuCDPbuQS0rnyb8i5SDPQ0bRyqW7Onv4Y+O9bPxxD84skCd=GiG0CEk1G3iUqeMTs3xhnhpkOKNA537o/GQBAiSG5/ixxg=5OoqhG0CoMODgw44D',
    'ssxmod_itna2': 'Yq+xB7eDqqnDyD4wDRgEDwO8WG=dDXDUqAQD2DIqGQGcD8OD0PGOAaxoz8QKSQ7SQG4Piq8D4iTGWD8OTvQOb7Dt1llEYBQDcCQ3np4D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://www.taptap.cn/top/download/action',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'web_app_uuid=ac71f55e-6952-49b3-96fc-619f8d976505; Hm_lvt_536e39e029b26af67aecbc444cdbd996=1748261706; HMACCOUNT=8B7740D650E5D4E7; XSRF-TOKEN=0l1o86c0q4gviztti3bi; _ga=GA1.1.648877972.1748261706; apk_download_url_postfix=/organic-direct_ranking; _clck=1azrm2y%7C2%7Cfw8%7C0%7C1972; acw_tc=2760820917482679710101017ef69b6e2bff504a50d1e6723328df00aeb1aa; Hm_lpvt_536e39e029b26af67aecbc444cdbd996=1748268007; _clsk=v5sczg%7C1748268007931%7C5%7C0%7Cb.clarity.ms%2Fcollect; _ga_6G9NWP07QM=GS2.1.s1748267974$o2$g1$t1748268008$j0$l0$h0; ssxmod_itna=Yq+xB7eDqqnDyD4wDRgEDwO8WG=dDXDUqAQD2DIqGQGcD8OD0PGOAaxoz8QKSQ7SQG4Piq8GqDseDWqYDSxD=HDK4GTGC6TxUtHFbA+RxNAiDHwK3iSr1vOdrbI4bcfoGF6vxPxxB3DExGkuj5x1D4DxaPD5xDTDWeDGDD3DmWGDi5oD0KDjegp8UgmDYPDED3DRZ53p+3D7rbmdI8eDD5WVhx3WfDDB2Gq1G75A4DrVp3o7GgQKqFmD753DlcbWLim9FZc3lE2tqIEY6YDXatDv6EjH+rQWK3vIFWqYOeYk=GxGD5xuCDPbuQS0rnyb8i5SDPQ0bRyqW7Onv4Y+O9bPxxD84skCd=GiG0CEk1G3iUqeMTs3xhnhpkOKNA537o/GQBAiSG5/ixxg=5OoqhG0CoMODgw44D; ssxmod_itna2=Yq+xB7eDqqnDyD4wDRgEDwO8WG=dDXDUqAQD2DIqGQGcD8OD0PGOAaxoz8QKSQ7SQG4Piq8D4iTGWD8OTvQOb7Dt1llEYBQDcCQ3np4D',
}

# 配置请求参数模板
params_template = {
    'limit': '10',
    'platform': 'android',
    'type_name': 'action',
    'X-UA': 'V=1&PN=WebApp&LANG=zh_CN&VN_CODE=102&LOC=CN&PLT=PC&DS=Android&UID=ac71f55e-6952-49b3-96fc-619f8d976505&OS=Windows&OSV=10&DT=PC',
}

# 设置请求重试机制
retries = 3  # 设置最大重试次数

for page in range(1, 7):  # 更直观的页码显示（1-6页）
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
                    
                    # 使用字典推导式创建数据记录
                    record = {
                        'app_name': app_info.get("title"),
                        'tag': '·'.join([t.get("value") for t in app_info.get("tags", [])]),
                        'rec_text': app_info.get("rec_text"),
                        'rating': rating_info.get("score")
                    }
                    lst.append(record)
                
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