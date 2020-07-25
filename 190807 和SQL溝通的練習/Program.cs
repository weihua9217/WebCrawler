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
    class Program
    {

        public class Customer
        {
            public int Id { get; set; }
            public string FirstName { get; set; }
            public string LastName { get; set; }
            public string City { get; set; }
            public string Country { get; set; }
            public string Phone { get; set; }
        }

        static void Main()
        {
            Program2.AddOrderItem();
        }
        //read the phone number from certain people
        static void Read1()
        {
            IDbConnection db = new SqlConnection("Server=MATTHEWL-PC;Trusted_Connection=true");
            var @params = new { Country = "Mexico" };
            var sql = "Select * from [my db].[dbo].[Customer] where Country = @Country";
            IEnumerable<Customer> Customers = db.Query<Customer>(sql, @params);

            //db.Open();
            //var result = db.Query<string>("select * from [my db].[dbo].[Customer];");
            //Console.WriteLine(result);

            List<object> CustomerList = new List<object>();
            foreach (var customer in Customers)
            {
                CustomerList.Add(customer);
            }

            for (int i = 0; i < CustomerList.Count; i++)
            {
                string update()
                {
                    return ((Customer)CustomerList[i]).Phone + "ABC";
                }

                ((Customer)CustomerList[i]).Phone = update();

                Console.WriteLine(((Customer)CustomerList[i]).Phone);
            }
            Console.ReadLine();
        }
        static void AddTest1()
        {
            using (var conn = new SqlConnection("Server=MATTHEWL-PC;Trusted_Connection = true"))
            {
                var customer = new List<Customer>();
                customer.Add(new Customer()
                {
                    Id = 95,
                    FirstName = "Sara",
                    LastName = "Lin",
                    City = "Taipei",
                    Phone = "0955554878"
                });
                customer.Add(new Customer()
                {
                    Id = 96,
                    FirstName = "Jen",
                    LastName = "Wang",
                    City = "Taoyuan",
                    Country = "Taiwan",                
                });
                var sql2 =
                    @"SET IDENTITY_INSERT [my db].[dbo].[Customer] ON
                    insert into [my db].[dbo].[Customer]([Id],[FirstName],[LastName],[City],[Country],[Phone])
                    values(@Id,@FirstName,@LastName,@City,@Country,@Phone)";
                var executwResult = conn.Execute(sql2, customer);
            }
        }
    }
}


