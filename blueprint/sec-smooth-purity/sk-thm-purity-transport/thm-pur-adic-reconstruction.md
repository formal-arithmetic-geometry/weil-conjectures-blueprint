+++
id = "thm-pur-adic-reconstruction"
kind = "theorem"
title = "Adic reconstruction"
order = 2023
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-derived-complete-integral-detailed", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-weil-pbc-reconstruction-uniform-tower", "thm-pur-finite-coefficient-smooth-purity", "thm-pur-finite-reduction-of-purity"]
+++
Work in the purity conventions of [def-pur-conventions], let
$f:X\to Y$ be smooth separated of relative dimension $d$, and let
$K\in D^b_{ctf}(Y,\mathcal O_E)$ with finite reductions
$K_n\in D^b_{ctf}(Y,A_{E,n})$. The comparisons
$\gamma_{f,K_n}$ of [thm-pur-finite-coefficient-smooth-purity] form a
morphism of normalized systems in the sense of
[def-weil-pbc-adic-coefficient-datum], and they induce an isomorphism

$$
Lf^*K(d)[2d]\xrightarrow{\ \sim\ }Rf^!K
$$

in $D^b_{ctf}(X,\mathcal O_E)$, whose reduction at every level $n$ is
exactly $\gamma_{f,K_n}$.
