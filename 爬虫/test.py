# requests 网络请求库
# lxml
#bs4
import requests
import bs4
import time
import PyPDF2
import pdfkit

def get_soup(suffex):
    res = requests.get(f"https://www.liaoxuefeng.com{suffex}")
    return bs4.BeautifulSoup(res.text, 'lxml')

def reduce_nav(parentNav, divDom, depth):
    div_list = divDom.select(f'div[depth="{depth+1}"]')
    a = divDom.select('a')
    href = a[0].attrs['href']
    parentNav['list'].append({"name": a[0].string, "href": href, "context": get_context(href), "list": []})
    print(f"完成{a[0].string}的加载...等待5秒")
    time.sleep(5)
    print("-----等待结束，开始下一轮-----")
    if len(div_list):
        for div in div_list:
            reduce_nav(parentNav['list'][-1], div, depth+1)
    else:
       pass

def get_context(href):
    return get_soup(href).select(".x-wiki-content.x-main-content")[0]

def main():
    wiki_nav = {"list": []}
    # wiki_div = get_soup("/wiki/1022910821149312/1023020745357888").select("#x-wiki-index > div")
    # reduce_nav(wiki_nav, wiki_div[0], 0)
    print(wiki_nav)

    pdfkit.from_string('<p>aaa<p>', "test.pdf")
    # with open("test.pdf", mode='w') as pdf_file:
    #     pdf_write = PyPDF2.PdfWriter(pdf_file)
    #     pdf_write.
    #     print(pdf_write)



if __name__ == '__main__':
    main()


