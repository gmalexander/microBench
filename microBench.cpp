#include <iostream>
#include <ctime>

const int SIZE = 1000000;

int* initializeBenchmarkArray()
{
  int* benchmarkArray = new int[SIZE];
  for(int x = 0; x < SIZE; x++)
  {
    benchmarkArray[x] = SIZE-x;
  }
  return benchmarkArray;
}

void performBenchmarkAlgorithm(int benchmarkArray[SIZE])
{
  int* sortedArray = new int[SIZE];
  for(int x = 0; x < SIZE; x++)
  {
    for(int y = x; y > 0; y--)
    {
      if ( benchmarkArray[y] < benchmarkArray[y-1] )
      {
        int temp = benchmarkArray[y];
        benchmarkArray[y] = benchmarkArray[y-1];
        benchmarkArray[y-1] = temp;
      }
    }
  }
}

int main()
{
  std::cout << "Initializing benchmark array for worst case O(2) insertion sort of size: " << SIZE << "...\n";
  int* benchmarkArray = initializeBenchmarkArray();
  std::cout << "Benchmark array initialized.\n";

  std::cout << "Starting Benchmark...\n";
  std::time_t startTime = std::time(nullptr);
  performBenchmarkAlgorithm( benchmarkArray );
  std::time_t endTime = std::time(nullptr);
  std::cout << "Benchmark complete.\n";

  delete[] benchmarkArray;

  double duration = std::difftime(endTime, startTime);
  std::cout << "Time to taken to sort insertion sort of size '" << SIZE << "': " << duration << " seconds.\n";
}
