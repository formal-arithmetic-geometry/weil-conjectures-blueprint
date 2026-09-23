+++
id = "lemma-weil-pbc-adic-lim-one-zero"
kind = "lemma"
title = "Mittag–Leffler kills the Milnor obstruction"
order = 1823
uses = ["lemma-weil-pbc-adic-mittag-leffler"]
+++
For a countable Mittag–Leffler system $(A_n)$ one has
$\varprojlim{}^1_nA_n=0$. In particular this holds for a tower of finite
abelian groups.

## Proof

Replace $A_n$ by the stable image in $A_n$; this does not change either
$\varprojlim$ or the cokernel description of $\varprojlim{}^1$, and the new
transition maps are surjective. Given $(y_n)\in\prod_nA_n$, choose $x_1$
arbitrarily and then choose $x_{n+1}$ recursively so that
$x_n-t_{n+1,n}(x_{n+1})=y_n$. Thus $1-s$ is surjective on the product and
its cokernel, namely $\varprojlim{}^1A_n$, is zero.
