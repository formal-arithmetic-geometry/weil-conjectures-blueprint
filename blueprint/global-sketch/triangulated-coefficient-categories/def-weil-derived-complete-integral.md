+++
id = "def-weil-derived-complete-integral"
kind = "definition"
title = "Bounded constructible integral category"
order = 13
uses = ["def-derived-complete-integral-object", "def-weil-finite-coefficient-datum", "def-weil-finite-torsion-constructible"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
Define $D^b_c(Y,\mathcal O_E)$ to be the full
triangulated subcategory of derived-complete
$K\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$ such that

$$
\operatorname{red}_{Y,n}(K)
\in D^b_c\bigl(Y,\mathcal O_E/\varpi_E^n\bigr)
$$

for every $n$, and one interval $[r,s]\subset\mathbf Z$, independent of
$n$, contains the cohomological support of every reduction.
