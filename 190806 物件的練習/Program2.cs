using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FirstSpace
{
    public class Animal
    {
        public string[] Food;
        public string Class;
    }
    public class Dog : Animal
    { 
        public string Local;
        public string[] Hate;
        public Dog(string[] _food , string _class)
        {
            Food = _food;
            Class = _class;
        }

    }
    public class Cat : Animal
    {
        public string Local; 
        public string[] Hate;
        public Cat(string[] _food, string _class)
        {
            Food = _food;
            Class = _class;
        }
    }
    public class Human : Animal
    {
        public string Local;
        public string[] Hate;
        public Human(string[] _food, string _class)
        {
            Food = _food;
            Class = _class;
        }
    }
    public class Shark : Animal
    {
        public string Local;
        public string[] Hate;
        public Shark(string[] _food, string _class)
        {
            Food = _food;
            Class = _class;
        }
    } 
    public class Fish : Animal
    {
        public string Local;
        public string[] Hate;
        public Fish(string[] _food, string _class)
        {
            Food = _food;
            Class = _class;
        }
    }

    public class Program
    {
        public static string[] Select()
        {
            Console.WriteLine("Pick one as char1:");
            Console.WriteLine("Tony(Dog), Kitty(Cat), Shrank(Shark), Fifi(Fish) , Matthew(Human)");
            string[] Options = { "Tony", "Kitty", "Shrank", "Fifi", "Matthew" };
            string char1 = Console.ReadLine();
            if (Options.Contains(char1))
            {
                Console.WriteLine("Char1 is {0}", char1);
                Console.WriteLine("====================");
                string char2 = SecondSelect();
                if (char1 == char2)
                {
                    Console.WriteLine("Error: Char1 is same as Char2");
                    Console.WriteLine("Please choose again!");
                    Console.WriteLine("====================");
                    return Select();
                }
                else
                {
                    Console.WriteLine("Char2 is {0}", char2);
                    Console.WriteLine("====================");
                    Console.WriteLine("{0} v.s {1}", char1, char2);
                    Console.ReadLine();
                    string[] Select = { char1, char2 };
                    return Select;
                }
            }
            else
            {
                Console.WriteLine("Error: Just Input The Name As Mention!");
                Console.WriteLine("====================");
                return Select();
            }
        }
        public static string SecondSelect()
        {
            string SecondSelect = Select();
            return SecondSelect;
            string Select()
            {
                Console.WriteLine("Pick one as char2:");
                Console.WriteLine("Tony(Dog), Kitty(Cat), Shrank(Shark), Fifi(Fish), Matthew(Human)");
                string[] Options = { "Tony", "Kitty", "Shrank", "Fifi", "Matthew" };
                string char2 = Console.ReadLine();
                if (Options.Contains(char2))
                {
                    return char2;
                }
                else
                {
                    Console.WriteLine("Error: Just Input The Name As Mention!");
                    Console.WriteLine("====================");
                    return Select();
                }
            }
        }
        public static string Compare()
        {
            string[] mySelect = Select();
            List<object> mySelect_object = new List<object>();
            for (int i = 0; i < mySelect.Length; i++)
            {
                switch (mySelect[i])
                {
                    case "Tony":
                        Dog Tony = new Dog ( new string[] {"Meat"} ,"Dog");
                        mySelect_object.Add(Tony);
                        break;
                    case "Kitty":
                        Cat Kitty = new Cat ( new string[] {"Fish"} ,"Cat" );
                        mySelect_object.Add(Kitty);
                        break;
                    case "Shrank":
                        Shark Shrank = new Shark(new string[] {"Fish"},"Shark");
                        mySelect_object.Add(Shrank);
                        break;
                    case "Fifi":
                        Fish Fifi = new Fish(new string[] {"Grass"},"Fish");
                        mySelect_object.Add(Fifi);
                        break;
                    case "Matthew":
                        Human Matthew = new Human(new string[] {"Meat","Fish"},"Human");
                        mySelect_object.Add(Matthew);
                        break;
                }
            }
            string[] char1Food = ((Animal)mySelect_object[0]).Food;
            string[] char2Food = ((Animal)mySelect_object[1]).Food;
            string char1Class = ((Animal)mySelect_object[0]).Class;
            string char2Class = ((Animal)mySelect_object[1]).Class;
            if (char1Food.Contains(char2Class))
            {
                return "char1 eats char2";
            }
            else if (char2Food.Contains(char1Class))
            {
                return "char2 eats char1";
            }
            else
            {
                return "nothing happend";
            }
            
        }
        public static void Main(string[] args)
        {
            string Output = Compare();

            Console.WriteLine("The output is [ {0} ]", Output);
            Console.ReadLine();
        }

    }



}
    