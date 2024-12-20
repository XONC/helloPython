# http://www.iplant.cn/frps/prov

import xlwt
import requests
import bs4
import time

def getData(list):
    obj = {
      "name": '全部',
      "p": -1 # -1 时查询全国，否则需指定省份的p值
    }
  # for obj in list:
    print(obj)
    workbook = xlwt.Workbook('utf-8')  # 新建工作簿
    sheet1 = workbook.add_sheet(obj.get('name'))  # 新建sheet
    sheet1.write(0, 0, "科名")  # 第1行第1列数据
    sheet1.write(0, 1, "科学名")  # 第1行第2列数据
    sheet1.write(0, 2, "属名")  # 第1行第1列数据
    sheet1.write(0, 3, "属学名")  # 第1行第2列数据
    sheet1.write(0, 4, "种名")  # 第1行第1列数据
    sheet1.write(0, 5, "种学名")  # 第1行第2列数据
    sheet1.write(0, 6, "产地分布")  # 第1行第2列数据 苋科, 类林地苋属


    # 省份的id
    p = obj.get('p')
    an_hui_data = requests.get(f"http://www.iplant.cn/frps/protreeajax.aspx?ID=0") if p == -1  else requests.get(f"http://www.iplant.cn/frps/protreeajax.aspx?ID=0&p={p}")
    ace_html_data = bs4.BeautifulSoup(an_hui_data.text, 'lxml')
    i = 1
    for item in ace_html_data.select("td > .folder_close_end"):
      genus_data = requests.get(f"http://www.iplant.cn/frps/protreeajax.aspx?ID={item.attrs['id'].split('_')[1]}") if p == -1 else requests.get(f"http://www.iplant.cn/frps/protreeajax.aspx?ID={item.attrs['id'].split('_')[1]}&p={p}")
      genus_html_data = bs4.BeautifulSoup(genus_data.text, 'lxml')
      for genus_item in genus_html_data.select("td > .file_end > a"):
        id = genus_item.attrs['href'].split('id=')[1]
        # id = 2088
        kind_page_data = requests.get(f"http://www.iplant.cn/frps/proclasslist.aspx?id={id}")
        kind_page_html_data = bs4.BeautifulSoup(kind_page_data.text, 'lxml')
        page = kind_page_html_data.select(".scott a")
        page_number = 1
        if (len(page) != 0):
          # 弹出下一页
          page.pop()
          # 弹出最后的分页页码
          page_number = int(page.pop().text)
        index = 1
        while (index <= page_number):
          kind_data = requests.get(f"http://www.iplant.cn/frps/proclasslist.aspx?id={id}&page={index}")
          kind_html_data = bs4.BeautifulSoup(kind_data.text, 'lxml')
          list = kind_html_data.select("tr")
          if (len(list) > 0):
            list.pop(0)
            # 处理表格数据
            for list_item in list:
              name1 = list_item.select("tr > td:nth-child(1)")[0].text
              name2 = list_item.select("tr > td:nth-child(2)")[0].text
              name3 = list_item.select("tr > td:nth-child(3)")[0].text
              # address_data = requests.get(f"http://www.iplant.cn/info/{name2}?t=z")
              # address_html_data = bs4.BeautifulSoup(address_data.text, 'lxml')
              # print(address_html_data)

              sheet1.write(i, 0, item.text.split(' ')[1])
              sheet1.write(i, 1, item.text.split(' ')[0])
              sheet1.write(i, 2, genus_item.text.split(' ')[1])
              sheet1.write(i, 3, genus_item.text.split(' ')[0])
              sheet1.write(i, 4, name1)
              sheet1.write(i, 5, name2)
              sheet1.write(i, 6, name3)
              print(f"处理了, {item.text.split(' ')[1]}, {genus_item.text.split(' ')[1]}, {name1}")
              i += 1
          else:
            sheet1.write(i, 0, item.text.split(' ')[1])
            sheet1.write(i, 1, item.text.split(' ')[0])
            sheet1.write(i, 2, genus_item.text.split(' ')[1])
            sheet1.write(i, 3, genus_item.text.split(' ')[0])
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, '')
            sheet1.write(i, 6, '')
            print(f"处理了, {item.text.split(' ')[1]}, {genus_item.text.split(' ')[1]}, ''")
            i += 1

          index += 1
          # 每次获取种的数据之后，延迟1s，在获取别的数据
          print("暂停")
          time.sleep(1)
          print("开启")
        # 测试用断点
        break
        # 测试用断点
      break
    workbook.save(fr'{obj.get("name")}.xls')  # 保存

def getShenData():
  an_hui_data = requests.get(f"https://www.iplant.cn/frps/prohot.html")
  ace_html_data = bs4.BeautifulSoup(an_hui_data.content, 'lxml')
  list = []
  for item in ace_html_data.select("area "):
    list.append({
      'name': item.attrs['alt'],
      'p': item.attrs['href'].split('?')[1].split('=')[1]
    })
  print(list)
  return list



if __name__ == '__main__':
  pList = getShenData()
  getData(pList)
