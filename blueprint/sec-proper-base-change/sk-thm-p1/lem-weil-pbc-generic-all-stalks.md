+++
id = "lem-weil-pbc-generic-all-stalks"
kind = "lemma"
title = "Propagation of generic vanishing to all geometric stalks"
uses = ["def-constructible-locally-constant", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Scheme.all_sheafFiber_map_eq_zero_of_generic"]
order = 1801
+++
Let $X$ be an irreducible scheme with generic point $\eta$, and $\Lambda$ a commutative ring. Let $F$ and $G$ be sheaves of $\Lambda$-modules on the small etale site of $X$ [def-weil-pbc-etale-site], with $G$ locally constant [def-constructible-locally-constant], and let $\varphi:F\to G$ be a morphism such that for every separably closed field $\Omega$ and every geometric point $s:\operatorname{Spec}\Omega\to X$ whose image is $\eta$ the induced map of stalks $\varphi_s:F_s\to G_s$ [def-weil-pbc-geometric-stalks] is zero. Then $\varphi_s=0$ for every separably closed field $\Omega$ and every geometric point $s:\operatorname{Spec}\Omega\to X$. No finiteness assumption is made.
