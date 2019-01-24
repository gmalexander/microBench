## Benchmarking is tough

If you've ever delved into attempts to benchmark something, you often know there are a lot of problems.
- Your own app is changing
- The machine you're building on is updating over time
- The hardware you're using might even be wearing down

To solve this complex problem, I decided to implement a rather simple technique. A static, tiny benchmark tool that never changes, because it's built with the bare minimum. Well, close to bare minimum, anyway. I'd use ANSI C, but I want *some* abstraction.

Anyway, the technique is to send a rather large (size 10000) array through an insertion sort algorithm. This is a decent measure of performance in that the array is sorted *descendingly* for an insertion sort algorithm that sorts *ascendingly*. This creates the O(N^2) worst case scenario for the insertion sort, and makes it a rather timely algorithm.

By taking the time of this process, we can tell a few things about our host system:
- CPU load - is the program being pre-empted by the operating system?
- Memory - are we being forced into a pagefile to accomodate a high memory load?
