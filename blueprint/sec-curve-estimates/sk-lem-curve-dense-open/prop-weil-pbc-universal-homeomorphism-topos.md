+++
id = "prop-weil-pbc-universal-homeomorphism-topos"
kind = "theorem"
title = "Topological invariance of the small etale topos"
order = 1516
lean = ["AlgebraicGeometry.Etale.cohomologyEquiv", "AlgebraicGeometry.Etale.cohomologyMap_bijective", "AlgebraicGeometry.Etale.isEquivalence_upperStar", "AlgebraicGeometry.Etale.sheafEquivalence"]
tags = ["latex:proposition"]
uses = ["def-pc-ext", "lemma-constructible-pullback-constant"]
+++
Let $u:X_0\to X$ be a universal homeomorphism. For every coefficient
category $\mathcal A$, restriction along base change (the pushforward
$u_*$) is an equivalence between $\mathcal A$-valued sheaves on
$X_{0,\mathrm{et}}$ and on $X_{\mathrm{et}}$; for $\mathcal A$ Grothendieck
abelian, pullback $u^{-1}$ is an equivalence from sheaves on
$X_{\mathrm{et}}$ to sheaves on $X_{0,\mathrm{et}}$, quasi-inverse to $u_*$.
For every abelian sheaf $F$ on $X_{\mathrm{et}}$ and every $n\ge0$, the map
induced by $u^{-1}$ (and the identification $u^{-1}\mathbf Z\cong\mathbf Z$
of constant sheaves) is an isomorphism

$$
H^n(X_{\mathrm{et}},F)\xrightarrow{\sim}H^n(X_{0,\mathrm{et}},u^{-1}F).
$$
