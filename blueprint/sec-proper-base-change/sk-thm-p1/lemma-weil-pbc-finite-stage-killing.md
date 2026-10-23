+++
id = "lemma-weil-pbc-finite-stage-killing"
kind = "lemma"
title = "Finite-stage killing of a class"
lean = ["AlgebraicGeometry.Etale.exists_cohomologyMap_eq_zero_of_isLimit"]
order = 1604
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-etale-cohomology-continuity"]
+++
Let $S$ be a scheme, $(D_j)_{j\in J}$ a cofiltered system of quasi-compact
quasi-separated schemes over $S$ with structure maps $\pi_j:D_j\to S$ and
affine transition morphisms, and let $X=\varprojlim_jD_j$ with projections
$p_j:X\to D_j$. Let $G$ be an abelian sheaf on $S_{\Et}$ and
$c\in H^q(S,G)$. If the pullback of $c$ along $\pi_{j_0}\circ p_{j_0}:X\to S$
vanishes for some $j_0$, then there is $j$ such that already the pullback of
$c$ to $D_j$ vanishes.

(In the application, $(T,T_0)$ is an affine henselian pair, the $D_j$ are the
closed fibres of a system of finite, finitely presented covers $T_\lambda\to T$
whose limit is an integral strictly local cover, and $c$ is a class on $T_0$.)
