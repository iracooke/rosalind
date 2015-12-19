# Longest increasing subsequence

	**Given:** A positive integer n≤10000 followed by a permutation π of length n.

	**Return:** A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

This can be viewed as a traversing the given sequence visiting the maximum number of increasing integers.  A way to visualise this is to create an alignment matrix between the given sequence and a perfectly ordered sequence of the same integers. Like with a normal alignment problem an arrow down or across is a gap and a diagonal is a match.  We score 1 for a match or 0 otherwise.


#Example Input
5
5 1 4 2 3

To get the longest increasing subsequence we align with the integers ordered from smallest to largest like this

  |  0 |  5 |  1     |  4 |  2     |  3
--|----|----|--------|----|--------|-------
0 |  0 |  0 |  0     |  0 |  0     | 0
1 |  0 | ⇓0 | **⬂1** | ⇒1 | ⇒1     | ⇓0
2 |  0 | ⇓0 | ⇓1     | ⇒1 | **⬂2** | ⇓0 
3 |  0 | ⇓0 | ⇓1     | ⇒1 | ⇓2     | **⬂3** 
4 |  0 | ⇓0 | ⇓1     | ⇒1 | ⇓2     | **⇓3**
5 |  0 | ⬂1 | ⇓1     | ⇒1 | ⇓2     | **⇓3**


And for the longest decreasing subsequence we use

  |  0 |  5 |  1 |  4 |  2 |  3
--|----|----|----|----|----|---
0 |  0 |  0 |  0 |  0 |  0 | 0
5 |  0 | **⬂1** | **⇒1** | ⇓0 | ⇓0 | ⇓0
4 |  0 | ⇓1 | ⇓1 | **⬂2** | **⇒2** | ⇒2 
3 |  0 | ⇓1 | ⇓1 | **⇓2** | ⇒2 | **⬂3** 
2 |  0 | ⇓1 | ⇓1 | ⇓2 | **⬂3** | **⇓3**
1 |  0 | ⇓1 | ⇓1 | ⇓2 | ⇓3 | **⇒3**

It turns out though that this method is overkill for the relatively simpler task at hand, and for long sequences it is far too slow.  We need a method
that uses the same dynamic programming concept but which does not require us to compute (and store in memory) the entire DP matrix.  

A much faster method is as follows;

For each position calculate the longest increasing subsequence that could be created up to and including that position.  At position i this is denoted by L[i].  For the first position this is very easy to calculate (it is just 1). For subsequent positions (i>0) we look back to previous positions, j and find the position that had the largest value of L[j] but which also satisfies the criterion seq[j] < seq[i] . The best possible value for L[i] will be L[j]+1.  So for position i we record its best possible length, L and we also record the position of its predecessor, j such that L[j] is the maximum value of L between 0 and i.  Once this is computed the sequence can easily be read off by examining the positions recorded in P.

#Example Input
9
8 2 1 6 5 7 4 3 9


    |  8  |  2  |  1  |  6  |  5  |  7  |  4  |  3  |  9
----|-----|-----|-----|-----|-----|-----|-----|-----|----
 i  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8 
P,L |-1,1 |-1,1 |-1,1 | 2,2 | 2,2 | 4,3 | 2,2 | 2,2 | 5,4
