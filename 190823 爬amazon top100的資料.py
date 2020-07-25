from selenium import webdriver
import time
from lxml import etree
import requests
import pandas as pd


def select(a, b):
    # ------------[List]--------------
    DptNameList = list()
    RankList = list()
    ASINList = list()
    IndexList = list()
    LinkList = ['https://www.amazon.com/Best-Sellers/zgbs/amazon-devices/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Amazon-Launchpad/zgbs/boost/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Appstore-Android/zgbs/mobile-apps/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Arts-Crafts-Sewing/zgbs/arts-crafts/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Audible-Audiobooks/zgbs/audible/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Automotive/zgbs/automotive/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0', 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_nav_0', 'https://www.amazon.com/best-sellers-music-albums/zgbs/music/ref=zg_bs_nav_0', 'https://www.amazon.com/best-sellers-camera-photo/zgbs/photo/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Cell-Phones-Accessories/zgbs/wireless/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers/zgbs/fashion/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Collectible-Coins/zgbs/coins/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-MP3-Downloads/zgbs/dmusic/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Entertainment-Collectibles/zgbs/entertainment-collectibles/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Gift-Cards/zgbs/gift-cards/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Grocery-Gourmet-Food/zgbs/grocery/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Handmade/zgbs/handmade/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Health-Personal-Care/zgbs/hpc/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Industrial-Scientific/zgbs/industrial/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Kindle-Store/zgbs/digital-text/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Kitchen-Dining/zgbs/kitchen/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Magazines/zgbs/magazines/ref=zg_bs_nav_0', 'https://www.amazon.com/best-sellers-movies-TV-DVD-Blu-ray/zgbs/movies-tv/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Office-Products/zgbs/office-products/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Garden-Outdoor/zgbs/lawn-garden/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Prime-Pantry/zgbs/pantry/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers/zgbs/smart-home/ref=zg_bs_nav_0', 'https://www.amazon.com/best-sellers-software/zgbs/software/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Sports-Outdoors/zgbs/sporting-goods/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Sports-Collectibles/zgbs/sports-collectibles/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Home-Improvement/zgbs/hi/ref=zg_bs_nav_0', 'https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_nav_0', 'https://www.amazon.com/best-sellers-video-games/zgbs/videogames/ref=zg_bs_nav_0']
    url = LinkList[a]
    dptcode = b
    next_page_link = list()
    for i in range(2):
        if i == 1:
            url = next_page_link[0]
        else:
            pass
        browser = webdriver.Chrome('./chromedriver')
        browser.get(url)
        time.sleep(2)
        cookies = browser.get_cookies()
        session = requests.Session()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        res = session.get(url, headers=headers)
        html = etree.HTML(res.text)
        browser.quit()
        # ----------[Dept. Name]-------
        dept = html.xpath('//ul[@id="zg_browseRoot"]//span[@class="zg_selected"]/text()')
        DptNameList.append(dept[0])
        # ----------[ASIN]------------
        ASIN = html.xpath('//div[@id = "zg-right-col"]/div[@id="zg-center-div"]//span/a[@class="a-link-normal"]/@href')
        for i_asin in range(0, len(ASIN)):
            ASINList.append((ASIN[i_asin].split('/')[3]))
        # ----------[NextPage]-------
        next_page_link.append(html.xpath('//ul[@class = "a-pagination"]//li[@class="a-normal"]/a/@href')[0])
    # =========================================================================
    for num in range(1, 101):
        RankList.append(num)
        IndexList.append(num)
    df = pd.DataFrame({"DeptCode": dptcode, "Dept": DptNameList[0], "Rank": RankList, "ASIN": ASINList})
    df.index += 1
    return df


df_select = select(2, '0002')
df_select.to_csv('./top100/0002.csv')

