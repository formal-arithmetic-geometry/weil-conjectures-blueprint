+++
id = "lem-kun-unbounded-exchange-constructions-agree"
kind = "lemma"
title = "The two constructions of the unbounded exchange morphism agree"
order = 1690
uses = ["def-kun-unbounded-exchange", "def-weil-pbc-derived-exchange", "def-weil-pbc-underived-exchange"]
+++
Let $\square=(f,f',g,g',\alpha)$ be a
cartesian square, $\Lambda$
a commutative ring and $K\in D(X_{\Et},\Lambda)$. The mate
description of $\Ex_{\square,K}$ in
[def-kun-unbounded-exchange] and its description by the termwise
underived exchange morphism of
[def-weil-pbc-underived-exchange] on a K-injective resolution
define the same morphism
$g^{-1}Rf_*K\to Rf'_*g'^{-1}K$.

## Proof

Both descriptions are the adjoint mate, under the derived adjunction
$f'^{-1}\dashv Rf'_*$, of the same composite
$f'^{-1}g^{-1}Rf_*K\to g'^{-1}K$, namely the one displayed in
[def-kun-unbounded-exchange]: the first description is the mate by
definition, and the
second because the termwise underived exchange morphism of
[def-weil-pbc-underived-exchange] on a K-injective resolution is
the mate of that composite, as in the
bounded case [def-weil-pbc-derived-exchange]. An adjunction
bijection is injective, so the two mates agree.
