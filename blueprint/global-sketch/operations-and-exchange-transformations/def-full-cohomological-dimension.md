+++
id = "def-full-cohomological-dimension"
kind = "definition"
title = "Full cohomological dimension"
order = 52
uses = ["def-derived-direct-image", "def-weil-finite-coefficient-datum", "def-weil-small-proetale-site"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let $n\geq1$, and
let $p:\overline X\to Y$ be proper. Write
$\operatorname{FullCD}(p,\mathcal O_E/\varpi_E^n;c)$ if an integer
$c\geq0$ satisfies

$$
R^qp_*\mathcal F=0\qquad\text{for every integer }q>c
$$

for every sheaf $\mathcal F$ of
$(\mathcal O_E/\varpi_E^n)_{\overline X}$-modules. For every
$U\to Y$ in the small pro-etale site and every integer $q>c$, the same
integer gives $R^q(p_U)_*\mathcal F_U=0$ for every sheaf on
$\overline X\times_YU$.
