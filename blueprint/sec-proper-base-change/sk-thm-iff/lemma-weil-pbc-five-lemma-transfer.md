+++
id = "lemma-weil-pbc-five-lemma-transfer"
kind = "lemma"
title = "Five-lemma transfer for exchange"
order = 1089
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_X₂_of_shortExact"]
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-etale-sheaves", "lemma-weil-pbc-derived-exchange-replacement", "lemma-weil-pbc-prime-factor-induction"]
+++
Let $\Lambda$ be a commutative ring, let $\square$ be a cartesian square as in
[def-weil-pbc-derived-exchange], and for a sheaf $E$ of $\Lambda$-modules on
$X_{\Et}$ and $q\in\mathbf Z$ write

$$
 \Ex^q_{\square,E}:g^{-1}R^qf_*E\longrightarrow R^qf'_*g'^{-1}E
$$

for the map induced on $q$-th cohomology sheaves by the exchange morphism of
[def-weil-pbc-derived-exchange] at $E$ placed in degree $0$. Let
$0\to F_1\to F\to F_2\to0$ be a short exact sequence of sheaves of
$\Lambda$-modules on $X_{\Et}$ (for instance torsion sheaves
[def-weil-pbc-etale-sheaves]). Then the maps $\Ex^q$ form a morphism between the
two long exact sequences of higher direct images, and if $\Ex^q_{\square,F_1}$
and $\Ex^q_{\square,F_2}$ are isomorphisms for every $q$, then so is
$\Ex^q_{\square,F}$ for every $q$. More generally, if two of the three families
$(\Ex^q_{\square,F_1})_q$, $(\Ex^q_{\square,F})_q$, $(\Ex^q_{\square,F_2})_q$
consist of isomorphisms, then so does the third.
