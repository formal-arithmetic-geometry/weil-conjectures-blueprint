+++
id = "def-completed-integral-coefficient-sheaf"
kind = "definition"
title = "Completed integral coefficient sheaf"
order = 9
uses = ["def-weil-finite-coefficient-datum", "def-weil-small-proetale-site"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
The completed coefficient sheaf on $Y_{\mathrm{proet}}$ is the inverse
limit in sheaves of rings

$$
\widehat{\mathcal O}_{E,Y}
=\varprojlim_{n\geq1}(\mathcal O_E/\varpi_E^n)_Y.
$$

Write
$D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$ for the derived
category of sheaves of $\widehat{\mathcal O}_{E,Y}$-modules. Thus the
coefficient in this notation is a ring sheaf, not the discrete ring
$\mathcal O_E$.
