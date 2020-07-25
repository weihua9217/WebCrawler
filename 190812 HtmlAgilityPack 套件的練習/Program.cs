using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.IO;
using HtmlAgilityPack;
using System.Net.Http;


namespace _190812
{
    class Program
    {
        static void Main(string[] args)
        {
            test7();
            Console.ReadLine();
        }
        public class Product
        {
            public string Title { get; set; }
            public string Price { get; set; }
            public string Link { get; set; }
        }

        static void test1()
        {
            WebClient client = new WebClient();
            MemoryStream ms = new MemoryStream(client.DownloadData("https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%9B%BB%E8%85%A6"));
            HtmlDocument doc = new HtmlDocument();
            Console.WriteLine(doc);
            doc.Load(ms, Encoding.Default);
            HtmlDocument docStockContext = new HtmlDocument();
            docStockContext.LoadHtml(doc.DocumentNode.SelectSingleNode(
            "//div[@id = 'ItemContainer']").InnerHtml);
            HtmlNodeCollection nodeHeaders = docStockContext.DocumentNode.SelectNodes("./dl");
            foreach (HtmlNode nodeHeader in nodeHeaders)
            {
                Console.WriteLine("Header:{0}", nodeHeader.InnerText);
            }
            Console.ReadLine();
        }
        static async void test3()
        {
            var url = "https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%9B%BB%E8%85%A6";
            var httpClient = new HttpClient();
            var html = await httpClient.GetStringAsync(url);
            var htmlDocument = new HtmlDocument();
            htmlDocument.LoadHtml(html);
            var Products = new List<Product>();

        }
        static void test4()
        {
            string url = "https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%9B%BB%E8%85%A6";
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load(url);
            HtmlDocument docStockContext = new HtmlDocument();
            docStockContext.LoadHtml(doc.DocumentNode.SelectSingleNode("//div[@id='ItemContainer']").InnerHtml);
            HtmlNodeCollection nodeTitles = docStockContext.DocumentNode.SelectNodes("./dd[@class='c2f']//a");
            foreach (HtmlNode node in nodeTitles)
            {
                Console.WriteLine("Title:{0}", node.InnerText);
            }
            Console.ReadLine();
        }
        static void test5()
        {
            var html = @"https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%9B%BB%E8%85%A6";
            HtmlWeb web = new HtmlWeb();
            html = html.Replace("\r\n", "");
            var htmlDoc = web.Load(html);
            var node = htmlDoc.DocumentNode.SelectSingleNode("//head/title");
            Console.WriteLine("Node Name: " + node.Name + "\n" + node.OuterHtml);
            var node2 = htmlDoc.DocumentNode.SelectSingleNode("//div[@id = 'ItemContainer']");
            Console.WriteLine(node2.Attributes["id"].Value);
            Console.WriteLine(node2.ChildNodes.Count);
            var node3 = htmlDoc.DocumentNode.SelectSingleNode("//div[@id = 'ItemContainer']");
            Console.WriteLine(node3.Name);
        }
        static void test6()
        {
            var html = @"https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%9B%BB%E8%85%A6";
            HtmlWeb web = new HtmlWeb();
            var htmlDoc = web.Load(html);
            var nodes = htmlDoc.DocumentNode.SelectNodes("//div[@id='ItemContainer']/dl[@id ='DCAO39-A90079OL2']");
            foreach (var node in nodes)
            {
                Console.WriteLine(node.Attributes["id"].Value);
            }
        }
        static void test2()
        {
            WebClient url = new WebClient();
            MemoryStream ms = new MemoryStream(url.DownloadData("https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%9B%BB%E8%85%A6"));
            HtmlDocument doc = new HtmlDocument();
            doc.Load(ms, Encoding.Default);
            var Products = new List<Product>();
            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//dd[@class = 'c2f']/h5/a/text()");
            foreach (HtmlNode node in nodes)
            {
                Console.WriteLine("Title:{0}", node);
            }
            Console.ReadLine();
        }

        public class Stock
        {
            public string Id;
            public string Time;
            public string Price;
            public string In;
            public string Out;
            public string IoD;
            public string Amount;
            public string YesterdayEnd;
            public string TodayOpen;
            public string Maximum;
            public string Minimum;
            public string Infor;
            
        }
        static void test7()
        {
            List<int> k =new List<int>();
            k.Add(2330);
            k.Add(2317);
            k.Add(2324);
            k.Add(6182);

            for (int j =0 ; j <= 3; j++)
            {
                WebClient client = new WebClient();
                MemoryStream ms = new MemoryStream(client.DownloadData(
                "http://tw.stock.yahoo.com/q/q?s=" + (k[j])));
                HtmlDocument doc = new HtmlDocument();
                doc.Load(ms, Encoding.Default);
                HtmlDocument docStockContext = new HtmlDocument();
                docStockContext.LoadHtml(doc.DocumentNode.SelectSingleNode(
                "/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);
                HtmlNodeCollection nodeHeaders =
                docStockContext.DocumentNode.SelectNodes("./tr[1]/th");
                string[] values = docStockContext.DocumentNode.SelectSingleNode(
                "./tr[2]").InnerText.Trim().Split('\n');
                int i = 0;
                foreach (HtmlNode nodeHeader in nodeHeaders)
                {
                    Console.WriteLine("Header: {0}, Value: {1}",
                    nodeHeader.InnerText, values[i].Trim());
                    i++;
                }
                Console.WriteLine("============");
                doc = null;
                docStockContext = null;
                client = null;
                ms.Close();
            }
                Console.WriteLine("Completed.");
                Console.ReadLine();
            
        }
    }
}

