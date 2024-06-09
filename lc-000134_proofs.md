# Proofs 
> I'm writing all the proofs out because I heck as don't understand why the $O(n)$ algorithm works. 

Suppose we have $n$ stations in a cycle, each with gas $g_i$ for a cost $c_i$. 


Let $g_{ij}$ and $c_{ij}$ denote the total cost and total gas of traversing clockwise w.l.o.g from station $i$ to station $j$

### Claim 1: $\sum_{i} g_i \geq \sum_{i} c_i \implies \exists j: g_{jj} - c_{jj} \geq 0$

> In English, this says if the total gas available is greater than the total cost, there must exist a starting position $j$ where we can traverse a cycle. 

Suppose for the purposes of contradiction that 
$$\sum_{i} g_i \geq \sum_{i} c_i$$ 

but there exists no such starting position where we can traverse the cycle.

This means, for any arbitrary starting position $j$ there must be some station $k$ s.t. that the tank becomes negative and for which we can't traverse the link $k - 1$ to $k$ i.e.: 
$$g_{jk} - c_{jk} < 0$$

Now, clearly

$$\sum_{i} g_i = g_{jk} + g_{kj}$$
$$\sum_{i} c_i  = c_{jk} + c_{kj}$$

But from the assumption about the total gas and total cost, this implies that 
$$
g_{kj} - c_{kj} \geq g_{jk} - c_{jk}
$$
So if we start a station $k$, we can loop back to station $j$ yet have enough fuel remaining to traverse from $j$ to $k$, which is a contradiction because we assumed this was not possible. 

Therefore there must exist some station $j$ where a route is possible. $\square$


