+++
id = "def-weil-pbc-henselian-terminology"
kind = "definition"
title = "Henselian terminology"
lean = ["HenselianRing", "HenselianLocalRing", "IsStrictlyHenselianLocalRing"]
order = 941
uses = ["def-weil-pbc-scheme-conventions"]
+++
A pair $(A,I)$ consisting of a commutative ring and an ideal is *henselian*
if $I$ is contained in the Jacobson radical of $A$ and, for every monic
polynomial $f\in A[X]$ and every $a_0\in A$ with $f(a_0)\in I$ and $f'(a_0)$ a
unit modulo $I$, there is a root $a\in A$ of $f$ with $a-a_0\in I$.
Equivalently, $I$ is contained in the Jacobson radical and, for every finite
$A$-algebra $B$, every idempotent of $B/IB$ lifts uniquely to an idempotent of
$B$. A local ring is *henselian* when its maximal-ideal pair is henselian, and
*strictly henselian* when it is henselian and its residue field is separably
closed. For $T=\operatorname{Spec}A$ and an ideal $I$, write
$T_0=\operatorname{Spec}(A/I)$ for the closed subscheme.
