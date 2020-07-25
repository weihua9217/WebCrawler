using System;
using System.Collections.Generic;
using System.Text;
using System.Net;
using System.IO;
using HtmlAgilityPack;
using System.Data.SqlClient;
using Dapper;

namespace _190813
{
    public class Stock
    {
        public string Id { get; set; }
        public int Time { get; set; }
        public decimal Price { get; set; }
        public int Amount { get; set; }
        public decimal Maximum { get; set; }
        public decimal Minimum { get; set; }
        public Stock(string _Id, int _Time, decimal _Price, int _Amount, decimal _Maximum, decimal _Minimum)
        {
            Id = _Id;
            Time = _Time;
            Price = _Price;
            Amount = _Amount;
            Maximum = _Maximum;
            Minimum = _Minimum;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {

            AddSql();
            Console.WriteLine("Finish");

        }
        public static List<object> scrap()
        {
            List<object> stocks = new List<object>();
            int[] Id = { 2330, 2317, 2324, 6182 };
            List<string> Name = new List<string>();
            List<int> Time = new List<int>();
            List<decimal> Price = new List<decimal>();
            List<int> Amount = new List<int>();
            List<decimal> Maximum = new List<decimal>();
            List<decimal> Minimum = new List<decimal>();


            for (int j = 0; j <= 3; j++)
            {
                WebClient client = new WebClient();
                MemoryStream ms = new MemoryStream(client.DownloadData(
                "http://tw.stock.yahoo.com/q/q?s=" + (Id[j])));
                HtmlDocument doc = new HtmlDocument();
                doc.Load(ms, Encoding.Default);
                HtmlDocument docStockContext = new HtmlDocument();
                docStockContext.LoadHtml(doc.DocumentNode.SelectSingleNode(
                        "/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);
                HtmlNodeCollection nodeHeaders =
                docStockContext.DocumentNode.SelectNodes("./tr[1]/th");
                string[] values = docStockContext.DocumentNode.SelectSingleNode(
                "./tr[2]").InnerText.Trim().Split('\n');
                //num = { 0, 1, 2, 6, 9, 10 };
                string name = values[0].Trim().Replace("加到投資組合", "");
                Name.Add(name);
                int time = Convert.ToInt32(values[1].Trim().Replace(":", ""));
                Time.Add(time);
                decimal price = Convert.ToDecimal(values[2].Trim());
                Price.Add(price);
                int amount = Convert.ToInt32(values[6].Trim().Replace(",", ""));
                Amount.Add(amount);
                decimal maximum = Convert.ToDecimal(values[9].Trim());
                Maximum.Add(maximum);
                decimal minimum = Convert.ToDecimal(values[10].Trim());
                Minimum.Add(minimum);
            }
            for (int i = 0; i < Id.Length; i++)
            {
                Stock stock = new Stock(Name[i], Time[i], Price[i], Amount[i], Maximum[i], Minimum[i]);
                stocks.Add(stock);
            }
            return stocks;
        }
        public static void AddSql()
        {
            using (var conn = new SqlConnection("Server=MATTHEWL-PC;Trusted_Connection=true"))
            {
                var stocks = scrap();

                var sql =
                    @"create table #T(
                        Id varchar(20) not null,
                        Time int,
                        Price decimal,
                        Amount int,
                        Maximum decimal(20),
                        Minimum decimal(20)
                        );
                        insert into #T ([Id],[Time],[Price],[Amount],[Maximum],[Minimum])
                        values(@Id,@Time,@Price,@Amount,@Maximum,@Minimum);
                        exec [my db].[dbo].[sp_stock190813];";
                var executwResult = conn.Execute(sql, stocks);
            }
        }




    }
}

