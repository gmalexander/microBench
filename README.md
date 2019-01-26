# Micro Bench

Micro Bench is a minimalistic benchmarking tool designed to be as isolated as reasonably possible from external influence that may skew the result.

## The Problem

Creating a valid benchmark comes with a number of challenges to overcome:
- Standard libraries change
- (Non-Standard) External dependencies change
- The host OS changes over time
- The hardware wears out over time

When taking all of these into account, it is often difficult to say with 100% certainty that a benchmark is "true" or reliable. It's then easy for the engineer, management, or whoever, to dismiss the failing benchmark with reasonable doubt.

## The Solution

To solve these challenges, a simple benchmarking tool needed to be crafted to try to get rid of as many of these variables as possible. An here we have microBench

## Requirements

### Language

When designing this tool, I had to be very aware of the factors stated in the problem statement. I needed something that was free of standard libraries potentially changing and nixing the result: a worst-case, custom implemented, insertion sort.

In addition to this, however, I had to scrutinize language implementations. If I were to write this in a JIT-compiled language, then on every execution, the result would be vulnerable to JIT-compiler changes affecting the performance of the program. This discounted my options of JavaScript, Python, and Java.

Unfortunately, I also had to discount languages or implementations of languages that require a higher degree of runtime support -  Visual C++ and Go, as I did not want the garbage collection algorithms (and their overhead), adding another layer of uncertainty to the deterministic performance algorithm used.

This left me with the understanding that the language of choice had to be statically compiled with little to no runtime support. Naturally, this led me to C++.

### Algorithm

Modern processors and their speed left me with the need for an extremely slow algorithm, that even enterprise mainframes would have difficulty processing below 10 or so seconds. For ease of implementation and its well understood nature, I chose the insertion sort. I harkened back to my CS days and recalled that an insertion sort has a worst case scenario of a presorted array, sorted in the opposite direction that the insertion sort is sorting. This yields a rather hefty algorithm of O(n^2).

To ensure that (very productive) modern methods of speeding up the algorithm (namely, Duff's Device) that may be present in modern implementations of the C++ standard library did not speed up the algorithm to the point of uselessness for benchmarking, I opted to implement the algorithm myself.

### Additional overhead

Looking at the code, you'll notice some a very fine detail I had to remain sensitive to in order to produce a valid benchmark. Namely, writing to standard out is entirely isolated from the benchmarking algorithm, for fear that OS-specific implementations may change overtime and cause the benchmark to be less trustworthy.

## The Result

From these requirements, I have created a benchmarking tool that is sufficiently isolated from all reasonable software overhead incurred by many modern programming techniques. I believe this tool is an accurate way to measure the speed of a server to determine three main factors about the system running Micro Bench:
- CPU/Memory health (as these two are permanently coupled together in the assignment of instructions to the CPU)
- Process pre-emption
- Environment speeds over time

## Final Challenge

There is only one point where one could still contend that Micro Bench is not a perfectly isolated benchmarking tool: its use of ctime. Theoretically, operating system specific implementations of time_t could result in retrieval times for the time itself that slightly skew the result of the benchmark. This is a challenge I look to resolve in future versions of this tool.

For now, I believe that this small overhead is tiny enough to not impact benchmark usage in a sufficient way, so long as I keep the SIZE variable sufficiently large. I would recommend using a standard deviation of one sigma in order to weed out any potential changes from time_t that may affect the benchmark over time.
