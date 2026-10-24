+++
id = "lem-pur-divisor-class"
kind = "lemma"
title = "Kummer class of a divisor and its $c_1$"
order = 2918
uses = ["def-coefficient-twists-detailed", "def-pur-affine-line-datum", "def-pur-conventions", "def-pur-frame-class", "def-pur-support-cohomology", "def-weil-derived-cohomology-sheaves", "lem-amb-cartier-kummer-map", "lem-pur-frame-independence", "lem-pur-kummer-additivity"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $T\to B$ be smooth of relative dimension $n$ and let
$D\hookrightarrow T$ be a closed subfamily, smooth over $B$, of pure
codimension one. The *Kummer class of the divisor $D$* is the
class $\operatorname{cl}(D)\in H^2_D(T,\Lambda(1))$ of
[def-pur-frame-class] of a frame of the ideal of $D$, well
defined by [lem-pur-frame-independence]. Moreover:

1. *(a)* $\operatorname{cl}(D)|_{U}=\partial(\kappa(f))$ in
$H^2_{D\cap U}(U,\Lambda(1))$ for a local equation $f$ of $D$ on an open $U$.
1. *(b)* Forgetting support sends $\operatorname{cl}(D)$ to
$c_1(\mathcal O_T(-D))=-c_1(\mathcal O_T(D))$. Here $\mathcal O_T(-D)$ is
the ideal sheaf of $D$. Equivalently, the class
$c_D\in H^2_D(T,\Lambda(1))$ of [lem-amb-cartier-kummer-map], built from
$\mathcal O_T(D)$ with its canonical section, is $-\operatorname{cl}(D)$.
1. *(c)* For any two functions $f_1,f_2$ on an open $U$ of $T$, with zero
loci $D_1=V(f_1)$ and $D_2=V(f_2)$ (not necessarily smooth over $B$),

$$
\partial\kappa(f_1f_2)=\partial\kappa(f_1)+\partial\kappa(f_2)
\quad\text{in }H^2_{D_1\cup D_2}(U,\Lambda(1)),
$$

the classes $\partial\kappa(f_i)\in H^2_{D_i}(U,\Lambda(1))$ being mapped
along the extension of supports from $D_i$ to $D_1\cup D_2$. Consequently
$\operatorname{cl}(D_1+D_2)=\operatorname{cl}(D_1)+\operatorname{cl}(D_2)$
whenever $D_1$, $D_2$ and $D_1+D_2$ are all smooth over $B$ of pure
codimension one, so that the three classes are defined.
