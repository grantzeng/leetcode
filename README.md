# Retrospectives

Notes about how to solve each problem/intuitions

### Week 1 - Arrays - Sliding Window

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/maximum-average-subarray-i/description/ | $k$ is fixed so just take window sum and you can compute average at the end. Error cases happen when array is size $< k$; you need to ask what behaviour is expected.  |
| https://leetcode.com/problems/find-all-anagrams-in-a-string/description/ | Strings which are anagrams will have the same "spectrum"/character frequency table. Suboptimal solution is to rebuild the window's table every time, better solution is to update the table each time the window slides. You can use a hashtable, or you can do the C-style trick of a 26-element array (`TODO: implement C-style version`). Edge cases: when `p` is shorter than `s`. |
| https://leetcode.com/problems/permutation-in-string/description/?envType=list&envId=xlep8di5 | Similar strategy to above (check permutation, in this context permutations and anagrams are the same thing). (`TODO: come back to implement C-style solution` later.). Same edge case where target is bigger than string being searched|
| https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/?envType=list&envId=xlep8di5 | `HARD COME BACK LATER` |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/ | Straightforward fixed length sliding window, just watch out for off-by-one errors with sliding the window |
| https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=list&envId=xlep8di5 | Modified prefix sum (the difficulty is figuring out when to grow and shrink the window) |
| https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=list&envId=xlep8di5 | Use the same pattern of outer loop trying to extend the window and inner loop to contract window to fix any invariant violations we require of a subarray |
| https://leetcode.com/problems/longest-substring-without-repeating-characters/description/ | ~~$O(n^2)$ solution is to just bruteforce search forward until duplicate at every position. `TODO: Figure out a more minimal solution that is faster that is more C style`~~  Variable length sliding window, just have an outer loop that keeps trying to extend right bound and inner loop that contracts leftbound. Like a catepillar. (Basically similar to 209/above question). Bruteforce solution is just trying every fixed window length so that ends up being $O(n)$ |
| https://leetcode.com/problems/sliding-window-maximum/description/?envType=list&envId=xlep8di5mi | `HARD` |
| https://leetcode.com/problems/minimum-window-substring/description/?envType=list&envId=xlep8di5 | `HARD` |
| https://leetcode.com/problems/subarray-product-less-than-k/description/ | Maintain window product. Main change is the increment to count of how many subarrays should be `j -i + 1` not just `1` because if $A[i:j]$ has product less than k, then so will all $A[i:x]$ for $x < j$|



| Stuff from Neetcode | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/| Greedily keep taking better buy price, `i` needs to lag `j`  to keep buy before sell.|
|~~https://leetcode.com/problems/longest-substring-without-repeating-characters/~~ ||
|~~https://leetcode.com/problems/longest-repeating-character-replacement/description/~~||
|~~https://leetcode.com/problems/permutation-in-string/description/~~||
|~~https://leetcode.com/problems/minimum-window-substring/description/~~||
|~~https://leetcode.com/problems/sliding-window-maximum/description/~~||

### Some quick notes about implementing variable sliding windows
We want to continually push the window to the right to "finish processing the whole array".

Something I've noticed: basically for a variable sliding window need to handle:
 - Expanding right bound (usually just get it to keep inching forward) (You can use a for loop to do this, but to me I am still moving a pointer around so I prefer while)
 - Contracting left bound (i.e. on what conditions do we move the left bound?) Often this looks like deleting things until the slice satisifes some invariant.

Usually entirely apparent to me _how_ you could prove correctness, but that's not the point. Maybe they'll address this in 3121.

*Added 2024-05-20*:
- Often you are wanting to keep some kind of "statistic" about a window, and you have to figure out how to update this when the window moves (for memory saving reasons, rather than regenerating it every time. I mean statistic in the broadest sense as a summary of the most important feature of the window, e.g. it could be a letter frequency table)
- I mean it's the same deal with a fixed width sliding window, the main difference is just that with every tick, you increment $i$ and $j$ by $1$ as the update rule for the window.

