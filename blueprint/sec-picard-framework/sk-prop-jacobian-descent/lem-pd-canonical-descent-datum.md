+++
id = "lem-pd-canonical-descent-datum"
kind = "lemma"
title = "A representing object carries a canonical descent datum"
lean = ["CategoryTheory.Functor.RepresentableBy.overDescentDatum", "CategoryTheory.Functor.RepresentableBy.overTransport"]
order = 866
uses = ["cor-pd-pic0-base-change", "def-pc-base-change", "def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-pd-descent-datum", "def-pd-separable-closure", "def-sc-jacobian", "lem-pd-descent-cocycle", "thm-pd-geometric-pic0"]
+++
Let $p:X\to Y$ be a morphism of schemes, let $F$ be a presheaf of sets on
the category of schemes over $Y$, and let $V$ be a scheme over $X$ which
represents the restriction of $F$ to schemes over $X$ (a scheme
$f:T\to X$ being regarded as the scheme $p\circ f:T\to Y$ over $Y$). For
$f_1,f_2:T\to X$ with $p\circ f_1=p\circ f_2$, let the *transport*
from the $T$-points of $V$ lying over $f_1$ to those lying over $f_2$ send
a point to the point corresponding to the same element of
$F(T\xrightarrow{p\circ f_1}Y)$. These transports are natural in $T$, are
the identity when $f_1=f_2$, and satisfy the cocycle condition
([lem-pd-descent-cocycle]). They form a descent datum on $V$ over $X/Y$ in
the transport form of [def-pd-descent-datum], and no choice is involved.

In particular, let $k$ be a field, $C$ a smooth projective curve over $k$
([def-pc-smooth-projective-curve]) which is geometrically integral
([def-pc-geometrically-irreducible]), $k_s$ a separable closure of $k$
([def-pd-separable-closure]), $C_s=C_{k_s}$ ([def-pc-base-change]), and
$J_s$ the representing object of $\operatorname{Pic}^0_{C_s/k_s}$ of
[thm-pd-geometric-pic0] ([def-sc-jacobian]). Then $J_s$ carries a
canonical descent datum over $\Spec(k_s)/\Spec(k)$.
