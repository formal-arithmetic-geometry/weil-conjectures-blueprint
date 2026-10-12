+++
id = "def-nagata-directed-finite-upper-bound"
kind = "definition"
title = "Selected upper bound of a finite set"
order = 335
+++
Let $I$ be a nonempty directed preorder. Fix a base point $i_\varnothing$
and, for each pair $(i,j)$, fix a selected common upper bound $d(i,j)$,
so $i\leq d(i,j)$ and $j\leq d(i,j)$. For finite subsets $F\subseteq I$
define $u(F)\in I$ by induction on $F$, inserting only an element $i\notin F$:

$$
u(\varnothing)=i_\varnothing,
\qquad
u(F\cup\{i\})=d(u(F),i)\quad(i\notin F).
$$