### Week 2 - Arrays - Two Pointers

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/backspace-string-compare/description/?envType=list&envId=xlem03mm | Parse from right to left to avoid having to backtrack, and write a helper function to grab next valid token (The helper is basically a state machine, it's either looking for a valid token to return, or it's looking for a token to skip because of backspace). (_Intuition_: Generally with string/array problems try to come up with single pass solution) |
| https://leetcode.com/problems/3sum/description/?envType=list&envId=xlem03mm | Repeat 2SUM two pointer solution for every prefix array (this is the whole "fix the first pointer" thing), but you have to pay for the sort for this to work. `TODO: Optimize this` |
| https://leetcode.com/problems/sort-colors/description/?envType=list&envId=xlem03mm | Dutch national flag algorithm.  You need `j <= k` in the loop invariant because it's the array $A[j: k]$ that contains the unsorted elements (see notes in journal for discussion of invariants we're maintaining).|
| https://leetcode.com/problems/container-with-most-water/description/?envType=list&envId=xlem03mm | *Greedy*. Greedily try to update the pointer pointing to the lowest height since you're going to get the best improvements to area from increasing height (whereas $\delta x$ is always $-1$) |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/two-sum/description/?envType=list&envId=xlem03mm | (Sorting solution is fine when you don't have to return original indices because otherwise you have to track the index scrambling, and you might as well have done the $O(n)$ hash table solution instead) |
| https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=list&envId=xlem03mm | Build the result in reverse, because the maximum element is going to be at either `0` or `n - 1`. That's where the two pointers comes in. (No need to try to find a "centre" element and then two pointer your way to the boundary) |
| ~~https://leetcode.com/problems/subarray-product-less-than-k/description/~~ | (See sliding window) |
| https://leetcode.com/problems/3sum-closest/description/?envType=list&envId=xlem03mm | You need to know the 3SUM 2 pointer algorithm since this will inch all the pointers to a triplet that sums closest to the target, the only difference is just needing to update the closest sum every time|
| https://leetcode.com/problems/trapping-rain-water/description/?envType=list&envId=xlem03mm | `HARD` |

### Week 3 - Arrays - Recursion & Backtracking

> `TODO: Rewrite all your retrospection notes in terms of what the partial candidate tree looks like`. Because that is the essence of what backtracking is doing.


| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=list&envId=xlere2g3 | You're doing a DFS on a sort of prefix tree, and trying to print out all possible paths from root to any leaf node. So you'd use either a stack or recursion |
| https://leetcode.com/problems/combination-sum/description/?envType=list&envId=xlere2g3 | More backtracking using DFS to traverse a "prefix tree". The issue is coming up with stopping case. |
| https://leetcode.com/problems/permutations/description/?envType=list&envId=xlere2g3 | ~~Use a set that has remaining elements and traverse through and leave one out for the next call. Basically if you can see how generating permutations as a tree works, you can write the back tracking to do it~~ Search space is a set difference at every branch of the partial candidate graph, instead of a suffix. |
| https://leetcode.com/problems/combinations/description/?envType=list&envId=xlere2g3 | ~~Similar to permutation, but you only want to test adding elements to "right" of current element to the combo. You can either add number `i` or not add number `i` and let the recursion generate the branching of the tree. Stopping case when combination considered is length `k`~~ Search space after adding `j` is `j + 1, ...` or `j+2, ....` or `j+3, ...` etc.  |
| https://leetcode.com/problems/subsets/description/?envType=list&envId=xlere2g3 | ~~There's $2^n$  possible subsets, use a DFS to explore that and do backtracking on the tree. It's the loop _and_ recursion that generates the branching at each point~~ We just want all nodes in the partial solution tree |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/generate-parentheses/description/?envType=list&envId=xlere2g3 | Couldn't completely get this one on first go, but idea is still you either add a `(` or a add a `)` in one step, then delete it after backtracking; the issue is figuring out what the right condition for this should be. (Do some gardening on the the decision tree of adding `(` or `)` so we only look at strings satisfying the balance constraint) |
| https://leetcode.com/problems/combination-sum-ii/description/?envType=list&envId=xlere2g3 | Search space is `A[j+1:]` once you've included `A[j]`, not `A[j:]` . This is because you're not allowed to reinclude used elements! Also you want to prune off branches that consider `A[x:]` where `A[x] =A[x-1]` because this would also result in duplicates |
| https://leetcode.com/problems/permutations-ii/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/subsets-ii/description/?envType=list&envId=xlere2g3 | Partial solution tree branch is based on "do we include _any number_ of $i$ or not" rather than "do we include `num[i]` or not". Hence sorting input.  |
| https://leetcode.com/problems/palindrome-partitioning/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/target-sum/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/combination-sum-iii/description/?envType=list&envId=xlere2g3 | Basically same as Combination 1. If you include $A[i]$ then remaining search space is $A[i + 1:]$ ($A$ can just be implicit by using a `range(i + 1, 10)`) |
| https://leetcode.com/problems/sudoku-solver/description/?envType=list&envId=xlere2g3 |  `HARD` |


