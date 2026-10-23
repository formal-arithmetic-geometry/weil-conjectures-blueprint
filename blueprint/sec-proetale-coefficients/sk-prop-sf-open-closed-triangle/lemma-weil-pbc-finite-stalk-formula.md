+++
id = "lemma-weil-pbc-finite-stalk-formula"
kind = "lemma"
title = "Geometric stalk formula for finite direct image"
order = 1095
lean = ["AlgebraicGeometry.Etale.lowerStarSheafFiberIsoPi", "AlgebraicGeometry.Etale.stalkRestrict"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-fibre", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-fin-finite-splitting", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $f:X\to Y$ be a finite morphism of schemes, let $\mathcal A$ be a
Grothendieck abelian coefficient category for which presheaves on small etale
sites can be sheafified (for instance abelian groups), and let
$\bar y:\operatorname{Spec}\Omega\to Y$ be a geometric point with $\Omega$
algebraically closed. For an $\mathcal A$-valued etale sheaf $G$ on $X$ and a
geometric point $\bar x$ of the geometric fibre of $f$ over $\bar y$, the
*restriction of stalks* $(f_*G)_{\bar y}\to G_{\bar x}$ sends the germ of a
section of $G$ over $U\times_YX$, for a pointed etale neighbourhood $U$ of
$\bar y$, to its germ at the pointed etale neighbourhood $U\times_YX$ of
$\bar x$. These maps together give an isomorphism

$$
 (f_*G)_{\bar y}\xrightarrow{\sim}
 \prod_{\bar x\in|X_{\bar y}|}G_{\bar x},
$$

natural in $G$, where the product runs over the finite geometric fibre of $f$
over $\bar y$. For a finite set, this product is also the direct sum.
