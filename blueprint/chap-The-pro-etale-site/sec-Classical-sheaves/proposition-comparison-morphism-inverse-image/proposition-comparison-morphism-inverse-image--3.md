+++
id = "proposition-comparison-morphism-inverse-image--3"
kind = "proposition"
title = "The comparison morphism and its inverse image (3)"
name_showing = false
order = 112003
aliases = ["bp-r031-3"]
lean = ["AlgebraicGeometry.ProEtale.isColimit_comparisonUpperStar_mapCocone"]
uses = ["proposition-comparison-morphism-inverse-image--2"]
+++
For $X$ and $A$ as in [proposition-comparison-morphism-inverse-image--1],
let $F$ be an $A$-valued étale sheaf on $X$ and let $(U_i)_{i\in I}$ be a
small cofiltered diagram of quasi-compact, quasi-separated étale
$X$-schemes with affine transition maps. Let $U$ be an object of
$X_{\mathrm{pro}\acute{e}t}$ with compatible maps to the $U_i$, and assume
that its underlying cone of schemes is a limit cone.
Then the restriction maps exhibit $(\nu_X^*F)(U)$ as the filtered colimit
of the $(\nu_X^*F)(U_i)$:

$$
\varinjlim_{i\in I^{\mathrm{op}}}(\nu_X^*F)(U_i)
\xrightarrow{\ \sim\ }(\nu_X^*F)(U).
$$
