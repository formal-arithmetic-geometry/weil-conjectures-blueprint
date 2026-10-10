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

## Proof

Applying $g^{-1}Rf_*$ and $Rf'_*g'^{-1}$ to the distinguished triangle
$F_1\to F\to F_2\to F_1[1]$ defined by the short exact sequence produces two long
exact cohomology sequences (the functors are triangulated and $g^{-1}$ is
exact). Naturality of the derived exchange morphism, as in
[lemma-weil-pbc-derived-exchange-replacement], makes the maps $\Ex^q$ a morphism
between these sequences; compatibility with the connecting maps holds because
$\Ex_\square$ is a natural transformation of triangulated functors, or
concretely by the connecting-homomorphism construction from an injective
resolution of [def-weil-pbc-derived-exchange]. The terms adjacent to
$g^{-1}R^qf_*F$ are
$g^{-1}R^{q-1}f_*F_2\to g^{-1}R^qf_*F_1\to g^{-1}R^qf_*F\to g^{-1}R^qf_*F_2\to
g^{-1}R^{q+1}f_*F_1$, and similarly for the target; if the exchange maps at
$F_1$ and $F_2$ are isomorphisms in all degrees, the five lemma shows that
$\Ex^q_{\square,F}$ is an isomorphism. The other two cases are the same
argument with the five consecutive terms centred at $g^{-1}R^qf_*F_1$
(neighbours $R^{q-1}f_*F$, $R^{q-1}f_*F_2$, $R^qf_*F$, $R^qf_*F_2$) or at
$g^{-1}R^qf_*F_2$ (neighbours $R^qf_*F_1$, $R^qf_*F$, $R^{q+1}f_*F_1$,
$R^{q+1}f_*F$).