### Some quick notes on backtracking

What the hell is going on?
- Is a bruteforce exploration of all possible candidate sets. Essentially DFS the partial candidate tree (if you happen across a node/partial candidate that violates some constraint/invariant then we know we can ignore that subtree, then just backtrack to the last place the partial candidate was still okay).
    - _Contrast_: DP (problems have some dependencies which you can carefully traverse to avoid doing extra work), greedy (greedily go to local optima, but obviously exploration space might not be "convex" in some sense so not necessarily coincides with global optima)
> Sometimes the difficulty is conceptualising what the tree looks like (if we care about duplicates, then branching might be based on include/exclude any number of an element, rather than include/exclude position $i$ of input. Useful to sort input here if so).
- I think the recursion only comes about because it's the easiest way to implement a DFS.

The "backtracking" comes from adding/removing elements from a variable you use to store a current potential solution. But really we are just doing a DFS of a partial candidate tree, so you might as well just write the code to express partial candidates explicitly.

Backtracking is used for constraint optimization e.g. job shop scheduling is a backtracking algorithm (?). Basically trying to find sets that satisfy constraints.

(Others to try later if not done already)
- (Useful basic ones): 39 combination sum, 40 combination sum ii ,78 subsets, 90 subsets ii, 46 permutations, 47 permutations ii (Classic backtracking problems. Basically can you map your problem to a graph traversal?)
- 131, 784, 1087, 93, 1079

It's not entirely apparent to me why sometimes if you sort the input first your exploration of the partial combination tree is nicer? But just know this as an idea.

**What to call the function?** I think `search` is a better name than `backtrack`. Backtracking doesn't capture fact we're exploring partial combination tree with a DFS.


### Week 4 - Arrays - Binary Search


| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/ | Modified binary search, but it's still a little bit unclear to me why `i` should land exactly on the second lowest one `TODO: need to think about this for a bit` |
| https://leetcode.com/problems/find-peak-element/description/ | Greedy update `mid` to the neighbour if it's less than either of its neighbours (if the neighbour exists). But there are issues re: implementation in keeping `mid` a valid index and how to code up loop condition to make sure it terminates (Are you treating $A[i:j]$ as including $j$ or not?) |
| https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=list&envId=xleplgq3 | Reuse peak finding algorithm for 162 |
| https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=list&envId=xleplgq3 | Either $A[i:mid]$ is monotonic or it isn't (or symmetrically we could consider $A[mid: j]$), then just do binary search thing of kicking $i$ and $j$ towards the position where target would be, if it exists.   |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/first-bad-version/description/ | Standard binary search implementation; just test if the mid point is bad or not, if it's not bad, we can safely raise the lower bound $i$. $i$ should land on position of bad version because it will always be $mid + 1$ (?)  |
| https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/search-a-2d-matrix/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/count-of-range-sum/description/?envType=list&envId=xleplgq3 |  |

### Some quick notes on implementing binary searches
Binary search only works if you can assume input is monotonic, like you _need_ the total ordering on inputs. The problem I run into a lot of time with binary search is the whole off by one error and whether you've written the loop assuming inclusive or exclusive end points for bounds.

Need to revise reasoning about the invariants at play and why sometimes you end up in an infinite loop and not. I did write this up at some point but I'd forgotten.
- Basically the issue is whether you treat array slices as inclusive/exclusive of upper bounds (and this changes what you set as `hi` and what the stopping condition of the while loop is (it should stop on an empty array: "continue until search space is exhausted"))

