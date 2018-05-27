using System;

public class Program {
    public static void Main() {
        string line = Console.ReadLine();
        string[] split = line.Split(new char[] { ' ' }, StringSplitOptions.None);
        long B = Int64.Parse(split[0]), Br = Int64.Parse(split[1]), Bs = Int64.Parse(split[2]);
        long A = Int64.Parse(split[3]), As = Int64.Parse(split[4]);
        long Ar = A;
        long BobSaved = (Br - B) * Bs;
        long AliceSavedMoney = 0;
        while(AliceSavedMoney <= BobSaved){
            AliceSavedMoney += As;
            Ar += 1;
            }
        Console.WriteLine(Ar);
        }
    }
