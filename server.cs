using System;

    public class Server
    {
        
        public static void Main (string[] args)
        {
            string line1 = Console.ReadLine();
            string line2 = Console.ReadLine();
            string[] split = line1.Split(new char[] { ' ' }, StringSplitOptions.None);
            int remaining_time = Int32.Parse (split [1]);
            int tasks_done = 0;
            string[] array = line2.Split(new char[] { ' ' }, StringSplitOptions.None);
            for (int i = 0; i < array.Length; i++) {
                remaining_time -= Int32.Parse(array [i]);
                if (remaining_time >= 0) {
                    tasks_done += 1;
                }else{
                    break;
                }
            }
            Console.WriteLine (tasks_done);
        }
    }
