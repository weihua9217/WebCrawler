from selenium import webdriver
import time
from lxml import etree
import requests
import pyodbc
# -----------------[connect to SQL]-------------
conn = pyodbc.connect('Driver={SQL Server};Server=MATTHEWL-PC;Database=my db;Trusted_Connection=no;')
cursor = conn.cursor()
# ------------[List]--------------
ASINList = list()
TitleList = list()
StarList = list()
PriceList = list()
InformationList = list()
InformationList2 = list()


# ------------[class]--------------
class Product():
    def __init__(self):
        pass
# ---------------------------------


links = ['https://www.amazon.com/ref=nav_logo']
for i in range(1):
    link = links[i]
    url = link
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    element = browser.find_element_by_xpath('//div[@id="nav-search"]//div[@class="nav-fill"]/div/input[@type="text"]')
    if i == 0:
        element.send_keys("Computer")
    time.sleep(2)
    submit = browser.find_element_by_xpath('//div[@id="nav-search"]//div[@class="nav-right"]/div/input').click()
    time.sleep(2)
    url = browser.current_url
    browser.get(url)
    cookies = browser.get_cookies()
    browser.delete_all_cookies()
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    res = session.get(url, headers=headers)
    html = etree.HTML(res.text)
    print(res.text)
    browser.quit()
    # ------------[ASIN]---------------
    ASIN = html.xpath('//div[@class="s-result-list s-search-results sg-row"]/div/@data-asin')
    for i_ASIN in range(0, len(ASIN)):
        if ASIN[i_ASIN] == '':
            pass
        else:
            ASINList.append(ASIN[i_ASIN])
    # ------------[Title]--------------
    Title = html.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
    for i_Title in range(0, len(Title)):
        TitleList.append(Title[i_Title])
    # ------------[Star]---------------
    Star = html.xpath('//div[@class="sg-col-inner"]//div[@class="s-result-list s-search-results sg-row"]//span[@class="a-icon-alt"]/text()')
    for i_Star in range(0, len(Star)):
        StarList.append(Star[i_Star])
    # ------------[Price]--------------
    Price = html.xpath('//div[@class="sg-col-inner"]//div[@class="s-result-list s-search-results sg-row"]//span[@data-a-size="l"]/span[@class="a-offscreen"]/text()')
    for i_Price in range(0, len(Price)):
        PriceList.append(Price[i_Price])
    # ------------[Information]--------
    links_for_information = list()
    link_for_information = html.xpath('//a[@class="a-link-normal a-text-normal"]/@href')
    print(len(link_for_information))
    for i_link in range(0, len(link_for_information)):
        links_for_information.append(link_for_information[i_link])
    for j_link in range(0, len(links_for_information)):
        url = 'https://www.amazon.com'+str(links_for_information[j_link])
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        res = session.get(url, headers=headers)
        html_for_information = etree.HTML(res.text)
        information = html_for_information.xpath('''
                                //ul[@class="a-unordered-list a-vertical a-spacing-none"]//li[@id="replacementPartsFitmentBullet"]/following-sibling::li/span[@class="a-list-item"]/text()
                                ''')
        informationList = list()
        for i_information in range(0, len(information)):
            information[i_information] = information[i_information].replace("\t", "")
            information[i_information] = information[i_information].replace("\n", "")
            informationList.append(information[i_information])
        InformationList.append(informationList)
        InformationList2.append('//'.join(informationList))
    # --------------[next-page_link]------------
    next_page_link = html.xpath('//li[@class="a-last"]/a/@href')
    for i_pre_page_link in range(0, len(next_page_link)):
        link = 'https://www.amazon.com'+str(next_page_link[i_pre_page_link])
        links.append(link)

print(len(ASINList))
print(len(TitleList))
print(len(StarList))
print(len(PriceList))
print(len(InformationList))
print(len(InformationList2))
# for i in range(0, len(InformationList)):
#     print(InformationList[i])
# print('===========================')
# print('===========================')
# for i in range(0, len(InformationList2)):
#     print(InformationList2[i])

ProductList = list()

# -------[to be object]--------------
for i in range(0, len(ASINList)):
    objProduct = Product()
    objProduct.ASIN = ASINList[i]
    objProduct.Title = TitleList[i]
    objProduct.Star = StarList[i]
    objProduct.Price = PriceList[i]
    objProduct.Information = InformationList2[i]
    ProductList.append(objProduct)

# ----------[create temp table]---------
cursor.execute('''
    create table ##T(
    ASIN varchar(20) primary key,
    Title nvarchar(max) not null,
    Star nvarchar(100) not null,
    Price nvarchar(50) not null,
    Information nvarchar(max) not null
    )
''')
# ----------[the data]-------------------
ProductData = list()
for i_data in range(0, len(ProductList)):
    ProductData.append((
        ProductList[i_data].ASIN,
        ProductList[i_data].Title,
        ProductList[i_data].Star,
        ProductList[i_data].Price,
        ProductList[i_data].Information
    ))

print(ProductData)

insert = ('''
    insert into ##T ([ASIN],[Title],[Star],[Price],[Information]) values(?, ?, ?, ?, ?)
''')
cursor.executemany(insert, ProductData)
cursor.execute('exec sp_amazon')
cursor.execute('drop table ##T')
cursor.commit()
cursor.close()









