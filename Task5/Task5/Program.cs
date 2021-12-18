using System;
using System.Threading;

class Program
{
    private static int[,] garden;
    private static int width;
    private static int height;

    public static void Main()
    {
        StartProgramm();
    }

    private static void StartProgramm()
    {
        Console.WriteLine("Type 1 to enter garden settings or 2 to generate it randomly");

        int var, speed1, speed2;
        var = Convert.ToInt32(Console.ReadLine());

        if (var == 1)
        {
            Console.Write("Enter speed of first gardener(1 - faster, 10 - slower):");
            Int32.TryParse(Console.ReadLine(), out speed1);

            Console.Write("Enter speed of second gardener(1 - faster, 10 - slower):");
            Int32.TryParse(Console.ReadLine(), out speed2);

            enterGardenSettings(speed1, speed2);
        } else if (var == 2) {
            Console.Write("Enter speed of first gardener(1 - faster, 10 - slower):");
            Int32.TryParse(Console.ReadLine(), out speed1);

            Console.Write("Enter speed of second gardener(1 - faster, 10 - slower):");
            Int32.TryParse(Console.ReadLine(), out speed2);

            randomGardenSetting(speed1, speed2);
        }  else if (var == 3) {
            Console.WriteLine("***DEVELOPERS ONLY***");
            Random rand = new Random();
            int amount;

            Console.WriteLine("Enter amount of tests:");
            Int32.TryParse(Console.ReadLine(), out amount);

            for (int i = 0; i < amount; i++) {
                randomGardenNotWrite(rand.Next(1, 100), rand.Next(1, 100));
            }
        } else {
            Console.WriteLine("Incorrect parameter!\n");
        }
    }

    private static void randomGardenNotWrite(int ms, int ms2)
    {
        Random rand = new Random();
        height = rand.Next(1, 15);
        width = rand.Next(1, 15);

        var watch = System.Diagnostics.Stopwatch.StartNew();
        garden = new int[height, width];

        Thread fir_gardener = new Thread(() => fir_garden(ms));
        Thread sec_gardener = new Thread(() => sec_garden(ms2));

        fir_gardener.Start();
        sec_gardener.Start();

        fir_gardener.Join();
        sec_gardener.Join();

        watch.Stop();
        var elapsedMs = watch.ElapsedMilliseconds;

        Console.WriteLine($"Program execution time: {elapsedMs}ms");
    }

    private static void randomGardenSetting(int ms, int ms2)
    {
        Random rand = new Random();
        height = rand.Next(1, 25);
        width = rand.Next(1, 25);

        var watch = System.Diagnostics.Stopwatch.StartNew();
        garden = new int[height, width];

        Thread fir_gardener = new Thread(() => fir_garden(ms));
        Thread sec_gardener = new Thread(() => sec_garden(ms2));

        fir_gardener.Start();
        sec_gardener.Start();

        fir_gardener.Join();
        sec_gardener.Join();

        if (height < 25 || width < 25)
        {

            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    Console.Write(garden[i, j] + " ");
                }
                Console.WriteLine();
            }
        }

        watch.Stop();
        var elapsedMs = watch.ElapsedMilliseconds;

        Console.WriteLine($"Program execution time: {elapsedMs}ms");
    }

    private static void enterGardenSettings(int ms, int ms2)
    {
        Console.WriteLine("Enter height of the garden:");
        Int32.TryParse(Console.ReadLine(), out height);

        Console.WriteLine("Enter width of the garden:");
        Int32.TryParse(Console.ReadLine(), out width);

        var watch = System.Diagnostics.Stopwatch.StartNew();
        garden = new int[height, width];

        Thread fir_gardener = new Thread(() => fir_garden(ms));
        Thread sec_gardener = new Thread(() => sec_garden(ms2));

        fir_gardener.Start();
        sec_gardener.Start();

        fir_gardener.Join();
        sec_gardener.Join();

        if (height <= 25 && width <= 25)
        {

            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    Console.Write(garden[i, j] + " ");
                }
                Console.WriteLine();
            }
        }

        watch.Stop();
        var elapsedMs = watch.ElapsedMilliseconds;

        Console.WriteLine($"Program execution time: {elapsedMs}ms");
    }

    private static void fir_garden(int ms)
    {
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                if (garden[i, j] == 0)
                    garden[i, j] = 1;
                Thread.Sleep(ms);
            }
        }
    }

    private static void sec_garden(int ms)
    {
        for (int i = width - 1; i > 0; i--)
        {
            for (int j = height - 1; j > 0; j--)
            {
                if (garden[j, i] == 0)
                    garden[j, i] = 2;
                Thread.Sleep(ms);
            }
        }
    }
}