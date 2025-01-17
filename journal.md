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

### 852
Same algorithm as 162
> Issue here is you're not 100% clear about how you can modify 162 to break it or use different conventions and explain all that, so something to come and revise later.

### General to do:
Need to sit down and analyse binary search algorithm to figure out when stuff breaks or doesn't. There's some subtlties here. I think maybe helpful to explain in terms of how you're contracting the search space?

We will come back to 33 tomorrow, the search in a rotated array.

### Jotting some ideas for 33
You could explicilty find the pivot (doing a binary search to find a valley as it were?)

Or you can do it without finding pivot?


# 2024-04-25

### 33
Basically, your code needs to detect whether you're in the uppper part or the lower part of the rotation.

What is the mathematical proof that $\lfloor \frac{i + j}{2}\rfloor = i + \lfloor{\frac{j - i}{2}}\rfloor$


# 2024-05-08 Wed

I'm stuck on 713 but I don't want to look up the solution yet.


# 2024-05-13 Mon

I think I will start with ~~griding~~ figuring out how sliding window works.

Change of plan. I think for the next month: focus on array problems
- Sliding window  (I feel like a lot of these algorithms probably have some better theoretical explanation than all the rabbit out of hat tricks, but this is not what I care about right now, _how_ to come up with a solution on the spot)

_Maybe_ come back to things later re: why Kadane's algorithm works (can you state it in SRTBOT framework?)


# 2024-05-14 Tue
We had a good run, solved two sliding window problems using what I learnt yesterday. So let's just leave it at that.


# 2024-05-07 Fri
I think I sort of get sliding window now, especially variable length. Next one to focus on is recursion and back tracking.

I think my strategy will be:
- Follow this plan
    - But skip all the hards for now, we'll come back to them later in a month or so when your skills are better
- If you don't really get something, go look for more practice questions from `neetcode.io`.
- Once we've gone through all 12 weeks of this:
    - Go back and try the hards
    - Go through all of neetcode.

In an interview I assume you'd have to explain your logic as well, so...we will deal with this later, this is a different problem.


# 2024-05-19 Sun
Trying to figure out backtracking.

