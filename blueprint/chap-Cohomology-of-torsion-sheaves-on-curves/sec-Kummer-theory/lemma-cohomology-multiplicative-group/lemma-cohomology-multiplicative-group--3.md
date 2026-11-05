+++
id = "lemma-cohomology-multiplicative-group--3"
kind = "lemma"
title = "Naturality under restriction"
order = 1571004
aliases = ["bp-r490-3"]
lean = ["AlgebraicGeometry.Scheme.etaleRestrictionH_toCohomologicalPicardGroup"]
uses = ["lemma-cohomology-multiplicative-group--1"]
+++
Let $f:X\to Y$ be an étale monomorphism of schemes. Under the Picard
identification [lemma-cohomology-multiplicative-group--1], restriction of
cohomology classes agrees with pullback of line bundles:
$$
f^*[\operatorname{Isom}(\mathcal O_Y,\mathcal L)]
=[\operatorname{Isom}(\mathcal O_X,f^*\mathcal L)]
\quad\text{in }H^1(X_{\acute{e}t},\mathbf G_m).
$$
In particular this applies to an open immersion $U\hookrightarrow C$.
