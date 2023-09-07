import requests
import bs4
import time
import urllib.request
import os
def download_svg(title,title_index, first, last, index):
    try:
        print(f"{title}第{index}页下载中。。")
        urllib.request.urlretrieve(f"https:{first}/{index}.{last}",f"./{title_index}/{title + '_' + str(index)}.{last}")
        print(f"{title}第{index}页下载完成")
        download_svg(title,title_index, first, last, int(index)+1)
    except:
        print(f"{title}下载完成")
        pass
#获取item 的soup
def deal_str(href, title, title_index):
    # res = requests.get("https://www.tukuppt.com/muban/lypaxkwy.html")
    res = requests.get(f"https://www.tukuppt.com{href}")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    print(f"获取{title}的soup")
    src_dom = soup.select(".middle.wlimit img")[0]
    src = src_dom.attrs['src']
    # 对加密的链接跳过
    if '!' in src:
        return
    else:
        pass
    src_split = src.split("/")
    first_half = '/'.join(src_split[:-1])
    last_half = src_split[-1].split('.')[-1]
    i = src_split[-1].split('.')[0]
    dir_path = f"./{title_index}"
    if os.path.exists(dir_path):
        pass
        download_svg(title, title_index, first_half, last_half, i)
    else:
        os.mkdir(dir_path)
        download_svg(title, title_index, first_half, last_half, i)
# 获取主站
def get_soup(i):

    res = requests.get(f"https://www.tukuppt.com/wordmuban/tiyujiaoan/__zonghe_0_0_0_0_0_0_{i}.html")

    return bs4.BeautifulSoup(res.text, 'lxml')

if __name__ == '__main__':
    for i in range(50):
        soup = get_soup(i)
        print("获取主站soup")
        item_list_dom = soup.select("dt.p-title > a")
        index = 0
        for item in item_list_dom:
            href = item.attrs['href']
            title_index = item.string[0:10] + str(index)
            title = item.string
            deal_str(href, title, title_index)
            index += 1
