using System;

    public class Program
    {
        public static void Main(string[] args)
        {
        string line1 = Console.ReadLine ();
        string[] split = line1.Split(new char[] { ' ' }, StringSplitOptions.None);
        string line2 = Console.ReadLine ();
        string ofnumbers = "";
        int[] array = new int[]{Int32.Parse(split[0]), Int32.Parse(split[1]),Int32.Parse(split [2])};
        Array.Sort(array);
        for (int i = 0; i < 3; i++) {
            switch (line2 [i]) {
            case 'A':
                {
                    ofnumbers += array [0] + " ";
                    break;
                            
                }
            case 'B':
                {
                    ofnumbers += array [1] + " ";
                    break;
                }
            case 'C':
                {
                    ofnumbers += array [2] + " ";
                    break;
                }
            default:
                {
                    break;
                }
            }
        }
        Console.WriteLine (ofnumbers);  
        }

        }
