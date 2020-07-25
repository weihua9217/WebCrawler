using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using Dapper;

namespace operate
{
    class Program2
    {
        public class OrderItem
        {
            public int Id { get; set; }
            public int OrderId { get; set; }
            public int ProductId { get; set; }
            public decimal UnitPrice { get; set; }
            public int Quantity { get; set; }
        }

        public static List<object> ReadOrderItem()
        { //read and change the number (return the List<object>)
            IDbConnection db = new SqlConnection("Server=MATTHEWL-PC;Trusted_Connection=true");
            var sql = "Select * from [my db].[dbo].[OrderItem]";
            IEnumerable<OrderItem> orderItems = db.Query<OrderItem>(sql);

            List<object> OrderItemList = new List<object>();
            foreach (var orderitem in orderItems)
            {
                OrderItemList.Add(orderitem);
            }
            for (int i = 0; i < OrderItemList.Count; i++)
            {
                ((OrderItem)OrderItemList[i]).Quantity = ((OrderItem)OrderItemList[i]).Quantity + 10;
            }
            return OrderItemList;
        }
        public static void AddOrderItem()
        {
            using (var conn = new SqlConnection("Server=MATTHEWL-PC;Trusted_Connection=true"))
            {
                var orderitem = ReadOrderItem();
                
                var sqlCITemp =
                    @"  create table #T(
                        Id int not null,
                        OrderId int not null,
                        ProductId int not null,
                        UnitPrice decimal(12,2) not null,
                        Quantity int not null
                        );
                        insert into #T([Id],[OrderId],[ProductId],[UnitPrice],[Quantity])
                        values(@Id,@OrderId,@ProductId,@UnitPrice,@Quantity);
                        exec [my db].[dbo].[sp_practice_0808];";
                var executwResult = conn.Execute(sqlCITemp, orderitem);
            }
        }


    }





}