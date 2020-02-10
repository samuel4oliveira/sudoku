using System;

namespace AISudokuSolver
{
    class Program
    {
        static void Main(string[] args)
        {

            int[,] matrix = new int[9, 9];
            int i;
            int j;

           //#iniciar array com 0
            for (i = 0; i < 9; i++)
            {
                for (j = 0;j < 9; j++)
                {
                    matrix[i,j] = 0;
                }
            }


            int rowLength = matrix.GetLength(0);
            int colLength = matrix.GetLength(1);
            int countPrintColuna = 0;
            int countPrintLinha = 0;
            //Printar array

            Console.Write("*-------+-------+-------*");
            Console.Write("\n| ");
            for (i = 0; i < rowLength; i++)
            {
                for (j = 0; j < colLength; j++)
                {

                    if (countPrintColuna == 3)
                    {
                        Console.Write("| ");
                        countPrintColuna = 0;
                    }                   
                    Console.Write(string.Format("{0} ", matrix[i, j]));
                    countPrintColuna++;
                }
                countPrintLinha++;
                if (countPrintLinha == 3)
                {
                    Console.Write("\n");
                    Console.Write("*-------+-------+-------*");
                    countPrintLinha = 0;
                }
                Console.Write("\n");
            }
            Console.ReadLine();

            Console.WriteLine(matrix);

          


            
        }

        void print_separator()
        {
            for (int i = 0; i < 3; ++i)
            {
                Console.Write("+---------*");
            }
            Console.Write("|");
        }
     
    }
}
