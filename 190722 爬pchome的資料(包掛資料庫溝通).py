from selenium import webdriver
from lxml import etree
import time
import pyodbc
# -----------------[connect to SQL]-------------
conn = pyodbc.connect('Driver={SQL Server};Server=MATTHEWL-PC;Database=my db;Trusted_Connection=no;')
cursor = conn.cursor()
# ----------------[List]---------------------
IdList = list()
PriceList = list()
TitleList = list()
DetailList = list()
links = list()
ProductList = list()
# ---------------[Class]--------------------


class Product():
    def __init__(self):
        pass


# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

url = 'https://shopping.pchome.com.tw/'
browser = webdriver.Chrome('./chromedriver')
browser.get(url)
element = browser.find_element_by_xpath('//dd[@id="SearchForm"]/input[@type="text"]')
element.send_keys("電腦螢幕")
submit = browser.find_element_by_xpath('//dd[@id="SearchForm"]/input[@type="button"]').click()
time.sleep(1)
url = browser.current_url
browser.get(url)
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(1)
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(1)
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(1)
html = etree.HTML(browser.page_source)
# print(browser.page_source)
browser.quit()
# print(browser.page_source)
# ----------------[Id]
Id = html.xpath('//div[@class="Cm"]/div[@id="ItemContainer"]/dl/@id')
for i_Id in range(0, len(Id)):
    IdList.append(Id[i_Id])
# ----------------[Price]
Price = html.xpath('//div[@class="Cm"]/div[@id="ItemContainer"]/dl/dd[@class="c3f"]/ul[@class="price_box"]/li/span[@class="price"]/span/text()')
for i_Price in range(0, len(Price)):
    PriceList.append(Price[i_Price])
# ------------[Title]---------
Title = html.xpath('''
    //div[@class="Cm"]/div[@id="ItemContainer"]/dl/dd[@class="c2f"]/h5[@class="prod_name"]/a
                    ''')
for i_t in range(0, len(Title)):
    t = Title[i_t].xpath('string(.)')
    TitleList.append(t)
# ------------[Detail]----------
Detail = html.xpath('''
    //div[@class="Cm"]/div[@id="ItemContainer"]/dl/dd[@class="c2f"]/span[@class="nick"]
                    ''')
for i_Detail in range(0, len(Detail)):
    detail = Detail[i_Detail].xpath('string(.)')
    DetailList.append(detail.replace("\n", ""))

# ------[to be object]---------
for k in range(0, len(IdList)):
    objProduct = Product()
    objProduct.Id = IdList[k]
    objProduct.Price = PriceList[k]
    objProduct.Title = TitleList[k]
    objProduct.Detail = DetailList[k]
    ProductList.append(objProduct)

# ------[insert to temp table in SQL]--------
cursor.execute('''
    create table ##T (
    Id nvarchar(50) primary key,
    Title nvarchar(max) not null,
    Price nvarchar(10) not null,
    Detail nvarchar(max) not null)
     ''')

# ------[The data to insert]-----------------
ProductData = list()
for i_data in range(0, len(ProductList)):
    ProductData.append((
         ProductList[i_data].Id,
         ProductList[i_data].Title,
         ProductList[i_data].Price,
         ProductList[i_data].Detail
     ))
print(ProductData)
insert = ('''insert into ##T ([Id],[Title],[Price],[Detail])
    values (?, ?, ?, ?)''')
cursor.executemany(insert, ProductData)
cursor.execute('exec sp_pchome')
cursor.execute('drop table ##T')
cursor.commit()
cursor.close()

print(ProductData)
print(IdList)
print(PriceList)
print(TitleList)
print(DetailList)
print(ProductList)
