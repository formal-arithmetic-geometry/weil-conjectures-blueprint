+++
id = "proposition-transitivity-trace-map--1"
kind = "proposition"
title = "Transitivity of the trace map (1)"
name_showing = false
order = 808001
aliases = ["bp-r243-1"]
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace_comp"]
uses = ["definition-derived-base-change-map", "proposition-composition-open-restriction-compactifications-f", "definition-trace-map", "definition-small-pro-etale-site--1", "definition-constructible-sheaves--6", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative
dimensions $d$ and $e$, and $K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$ for any admissible
$\Lambda$. Then
$\operatorname{Tr}_{g\circ f}(K)$ is the composite

$$
\begin{gathered}
R(g\circ f)_!
\bigl((g\circ f)^{*}K(d+e)[2d+2e]\bigr)
\simeq Rg_!Rf_!
\bigl(f^{*}
(g^{*}K(e)[2e])(d)[2d]\bigr)\\
\xrightarrow{\ Rg_!
(\operatorname{Tr}_{f}(g^{*}K(e)[2e]))\ }
Rg_!\bigl(g^{*}K(e)[2e]\bigr)
\xrightarrow{\ \operatorname{Tr}_{g}(K)\ }K.
\end{gathered}
$$
