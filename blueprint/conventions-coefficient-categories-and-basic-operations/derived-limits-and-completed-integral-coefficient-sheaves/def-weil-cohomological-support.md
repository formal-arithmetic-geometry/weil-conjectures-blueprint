+++
id = "def-weil-cohomological-support"
kind = "definition"
title = "Cohomological support"
order = 1222
lean = ["AlgebraicGeometry.Proetale.cohomologicalSupport"]
uses = ["def-weil-small-proetale-site-detailed", "def-weil-derived-cohomology-sheaves"]
+++
For a complex $K$ of sheaves on the small pro-etale site
[def-weil-small-proetale-site-detailed] with cohomology sheaves
[def-weil-derived-cohomology-sheaves] $\mathcal H^r(K)$, the *cohomological
support* is the set of degrees in which the cohomology does not vanish:

$$
 \operatorname{Supp}_{\mathrm{coh}}(K)
 =\{r\in\mathbf Z:\mathcal H^r(K)\neq0\}.
$$
