+++
id = "lemma-frobenius-fixed-scheme--3"
kind = "lemma"
title = "Reducedness"
order = 959004
aliases = ["bp-r292-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.exists_isOpenImmersion_rationalPoint_of_isLimit"]
uses = ["definition-correspondence", "definition-frobenius-correspondences-their-operators"]
+++
Lean bypasses a separate reducedness lemma by describing each point of the
fixed scheme as an open copy of $s$.

Let $k_0=\Fq$, let $k$ be an algebraically closed extension of $k_0$, and
let $X=X_0\times_{k_0}k$ be locally of finite type over $k$. For the
model Frobenius $\Phi_X$ and $m\geq1$, let $T\to X$ be any equalizer
of $\id_X$ and $\Phi_X^m$ over $s=\Spec k$.

For every point $z\in T$, there is a $k$-rational open immersion
$s\to T$ with image $\{z\}$. In particular, $T$ is reduced.
