# Proofs for the gas station problem
*Date*: Sun 2024-06-09

> I'm writing all the proofs out because I heck as don't understand why the $O(n)$ algorithm works. None of these properties are remotely obvious. Yet it does seem the fact the stations are in a cycle might impose some interesting constraints.

> Not sure if any of this generalises to other problems, it's not clear to me why this is greedy other than we just terminate our algorithm when we find one station. Like, where is the "optimal substructure"?

> _Citing my sources_: https://www.youtube.com/watch?v=rf66wlb9aNQ (Found the explanation here took a few listenings to get it, would be quicker to just look at the notation.)

### Set up

Suppose we have $n$ stations in a cycle, each with gas $g_i$ for a cost $c_i$. 


Let $g_{ij}$ and $c_{ij}$ denote the total cost and total gas of traversing clockwise w.l.o.g. from station $i$ to station $j$

### Claim 1
Is about existence/non-existence of solutions. This turns up in the code as an existence check at the start. 

### Claim 1a: $\sum_{i} g_i \geq \sum_{i} c_i \implies \exists j: g_{jj} - c_{jj} \geq 0$

> In English, this says if the total gas available is greater than the total cost, there must exist a starting position $j$ where we can do a cycle. Intuitively this seems like it should be the case, but it's not obvious how to prove this.

Suppose for the purposes of contradiction there exists _no_ starting station where we can traverse a cycle, but 

$$
\sum_{i} g_i \geq \sum_{i} c_i
$$ 

holds.

This means, for any arbitrary starting station $j$ there must be some station $k$ s.t. that the tank becomes negative and for which we can't traverse the link $k - 1$ to $k$ i.e.: 
$$g_{jk} - c_{jk} < 0$$

Now, clearly

$$
\sum_{i} g_i = g_{jk} + g_{kj}
$$

$$
\sum_{i} c_i  = c_{jk} + c_{kj}
$$

But from the assumption about the total gas and total cost, this implies that 

$$
g_{kj} - c_{kj} \geq g_{jk} - c_{jk}
$$

Hence if we start instead at station $k$, we can loop back to station $j$ yet have enough fuel remaining to traverse from $j$ to $k$, which is a contradiction because we assumed this was not possible. 

Therefore there must exist some station $j$ where a route is possible. $\square$


### Claim 1b: $\sum_{i} g_i < \sum_{i} c_i \implies \nexists j: g_{jj} - c_{jj} \geq 0$
> I think this is just as important as the above, but the reference skips this. Basically the point of Claim 1a and 1b is we have some total constraints on solution existence. 

Suppose for the purposes of contradiction that there is a station $j$ s.t. a cycle is possible i.e. 

$$
g_{jj} - c_{jj} \geq 0
$$

Chose some arbitrary station $k$ on the path. Now clearly

$$
\begin{align*}
    g_{jj} = g_{jk} + g_{kj} &= \sum_{i} g_i \\ 
    c_{jj} = c_{jk} + c_{kj} &= \sum_{i} c_i \\ 
\end{align*}
$$

So substituting this back we get

$$
\begin{align*}
    \sum_{i} g_i -\sum_{i} c_i &\geq 0  \\ 
   \sum_{i} g_i &\geq \sum_{i} c_i \\ 
\end{align*}
$$

But this is a contradition. Therefore there cannot exist any such station. $\square$


### Claim 2: If $g_{ij} < c_{ij}$ _only_ at station $j$, then $\forall k \in \{i + 1, ..., j - 1\}, g_{kj} < c_{kj}$
> In English, if the route from $i$ to $j$ at station $j$ fails at the link $j-1$ to $j$, then it should fail for all the intervening stations.

> Actually this is intuitively obvious, the chokepoint is at link $j-1$ to $j$. The problem was in the reference it sounded like it could fail for _any_ intermediate link, not just the last one. Then obviously this is not true, because you just pick an intermediate station after the failed link but before the destination and you could still get a path.

> Ignore the case where there's multiple chokepoints, it's obvious if it fails than the last chokepoint, it'll fail for any destination after that. 

Suppose for the purposes of contradition there is an arbitrary intermediate station $k \in \{i + 1, ..., j - 1\}$ where it _is_ possible to traverse to $j$, yet $g_{ij} < c_{ij}$. 

Now since route is possible from the intermediate station we have: 

$$
    g_{kj} \geq c_{kj}
$$

Also, $g_{kj} = g_{kj-1} + g_{j-1j}$ and $c_{kj} = c_{kj-1} + c_{j-1j}$ but since from the assumption, $j-1$ is reachable from $k$, $g_{kj-1} - c_{kj-1} \geq 0$ we must have 

$$
    g_{j-1j} \geq c_{j-1j}
$$

Since $j$ is not reachable from $i$ (i.e. our assumption $g_{ij} < c_{ij}$) but $j-1$ is (so $g_{ij-1} \geq c_{ij-1}$), and using the fact $g_{ij} = g_{ij-1} + g_{j-1j}$ and similarly with cost, we can derive that:

$$
    g_{j-1j} < c_{j-1j}
$$

But clearly this is a contradiction, so there cannot exist such intermediate station $k$.  $\square$

### Claim 3: $\sum_{i} g_i \geq \sum_{i} c_i$  and $g_{jk} \geq c_{jk}$ $\implies$ $g_{kj} \geq c_{kj}$

> The moral of this is you don't have to check the first part of the array again when looping back, if you know the second half works.

> This is a highly unintuitive property but is the basis of the $O(n)$ solution. Seems like one might converge on it accidentally if you think about the existence of a solution constraint. 

This proof is easy. 

Starting with the constraint, we have

$$
\begin{align*}
\sum_{i} g_i &\geq \sum_{i} c_i \\
g_{jk} + g_{kj} &\geq c_{jk} + c_{kj}
\end{align*}
$$

But from the other assumption $g_{jk} \geq c_{jk}$, this implies that

$$
g_{kj} \geq c_{kj}
$$

As required.  $\square$