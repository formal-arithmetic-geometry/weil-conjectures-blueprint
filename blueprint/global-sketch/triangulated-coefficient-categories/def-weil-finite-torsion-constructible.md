+++
id = "def-weil-finite-torsion-constructible"
kind = "definition"
title = "Finite-torsion constructibility"
order = 8
uses = ["def-weil-finite-coefficient-datum", "def-weil-small-proetale-site"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ as in
Definition [def-weil-finite-coefficient-datum].
For every $n\geq1$, a sheaf of modules over the constant ring sheaf
$(\mathcal O_E/\varpi_E^n)_Y$ on $Y_{\mathrm{proet}}$ is
*constructible* if $Y$ has a finite partition by constructible locally
closed subschemes on each of which the sheaf is locally constant with finite
$\mathcal O_E/\varpi_E^n$-module stalks. The category

$$
D^b_c\bigl(Y,\mathcal O_E/\varpi_E^n\bigr)
\subset
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)
$$

is the full triangulated subcategory of complexes with finitely many nonzero
cohomology sheaves, all constructible.
