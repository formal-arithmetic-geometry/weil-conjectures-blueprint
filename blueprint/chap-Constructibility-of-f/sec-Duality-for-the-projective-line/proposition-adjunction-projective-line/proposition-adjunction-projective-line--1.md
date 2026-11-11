+++
id = "proposition-adjunction-projective-line--1"
kind = "proposition"
title = "The projective-line adjunction"
order = 554002
aliases = ["bp-r167-1"]
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction"]
uses = ["definition-derived-base-change-map", "lemma-cohomology-projective-line-trace", "definition-small-pro-etale-site--1", "definition-constructible-sheaves--6", "definition-underived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--2", "proposition-forgetting-supports-composition--3", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Let $S$ be of finite type over $k$, and let $p:\mathbf P^1_S\to S$ be the
projection. The functors
$Rp_*:D_{\mathrm{class}}((\mathbf P^1_S)_{\mathrm{pro}\acute{e}t},\Lambda)\to
D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$ and
$p^*(1)[2]:D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)\to
D_{\mathrm{class}}((\mathbf P^1_S)_{\mathrm{pro}\acute{e}t},\Lambda)$ form
an adjunction

$$
Rp_* \ \dashv\ p^*(1)[2],
\tag{6.9}
$$

with unit (6.7) and counit (6.8).
