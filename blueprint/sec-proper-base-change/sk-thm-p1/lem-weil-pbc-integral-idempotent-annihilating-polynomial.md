+++
id = "lem-weil-pbc-integral-idempotent-annihilating-polynomial"
kind = "lemma"
title = "An integral lift of an idempotent mod IB is a root of a monic polynomial congruent to x^d(x-1)^d"
lean = ["Polynomial.exists_monic_aeval_eq_zero_map_eq_of_isIdempotentElem_quotient"]
order = 1940
+++
Let $A$ be a commutative ring, $I\subseteq A$ an ideal and $A\to B$ a ring map with $B$ integral over $A$. Let $b\in B$ be an element whose image in $B/IB$ is idempotent. Then there are an integer $d\ge1$ and a monic polynomial $f\in A[x]$ with $f(b)=0$ in $B$ and $f\equiv x^d(x-1)^d$ modulo $I$, i.e. the image of $f$ in $(A/I)[x]$ is $x^d(x-1)^d$.
