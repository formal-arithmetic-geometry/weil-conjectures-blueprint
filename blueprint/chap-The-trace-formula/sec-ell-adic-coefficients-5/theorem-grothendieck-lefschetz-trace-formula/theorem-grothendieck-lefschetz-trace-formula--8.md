+++
id = "theorem-grothendieck-lefschetz-trace-formula--8"
kind = "theorem"
title = "Alternating cohomological trace over a field"
order = 1018016
aliases = ["bp-r311-8"]
lean = ["AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq", "AlgebraicGeometry.WeilSheaf.sum_trace_compactlySupportedCohomology"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-weil-structure--1", "definition-weil-structure--3", "theorem-grothendieck-lefschetz-trace-formula--6", "definition-trace-function--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1"]
+++
For $\Lambda=\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell$, it reads

$$
\sum_i(-1)^i\operatorname{Tr}
\bigl(\operatorname{Frob}_{X,K}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}\sum_j(-1)^j
\operatorname{Tr}\bigl(\operatorname{Frob}_{y,m}\mid H^j(K_{\bar y})\bigr),
\tag{12.4}
$$

where all sums over degrees are finite.