### On backtracking and all the backtracking confusion I'm having
_Notes to self_:
- Need to "see" what the recursion tree/tree we're traversing is for the problem. Sometimes I can't see that so recap all the existing problems to make sure you can draw it out.
- Since recursion with memoisation...maybe possible to convert some of these solutions into DP solutions (but this is a problem for later, we're trying to practice backtracking)

Some useful questions:
- 39 combination sum, 40 combination sum ii ,78 subsets, 90 subsets ii, 46 permutations, 47 permutations ii (Classic backtracking problems. Basically can you map your problem to a graph traversal?)
- 131, 784, 1087, 93, 1079

The problem I think you're having at the moment is can you make the implicit tree when doing backtracking, into an explicit tree?


# 2024-05-20 Mon

### Figuring out backtracking

Backtracking is a bruteforce algorithm.

Problem with greedy: only finds local minima/maxima.
Problem with dynamic programming: sometimes your subproblems are independent of each other.

Something to do with subproblem dependency graph?


### Backtracking
Mapping the search space as a tree of partial candidates, which you then dfs.
- Basically if a partial candidate violates a constraint, then we can just prune that branch and backtrack.


I'm going to redo all the practice problems for backtracking, then try to tackle some of the newer problems.
- Just conceptually do it with recursion. (We can test your understanding later by doing it with a stack.)

39 is weird
- I don't quite get why my presort solution is wrong


# 2024-05-21 Tue
I'm stuck on 47 and 90. The issue is how to avoid duplicates when searching.

We'll come back to 47 and 90. Look at the study problems and think about how you can draw the partial solution tree to avoid traversing duplicate sets. How do duplicates arise?

# 2024-05-22 Wed
We'll work on 47 and 90

Seems like if you're having to deal with duplicates, sorting the input _seems_ like a good idea.

### A useful link.
https://algo.monster/problems/stats

The issue is prioritisation and deciding what not to learn. What has most ROI is the real question.

> It's 10:36am now, I think we just have to stop, but at least you have clue to puzzle out for how to solve 90 (need to draw out the right partial solution tree that avoids traversing duplicates altogether)


# 2024-05-30 Thu
Life has got in the way and I've ended up skipping a few days.

I think realistically, we can only expect to solve one question a day. It's not exactly a matter of urgency that you learn this skill either. But it is important.

I think I'll move on to the training questions for stack techniques with arrays, kind of tired of doing the same topic over and over again. Should try to make a checklist of some standard techniques/toolbox of things you can chuck at problems at some point, I think part of the issue is it feels like all you have is a blunt spoon to work with quite often.

The advice I've read is to memorise the intuition and then practice using your intuition to get something to work.
### 11:13am
Need to move on to what I need to do for the rest of the day; don't have all the time in the world to look at monotonic stacks and how to use them


# 2024-06-03 Mon
> Wk2, 24T2

Somehow got `56` right on the spot without too much fuss.

Sorting your input seems to turn up a lot, maybe you should make a study of sorting algorithms again, since you're just being lazy in Python and calling `.sort()` all the time. The idea was that you could implement this in C if you had to.

> Actually I kind of wonder if it might be interesting to implement everything in Haskell just make you think in a different way...but this is a project for later.


The advice has been: if you can't figure it out in 15 minutes, then just look up the solution -- you'll build up intuition as you go.


# 2024-06-06 Thu 
Brainspace is just completely zapped right now, so probably better not to try tackle new problems. Skip ahead to some topics you've seen before and see if you can do them on the spot. 


# 2024-06-07 Fri
We're probably good with BFS/DFS stuff, it's actually a lot of the array stuff that I'm not 100% down with.

### 134
Try this on again and work through how it's solved with a greedy algorithm. 

> Reminder we're doing this in Python because I want to focus on grokking the algorithmic thinking (and not getting stuck in implementation issues)

> I think my general plan is: finish this list. Then go through neetcode's list; and that should give me general coverage of the patterns I'm likely to see.

> General goal is: aim to be able to be comfortable at solving any medium question within 30 minutes (i.e. within programming interview environment)

Still don't really understand why we can do this in a single pass.

# 2024-06-09 Sun 
I think go back to working on the greedy questions. Leave the "other stuff" like dfs/bfs/things we know for later or when you have a day where you feel like you don't want to do anything. 

### 134
Spent way too much time on understanding this question. The lesson seems to be: paying attention to constraints on whether solution exists or not, and figuring out how that constraint might affect how you go about finding a solution.

# 2024-06-09 Wed

### 134 
Proof needs a few tweaks but non urgent

### What we're doing today: 
Focus on learning the greedy algorithm techniques. No brain space for doing test questions. 

# 2024-06-17 Mon 
Probably need to be a bit more consistent...


### 402
Right I think all I have the brainpower for today is -- at least understand the intuition of how the algorithm works. Not at all apparent to me how you'd come up with the solution. 


# 2024-06-20 Thu 

Proofs for 134 look a bit fishy, come back to later. 

Re: greedy. Probably need to go look up a bit more of the theory. We'll watch a 3121 lecture if can find any.


### All the DFS questions 
Solve them recursively first. 

Not enough brain power today to do them, but most of them are easys. 



# 2024-06-24 Mon 

### 105 
I will learn this tomororw it's like a "deserialise a tree"

There's many standard tree algorithms, just go learn them. I seem to have less trouble with this topic than others. 

Trees are useful structures that turn up everywhere. e.g. a DOM is just a tree. hierachies are trees etc. 


# 2024-06-27 Thu 

### 743 
Recapping the _informal_ explanation for why/how Dijkstra's works. 

(Generally re how SSSP algorithms work) If we want to go from $u$ to $v$, we could go through $w$ i.e. $d(u, w) \leq d(u, v) + c(u, w)$. 
- So if our current estimate doesn't meet this we've violated the triangle inequality hence the reassignment of $d(u, w) \leftarrow d(u, v) + c(u, w)$ to relax. 
 
Picking which next neighbour to visit in Dijkstra's
- Optimal substructure: shortest paths are themselves made of shortest paths, hence we just greedily grab the next node that is closest to us (need to clarify formal statement of this at some point)

# 2025-01-07 Tue 
I can't remember why I stopped this for a bit. I think it was the Haskell course and then frontend taking up a lot of time. 

### 1514

Divine inspiration leads you to take a log (or well it's what engineers tend to do when you have a product and you want to deal with sums)


# 2025-01-05 Thu


### Thoughts about how to proceed
Maybe just have to make it a daily habit of solving one every day as warm up to whatever you have to do that day. 

I'm stuck on 1514, I'm going to give it 15 more minutes today, and then I'm looking up the intuition about how to solve it. 

### 1514 - we're still stuck

Probably best to just leave it for now and pick something else to do. I'm not sure why my current solution doesn't work. 


### 236
Come back to this algorithm tomorrow morning, not sure if I 100% grok it. 

Basically the idea is try to find the targets first, and then backtrack upwards to the LCA - at which point you only want to return the LCA information. I think if you grok the algorithm you should be able to write it iteratively. 

Will come back to it tomorrow