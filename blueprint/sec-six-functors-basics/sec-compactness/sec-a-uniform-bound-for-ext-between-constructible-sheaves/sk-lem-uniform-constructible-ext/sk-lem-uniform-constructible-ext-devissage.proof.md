+++
kind = "proof"
of = "det-uniform-constructible-ext-devissage"
+++
(1) By induction on $m$. The short exact sequence $0\to C_{m-1}\to C\to C/C_{m-1}\to0$ gives the
long exact sequence

$$
\cdots\to\Ext^q(C/C_{m-1},N)\to\Ext^q(C,N)\to\Ext^q(C_{m-1},N)\to\cdots.
$$

For $q>\max_kc_k$ the outer terms vanish (the left one by hypothesis, the right one by induction), so
the middle one vanishes.

(2) Similarly, from $0\to N_{r-1}\to N\to N/N_{r-1}\to0$ and the sequence
$\Ext^q(C,N_{r-1})\to\Ext^q(C,N)\to\Ext^q(C,N/N_{r-1})$, by induction on $r$; the bound does not
change.

For the consequence: by part (3) of [sk-lem-coefficient-heart], every $C\in\Cons(X,\Lambda)$ has a
finite filtration with subquotients $(a_k)_!L_k$, and every $N\in\Cons(X,\Lambda)$ has one with
subquotients $b_!M$. Put $d_C=\max_kc_{a_k}$; then (2) gives $\Ext^q((a_k)_!L_k,N)=0$ for $q>c_{a_k}$
and every constructible $N$, and (1) gives $\Ext^q(C,N)=0$ for $q>d_C$. The bound depends only on $C$
(through the chosen filtration), not on $N$.
