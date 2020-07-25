import requests
from lxml import etree
import pyodbc
# -----------------[connect to SQL]-------------
conn = pyodbc.connect('Driver={SQL Server};Server=MATTHEWL-PC;Database=my db;Trusted_Connection=no;')
cursor = conn.cursor()
# -----------------[lists]-----------------------
IdList = list()
AuthorList = list()
TitleList = list()
DatesList = list()
RecommendsList = list()
ContentList = list()

ArticleList = list()
remove_dates = list()


class Article():
    def __init__(self):
        pass


links = ['https://www.ptt.cc/bbs/movie/index.html']
# 用來翻頁的for，range(2)代表會包含此頁和它的前一頁
for i in range(2):
    link = links[i]
    res = requests.get(link)
    html = etree.HTML(res.text)
# ------[Id]-------------
    Id = html.xpath('//div[@class ="r-ent"]/div[@class = "title"]/a/@href')
    for i_Id in range(0, len(Id)):
        IdList.append(Id[i_Id])
# ------[Author]-------------
    Author = html.xpath('//div[@class ="r-ent"]/div[@class = "meta"]/div[@class = "author"]/text()')
    for i_Author in range(0, len(Author)):
        if Author[i_Author] != '-':
            AuthorList.append(Author[i_Author])
        else:
            remove_dates.append(i_Author)
# ------[Title]-------------
    Title = html.xpath('//div[@class ="r-ent"]/div[@class = "title"]/a/text()')
    for i_Title in range(0, len(Title)):
        TitleList.append(Title[i_Title])
# ------[Dates]-------------
    Dates = html.xpath('//div[@class ="r-ent"]/div[@class = "meta"]/div[@class = "date"]/text()')
    for i_Dates in range(0, len(Dates)):
        DatesList.append(Dates[i_Dates])
# ------[Recommends]-------------
    Id = html.xpath('//div[@class ="r-ent"]/div[@class = "title"]/a/@href')
    for i_re in range(0, len(Id)):
        Recommends = html.xpath(
            '//a[@href="' + str(Id[i_re]) + '"]/ancestor::div[@class="r-ent"]/div[@class="nrec"]/span/text()')
        if len(Recommends) == 0:
            RecommendsList.append("nan")
        else:
            RecommendsList.append(Recommends[0])
# ------[content]-------------
    links_for_content = list()
    # 我的list
    link_for_content = html.xpath('//div[@class ="r-ent"]/div[@class = "title"]/a/@href')
    # 把連結抓到我的list裡
    for i_content in range(0, len(link_for_content)):
        links_for_content.append(link_for_content[i_content])
    # 用來爬進去每一篇文章，將內容取出
    for j_content in range(0, len(links_for_content)):
        link = 'https://www.ptt.cc' + str(links_for_content[j_content])
        res = requests.get(link)
        html_for_content = etree.HTML(res.text)
        Content = html_for_content.xpath('''normalize-space(
                        //div[@id="main-container"]/div[@id="main-content" and @class= "bbs-screen bbs-content"]/text()
                        )''')
        ContentList.append(Content)
    # ------[pre-page_link]-------------
    pre_page_link = html.xpath('//div[@class="btn-group btn-group-paging"]/a[position()=2]/@href')
    for i_pre_page_link in range(0, len(pre_page_link)):
        A_link = 'https://www.ptt.cc' + str(pre_page_link[i_pre_page_link])
        links.append(A_link)

if len(remove_dates) != 0:
    for i_remove_dates in range(0, len(remove_dates)):
        del DatesList[int(remove_dates[i_remove_dates])]


print(len(IdList))
print(len(AuthorList))
print(len(DatesList))
print(len(RecommendsList))
print(len(ContentList))

ArticleList = list()

# ------[to be object]---------
for k in range(0, len(IdList)):
    objArticle = Article()
    objArticle.Id = IdList[k]
    objArticle.Author = AuthorList[k]
    objArticle.Title = TitleList[k]
    objArticle.Dates = DatesList[k]
    objArticle.Recommends = RecommendsList[k]
    objArticle.Content = ContentList[k]
    ArticleList.append(objArticle)

# ------[insert to temp table in SQL]--------
cursor.execute('''
    create table ##T (
    Id nvarchar(50) primary key,
    Author nvarchar(50) not null,
    Title nvarchar(50) not null,
    Dates nvarchar(50) not null,
    Recommends nvarchar(10) not null,
    Content nvarchar(max) not null)
     ''')
# ------[The data to insert]-----------------
ArticleData = list()
for i_data in range(0, len(ArticleList)):
    ArticleData.append((
         ArticleList[i_data].Id,
         ArticleList[i_data].Author,
         ArticleList[i_data].Title,
         ArticleList[i_data].Dates,
         ArticleList[i_data].Recommends,
         ArticleList[i_data].Content,
     ))

print(ArticleData)

insert = ('''insert into ##T ([Id],[Author],[Title],[Dates],[Recommends],[Content])
    values (?, ?, ?, ?, ?, ?)''')
cursor.executemany(insert, ArticleData)
cursor.execute('exec sp_ptt_crawler')
cursor.execute('drop table ##T')
cursor.commit()
cursor.close()