### Week 5 - Arrays - Stack

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/valid-parentheses/description/ | It's all about tokens. (And use a hash table to keep track of things matching up) |
| https://leetcode.com/problems/maximum-subarray-min-product/description/ | I definitely had zero idea about how to solve this, so looked up the intuition: monotonic stack to find for what subarray $A[i:j]$ is $A[k]$ minimal for + prefix sums to get subarray sums in constant time. (Very difficult because never seen these tools before.). (There are other ways of doing this problem apparently.) `TODO: COME BACK TO MONOTONIC STACKS LATER` |
| https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/ | "Conceptual stack". See `#20` if you don't know what I mean |
| https://leetcode.com/problems/merge-intervals/description/ | Pay for a sort then do a single pass. |
| https://leetcode.com/problems/maximum-frequency-stack/description/ | `HARD` |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/daily-temperatures/description/  |  |
| https://leetcode.com/problems/asteroid-collision/description/ |  |
| https://leetcode.com/problems/next-greater-element-ii/description/ |  |
| https://leetcode.com/problems/132-pattern/description/ |  |
| https://leetcode.com/problems/largest-rectangle-in-histogram/description/ |  |
| https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/ |  |


##
- If you're having to sum subarrays, precomputed prefix sums will let you do this in $O(1)$
### Monotonic stacks
- Look at 496 to get an idea of how monotonic stacks can be useful?

### Week 6 - Arrays - Greedy

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/gas-station/description/ | ~~(Baffling, come back later)~~ I don't get why this one is greedy, this really should be a math question and depends on you recognising what the constraints are. The only way I think I could possibly come up with the algorithm on my own is to find conditions for solution existence, then looking at how that constraint affects how one would find a solution. |
| https://leetcode.com/problems/largest-number/description/ | It's obviously greedy, you want the largest number in the largest positions, but you need a custom comparator to compare things like "3" vs "34" vs "33" as to what's the best position. (Will need to come back to this - can you implement your own parser and sorting algorithms and not rely on Python? You could just strip zeros from the front of the sorted list as well) |
| https://leetcode.com/problems/remove-duplicate-letters/description/ |(Come back to it later, since I'm not 100% but the idea seems to be "greedily build result" rather than "delete letters from final string". Probably goes back to idea that _if you have an array, think about finding a one pass solution?_ ) UPDATE: Nope, it's just another monotonic stack. |
| https://leetcode.com/problems/remove-k-digits/description/ | You want the front of your number to be monotonically increasing, then you just have to deal with the fact that you have to add whatevers left when you run out of deletes. `TODO: Go look at the proof of correctenss that "greedy stays ahead", I've never really seen this` |
| https://leetcode.com/problems/integer-replacement/description/ | When even, you don't have a choice. When odd, make the greedy choice (what's the better option two steps away?) `TODO: There is a DP solution to this, come back to this question when you get up to DP` |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/longest-palindrome/description/ |  |
| https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/ |  |
| https://leetcode.com/problems/valid-triangle-number/description/ |  |
| https://leetcode.com/problems/increasing-triplet-subsequence/description/ |  |
| https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/ |  |


### Notes to self: 
Greedy is a new algorithm technique to me. 

See COMP3121 lectures if you can find any copies online re: how to recognise greedy. The algorithms are amazingly simple, yet...a lot of cleverness. I think I just need a few more worked examples.
- For `316` it's the same as `402`. You just have strings that base-26 instead of base-10, the principle of wanting the front of the string to be monotonic increasing is the same. 
- `719` is basically decreasing lexical sort. So `'9' > '35'` and `'35' > 33 > 3_'` I think. 

I think there's two things for me to do here:

