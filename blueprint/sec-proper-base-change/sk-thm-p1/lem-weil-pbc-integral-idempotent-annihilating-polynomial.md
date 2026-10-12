+++
id = "lem-weil-pbc-integral-idempotent-annihilating-polynomial"
kind = "lemma"
title = "An integral lift of an idempotent mod IB is a root of a monic polynomial congruent to x^d(x-1)^d"
lean = ["Polynomial.exists_monic_aeval_eq_zero_map_eq_of_isIdempotentElem_quotient"]
source = "literature/stacks-project/more-algebra.tex, More on Algebra, Lemma Tag 09XG (lemma-helper-integral) and its proof (uses Algebra, Lemma Tag 00H5, lemma-integral-integral-over-ideal: an element of IB is a root of a monic polynomial with non-leading coefficients in I)"
+++
Let $A$ be a commutative ring, $I\subseteq A$ an ideal and $A\to B$ a ring map with $B$ integral over $A$. Let $b\in B$ be an element whose image in $B/IB$ is idempotent. Then there are an integer $d\ge1$ and a monic polynomial $f\in A[x]$ with $f(b)=0$ in $B$ and $f\equiv x^d(x-1)^d$ modulo $I$, i.e. the image of $f$ in $(A/I)[x]$ is $x^d(x-1)^d$.
