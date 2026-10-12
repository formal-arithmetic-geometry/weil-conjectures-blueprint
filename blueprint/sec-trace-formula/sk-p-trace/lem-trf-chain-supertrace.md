+++
id = "lem-trf-chain-supertrace"
kind = "lemma"
title = "Chain-level supertrace computation, with explicit conventions"
order = 2607
uses = ["def-trf-categorical-trace", "def-trf-coefficient-conventions"]
+++
Let $A$ be a commutative ring, let
$P^\bullet=(P^i,d^i)_{i\in\mathbf Z}$ be a bounded complex of finite
projective $A$-modules, and let $v:P^\bullet\to P^\bullet$ be a chain
map. On the model category of bounded complexes of finite projective
$A$-modules use the following *strict* symmetric monoidal
structure (the Koszul convention of
the categorical trace):

1. the tensor product of complexes is the total complex of the
double complex $(P^i\otimes_AQ^j)$, with the differential
$d(p\otimes q)=dp\otimes q+(-1)^{|p|}p\otimes dq$, the unit is
$A$ concentrated in degree $0$, and the associator and unit
isomorphisms are the identity maps;
1. the braiding is
$\operatorname{sym}_{P,Q}(p\otimes q)=(-1)^{|p||q|}q\otimes p$;
1. the dual complex $P^\vee$ is
$(P^\vee)^n=\operatorname{Hom}_A(P^{-n},A)$ with the differential
$$
(d^\vee\varphi)(x):=(-1)^{|\varphi|+1}\varphi(dx),
$$
so that $|e^\vee|=-|e|$ for the dual basis element $e^\vee$ of a
basis element $e$;
1. the evaluation and the coevaluation are
$$
\operatorname{ev}_P(\varphi\otimes p):=\varphi(p),\qquad
\operatorname{coev}_P(1):=\sum_{\alpha}e_\alpha\otimes e_\alpha^\vee,
$$
where $(e_\alpha)$ is a basis of the finite projective $A$-module
$\oplus_iP^i$ (the sum is finite because $P^\bullet$ is bounded, and
is independent of the basis).

Then:

1. **(a)** $\operatorname{ev}_P$ and $\operatorname{coev}_P$ are
chain maps of degree $0$;
1. **(b)** the triangle identities hold:
$$
(\operatorname{ev}_P\otimes1)\circ(1\otimes\operatorname{coev}_P)=1_{P^\vee},\qquad
(1\otimes\operatorname{ev}_P)\circ(\operatorname{coev}_P\otimes1)=1_P;
$$
1. **(c)** the categorical
trace of $v$ is the supertrace of its components,
$$
\operatorname{tr}_A(v\mid P)=
\sum_{i\in\mathbf Z}(-1)^i\operatorname{Tr}\bigl(v^i\mid P^i\bigr),
$$
the sum of the ordinary traces of the components; in particular
$\operatorname{tr}_A(\operatorname{id}_P)=\sum_i(-1)^i\operatorname{rank}_AP^i$,
the Euler characteristic.

Consequently the value depends only on the homotopy, hence the
quasi-isomorphism, class of $v$: it is a well-defined function

$$
\operatorname{tr}_A:\operatorname{End}_{D(A)}(P)\longrightarrow A
$$

on the derived category, which is the categorical trace of
Definition
[def-trf-categorical-trace].