1.  Need more exposure to examples of using greedy methods (it seems like it's a very general and useful technique but requires you to recognise some substructure in the problem for it to work. I think for remove-k you'd have to play around with the problem to try to discover substructure of what preferences we'd have when building the string) 
2.  Proofs of correctness to understand why greedy works. "Greedy stays ahead" etc. 

It's not like with BFS or DFS where it's as straightforward as mapping the problem to them. 

Basically, for the remove $k$ problem, it really is a search problem. You have a $\binom{n}{k} = \mathcal{O}(n^k)$ search space. But this is too big to do by bruteforce and you sort of have to recognise some substructure that makes your life easier.
> Similar ideas might come up in combinatorial optimization?

### Week 7 - Trees - BFS

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/minimum-depth-of-binary-tree/description/?envType=list&envId=xlepfebm | If doing BFS iterative solution, just track the node depth with the node in the queue rather than fiddling with a single variable. (For DFS solution, need to visualise how you're adding 1's and minning the sums)|
| https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=list&envId=xlepfebm | Try `102` if you forgot how to do level order traversal. (Also don't forget to return the data structure you're modifying, d'oh.) |
| https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=list&envId=xlepfebm | It's just level order traversal except you reverse the order in which you print the values if the level is odd |
| https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/?envType=list&envId=xlepfebm | Just do a level order traversal and keep the results in reverse |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=list&envId=xlepfebm | (Just go learn the algorithm)  |
| https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=list&envId=xlepfebm |  |

### Things to do: 
- Reimplement all these with a DFS later, the BFS algorithm you use is _basically_ the same in every question. 

### Weeks 8 - 10 Trees - DFS

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/same-tree/description/ | Tree must recursively satisfy the equality constraint (just write out the DFS to be explicit about what the cases are) |
| https://leetcode.com/problems/merge-two-binary-trees/description/ | Doing two DFSs at the same time.  |
| https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/ |  |
| https://leetcode.com/problems/path-sum/description/ | This is another DFS. Can't call search off early if remaining goes below zero, because no guarantees only positive values |
| https://leetcode.com/problems/diameter-of-binary-tree/ |  |
| https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/ |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/maximum-depth-of-binary-tree/description/ |  |
| https://leetcode.com/problems/invert-binary-tree/description/ |  |
| https://leetcode.com/problems/path-sum-ii/ |  |
| https://leetcode.com/problems/binary-tree-maximum-path-sum/description/ |  |
| https://leetcode.com/problems/sum-root-to-leaf-numbers/description/ |  |
| https://leetcode.com/problems/implement-trie-prefix-tree/description/ |  |
| https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/ |  |
| https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/ |  |
| https://leetcode.com/problems/validate-binary-search-tree/ |  |
| https://leetcode.com/problems/word-search-ii/description/ |  |
| https://leetcode.com/problems/path-sum-iii/ |  |
| https://leetcode.com/problems/subtree-of-another-tree/description/ |  |
| https://leetcode.com/problems/maximum-binary-tree/ |  |
| https://leetcode.com/problems/maximum-width-of-binary-tree/ |  |
| https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/ |  |

### Week 11 - Graphs & Matrices - BFS & DFS

| Study solutions - Matrices | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/flood-fill/description/ |  |
| https://leetcode.com/problems/number-of-islands/description/ |  |
| https://leetcode.com/problems/max-area-of-island/ |  |

| Practice & apply - Matrices | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/island-perimeter/description/ |  |
| https://leetcode.com/problems/pacific-atlantic-water-flow/description/ |  |
| https://leetcode.com/problems/surrounded-regions/description/ |  |
| https://leetcode.com/problems/count-sub-islands/description/ |  |

| Study solutions - Graphs | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/evaluate-division/description/ |  |
| https://leetcode.com/problems/get-watched-videos-by-your-friends/description/ |  |
| https://leetcode.com/problems/clone-graph/description/ |  |
| https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/ |  |

| Practice & apply - Graphs | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/accounts-merge/description/ |  |
| https://leetcode.com/problems/number-of-provinces/description/ |  |
| https://leetcode.com/problems/course-schedule-ii/ |  |
| https://leetcode.com/problems/redundant-connection/description/ |  |

### Week 12 - Graphs - Shortest Path & Dijkstra’s

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/network-delay-time/description/ |  |
| https://leetcode.com/problems/path-with-maximum-probability/description/ |  |
| https://leetcode.com/problems/word-ladder/description/ |  |
| https://leetcode.com/problems/cut-off-trees-for-golf-event/description/ |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/path-with-minimum-effort/description/ |  |
| https://leetcode.com/problems/cheapest-flights-within-k-stops/description/ |  |
| https://leetcode.com/problems/critical-connections-in-a-network/description/ |  |
| https://leetcode.com/problems/shortest-path-to-get-all-keys/description/?envType=list&envId=xler60c5 |  |


### Week 13 - Potpourri
> Added this myself as checklist of non-urgent things to do 
Reimplement all sorts (i.e. at this point you're using `sort()` a lot but you should probably know for example how to implement the sort in C)