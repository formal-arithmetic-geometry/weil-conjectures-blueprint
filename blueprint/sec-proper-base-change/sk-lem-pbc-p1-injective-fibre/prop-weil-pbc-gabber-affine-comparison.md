+++
id = "prop-weil-pbc-gabber-affine-comparison"
kind = "theorem"
title = "Gabber affine comparison"
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_of_henselianRing", "AlgebraicGeometry.Etale.affine_closed_etale_neighborhood_comparison"]
order = 1581
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-gabber-effacement", "def-weil-pbc-torsion-etale-sheaf"]
+++
Let $(A,I)$ be a henselian pair [def-weil-pbc-henselian-terminology],
$T=\operatorname{Spec}A$ and $T_0=\operatorname{Spec}(A/I)$, and let $\Lambda$ be a
commutative ring. For every sheaf $F$ of $\Lambda$-modules on $T_{\Et}$ which is
torsion [def-weil-pbc-torsion-etale-sheaf], with restriction $F_0$ to $T_0$,
restriction induces isomorphisms

$$
 H^q(T,F)\xrightarrow{\sim}H^q(T_0,F_0)
 \qquad(q\geq0).
$$

Consequently, if $X$ is an affine scheme, $i:Z\hookrightarrow X$ a closed
immersion and $F$ a torsion sheaf of $\Lambda$-modules on $X_{\Et}$, then there
are a directed system of étale morphisms $v_a:U_a\to X$ with compatible
factorizations $i=v_a\circ s_a$ ($s_a:Z\to U_a$), i.e. étale neighbourhoods of
$Z$, such that the maps $s_a^*$ induce isomorphisms

$$
 \varinjlim_aH^q(U_a,v_a^{-1}F)\xrightarrow{\sim}H^q(Z,i^{-1}F)
 \qquad(q\geq0).
$$

The map $H^q(X,F)\to H^q(Z,i^{-1}F)$ itself need not be an isomorphism: for
$X=\operatorname{Spec}k((t))$, $Z=\emptyset$ and $F=\mathbf Z/n$ one has
$H^0(X,F)=\mathbf Z/n$ while $H^0(Z,i^{-1}F)=0$.
