+++
id = "def-nagata-directed-finite-upper-bound"
kind = "definition"
title = "Selected upper bound of a finite set"
order = 335
lean = ["Finset.directedBound"]
+++
Let $I$ be a preorder. Fix a base point $i_\varnothing$
and, for each pair $(i,j)$, fix a selected common upper bound $d(i,j)$,
so $i\leq d(i,j)$ and $j\leq d(i,j)$. For a finite subset $F\subseteq I$
fix an enumeration $F=\{i_1,\ldots,i_n\}$ without repetitions and define
$u(F)\in I$ by inserting the elements of $F$ one at a time in this order:

$$
u_0=i_\varnothing,
\qquad
u_k=d(u_{k-1},i_k)\quad(1\leq k\leq n),
\qquad
u(F)=u_n.
$$

Since $d$ need not be commutative or associative, $u(F)$ depends on the
fixed enumeration.
