+++
kind  = "proof"
of    = "lem-fet-locally-trivial"
+++
Step 1: the strictly local case. Let $(A,\mathfrak m)$ be a strictly
henselian local ring and $B$ a finite etale $A$-algebra (finite
etale morphisms being those of [def-galois-categories] and
[def-weil-pbc-scheme-conventions]). Then $B$ is
finite locally free over $A$; let $n$ be its rank. The reduction
$B/\mathfrak mB$ is a finite etale algebra over the separably closed
field $A/\mathfrak m$, hence a finite product of copies of that field (a
finite etale algebra over a field is a product of finite separable field
extensions, and over a separably closed field each of these is the field).
Since $A$ is henselian and $B$ is finite over $A$, the $n$ primitive
idempotents of $B/\mathfrak mB$ lift to orthogonal idempotents
$e_1,\dots,e_n\in B$ with sum $1$; the induced $A$-algebra map
$A^n\to B$, $(a_i)\mapsto\sum a_ie_i$, is surjective by Nakayama's
lemma, and both sides are free of rank $n$, so it is an isomorphism.
Step 2: the general case. Let $y\in Y$ and $A=\mathcal O_{Y,\bar y}^{sh}$, the strict henselization, which is the filtered
colimit of the rings of the etale neighbourhoods $U\to Y$ of $y$. By
Step 1 the finite etale $A$-algebra
$B=\Gamma(P\times_Y\operatorname{Spec}A,\mathcal O)$ is isomorphic to
$A^n$. The isomorphism is given by finitely many elements and relations,
so by the standard limit argument for finitely presented data it descends
to an etale neighbourhood: there is a factorization $y\to U\to Y$ with
$U\to Y$ etale and $P\times_YU\cong\coprod_{i=1}^nU$. The last
assertion is immediate, the image of $U\to Y$ containing $y$.
