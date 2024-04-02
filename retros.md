# Retrospectives
(Study plan for adding notes about how to solve these things)


Things to think about:
- Pros/cons of different solutions
- Error cases/edge cases and how to handle
- What the optimal solution is (since you have to converge on this in an interview eventually).

The notes are about grokking the algorithm involved, I've put all the time and space complexities in all my solutions.

### Week 1 - Arrays - Sliding Window


| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/maximum-average-subarray-i/description/ | $k$ is fixed so just take window sum and you can compute average at the end. Error cases happen when array is size $< k$; you need to ask what behaviour is expected.  |
| https://leetcode.com/problems/find-all-anagrams-in-a-string/description/ | Strings which are anagrams will have the same "spectrum"/character frequency table. Suboptimal solution is to rebuild the window's table every time, better solution is to update the table each time the window slides. You can use a hashtable, or you can do the C-style trick of a 26-element array (`TODO: implement C-style version`). Edge cases: when `p` is shorter than `s`. |
| https://leetcode.com/problems/permutation-in-string/description/?envType=list&envId=xlep8di5 | Similar strategy to above (check permutation, in this context permutations and anagrams are the same thing). (`TODO: come back to implement C-style solution` later.). Same edge case where target is bigger than string being searched|
| https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/?envType=list&envId=xlep8di5 | Dynamic programming means come up with a recursive solution first (SRTBOT) then traverse the subproblem graph carefull |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/ |  |
| https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=list&envId=xlep8di5 |  |
| https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=list&envId=xlep8di5 |  |
| https://leetcode.com/problems/longest-substring-without-repeating-characters/description/ |  |
| https://leetcode.com/problems/sliding-window-maximum/description/?envType=list&envId=xlep8di5mi |  |
| https://leetcode.com/problems/minimum-window-substring/description/?envType=list&envId=xlep8di5 |  |

### Week 2 - Arrays - Two Pointers

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/backspace-string-compare/description/?envType=list&envId=xlem03mm |  |
| https://leetcode.com/problems/3sum/description/?envType=list&envId=xlem03mm |  |
| https://leetcode.com/problems/sort-colors/description/?envType=list&envId=xlem03mm |  |
| https://leetcode.com/problems/container-with-most-water/description/?envType=list&envId=xlem03mm |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/two-sum/description/?envType=list&envId=xlem03mm |  |
| https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=list&envId=xlem03mm |  |
| https://leetcode.com/problems/subarray-product-less-than-k/description/ |  |
| https://leetcode.com/problems/3sum-closest/description/?envType=list&envId=xlem03mm |  |
| https://leetcode.com/problems/trapping-rain-water/description/?envType=list&envId=xlem03mm |  |

### Week 3 - Arrays - Recursion & Backtracking

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/combination-sum/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/permutations/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/combinations/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/subsets/description/?envType=list&envId=xlere2g3 |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/generate-parentheses/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/combination-sum-ii/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/permutations-ii/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/subsets-ii/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/palindrome-partitioning/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/target-sum/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/combination-sum-iii/description/?envType=list&envId=xlere2g3 |  |
| https://leetcode.com/problems/sudoku-solver/description/?envType=list&envId=xlere2g3 |  |

### Week 4 - Arrays - Binary Search

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/ |  |
| https://leetcode.com/problems/find-peak-element/description/ |  |
| https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=list&envId=xleplgq3 |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/first-bad-version/description/ |  |
| https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/search-a-2d-matrix/description/?envType=list&envId=xleplgq3 |  |
| https://leetcode.com/problems/count-of-range-sum/description/?envType=list&envId=xleplgq3 |  |

### Week 5 - Arrays - Stack

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/valid-parentheses/description/ |  |
| https://leetcode.com/problems/maximum-subarray-min-product/description/ |  |
| https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/ |  |
| https://leetcode.com/problems/merge-intervals/description/ |  |
| https://leetcode.com/problems/maximum-frequency-stack/description/ |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/daily-temperatures/description/  |  |
| https://leetcode.com/problems/asteroid-collision/description/ |  |
| https://leetcode.com/problems/next-greater-element-ii/description/ |  |
| https://leetcode.com/problems/132-pattern/description/ |  |
| https://leetcode.com/problems/largest-rectangle-in-histogram/description/ |  |
| https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/ |  |

### Week 6 - Arrays - Greedy

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/gas-station/description/ |  |
| https://leetcode.com/problems/largest-number/description/ |  |
| https://leetcode.com/problems/remove-duplicate-letters/description/ |  |
| https://leetcode.com/problems/remove-k-digits/description/ |  |
| https://leetcode.com/problems/integer-replacement/description/ |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/longest-palindrome/description/ |  |
| https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/ |  |
| https://leetcode.com/problems/valid-triangle-number/description/ |  |
| https://leetcode.com/problems/increasing-triplet-subsequence/description/ |  |
| https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/ |  |

### Week 7 - Trees - BFS

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/minimum-depth-of-binary-tree/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/?envType=list&envId=xlepfebm |  |

| Practice & apply | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=list&envId=xlepfebm |  |
| https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=list&envId=xlepfebm |  |

### Weeks 8 - 10 Trees - DFS

| Study solutions | Retrospection notes |
| --- | --- |
| https://leetcode.com/problems/same-tree/description/ |  |
| https://leetcode.com/problems/merge-two-binary-trees/description/ |  |
| https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/ |  |
| https://leetcode.com/problems/path-sum/description/ |  |
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