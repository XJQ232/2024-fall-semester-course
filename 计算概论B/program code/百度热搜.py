import requests
from bs4 import BeautifulSoup

# 百度热搜榜 URL
BAIDU_HOT_SEARCH_URL = "https://top.baidu.com/board?tab=realtime"

# 获取百度热搜榜数据
def get_baidu_hot_search():
    # 发送 HTTP 请求获取页面内容
    response = requests.get(BAIDU_HOT_SEARCH_URL)
    
    # 检查是否请求成功
    if response.status_code != 200:
        print("无法访问百度热搜榜")
        return None
    
    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到热搜榜的部分
    hot_search_items = soup.find_all('div', class_='c-single-text-ellipsis')  # 热搜标题部分
    
    # 如果找不到内容，返回
    if not hot_search_items:
        print("未找到热搜榜内容")
        return None
    
    # 获取热搜榜标题并打印
    hot_search_list = []
    for idx, item in enumerate(hot_search_items, 1):
        title = item.get_text(strip=True)
        hot_search_list.append(f"{idx}. {title}")
    
    return hot_search_list

# 展示热搜榜
def display_hot_search(hot_search_list):
    if hot_search_list:
        print("百度热搜榜：")
        for item in hot_search_list:
            print(item)
    else:
        print("没有热搜榜数据可展示。")

# 主函数
if __name__ == "__main__":
    hot_search_list = get_baidu_hot_search()
    display_hot_search(hot_search_list)

