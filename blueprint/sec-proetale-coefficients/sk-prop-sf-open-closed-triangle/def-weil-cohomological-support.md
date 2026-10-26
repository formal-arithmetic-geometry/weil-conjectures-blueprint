+++
id = "def-weil-cohomological-support"
kind = "definition"
title = "Cohomological support"
order = 1079
lean = ["DerivedCategory.cohomologicalSupport"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-pbc-proetale-site"]
+++
Let $\mathcal C$ be an abelian category and $K\in D(\mathcal C)$, with cohomology objects
$\mathcal H^r(K)$ for the standard t-structure; the case of interest is a complex of sheaves on
the small pro-etale site [def-weil-pbc-proetale-site], with its cohomology sheaves
[def-weil-derived-cohomology-sheaves]. The *cohomological support* of $K$ is the set of degrees
in which the cohomology does not vanish:

$$
 \operatorname{Supp}_{\mathrm{coh}}(K)
 =\{r\in\mathbf Z:\mathcal H^r(K)\neq0\}.
$$
