# 2024-03-14 Thu 

Sliding window:
- Fixed length
- Variable length


# 2024-03-15 Fri

### 567
Problem you had was how to maintain the frequency table when sliding along, the window itself wasn't hard to see.

I've seen this trick where they use a 26 long array to be the frequency table rather than an explicit hashmap.


# 2024-04-03 Wed

### 828
Really stuck on this one, I'm not sure why my recursive attempt bruteforce searching all substrings isn't exploring all substrings?


# 2024-04-07 Sun
Aims for today: work on some two pointer training set questions
- Understand two pointer solution for 844
- Figure out how the solution to 828 works


The test set for sliding window is _really_ hard. Maybe need to go do some more practice on easies/mediums and come back to it later

Feels kinda like, constantly seeking around to find a jumpable gap and having to be very deliberate because it's like slime how many unsolvable things there are.

### 828
It's a dynamic programming problem, how is this a two pointer thing? Apparently the trick/intuition is to look at how many strings each token contributes to rather than traversing all substrings (since obviously they're overlapping). I think I'll leave this one for later.

# 2024-04-08 Mon

### 75
Dutch flag algorithm.

Come back to investigating why the loop invariant here should be `j <= k` not `i <= j`, I don't fully grok this.

Invariants we're maintaining (array bounds inclusive and treat $A[:-1]$ and $A[n:]$ to be empty.)
- $A[:i-1]$ should be an array of $0$'s
- $A[i:j-1]$ should be an array of $1$'s
- $A[k+1:]$ should be an array of $2$'s
- $A[j: k]$ is the part of the array that contains elements to be sorted

We shrink the last array by incrementing `j` but need to maintain invariant that $j \leq k$. That's the only reasonable explanation I can give for why the loop invariant is this way
- (it's tracking processing of elements, we've got two arrays on the left and one array on the right of it)

### Backtracking
Not sure if most of these problems involve DFS


# 2024-04-24

### 162
More binary search shenanigans

How do you make sure `mid` is a valid index?
> Why doesn't `(i + j) // 2` just work? Over having update rule as `i + (j - i) // 2`?

Whether `j` is inclusive or exclusive of search space?
> Algorithm is much easier if `j` is always a valid index. But it should be possible to write it in a way where it _isn't_? i.e. $A[i:i]$ is treated as array of 1 element rather than empty array if we have inclusive upper bound?

I wonder if Jensen's inequality has anything to do with why this works. Trying to find some locally convex thing? But priority here is more understanding how the binary search is behaving and how to break it and how to fix it.