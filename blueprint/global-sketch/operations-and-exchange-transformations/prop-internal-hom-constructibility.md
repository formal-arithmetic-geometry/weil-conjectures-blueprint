+++
id = "prop-internal-hom-constructibility"
kind = "theorem"
title = "Internal-Hom constructibility and coefficient comparison"
order = 64
tags = ["latex:proposition"]
uses = ["def-derived-internal-hom", "def-finite-reduction", "def-finite-tor-amplitude", "def-weil-finite-coefficient-datum", "prop-ramified-coefficient-change", "thm-qbar-functor-descent"]
+++
Fix a scheme $Y$, an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. At every coefficient level, derived
internal Hom restricts to

$$
D^b_{ctf}(Y,\Lambda)^{\mathrm{op}}\times D^b_c(Y,\Lambda)
\longrightarrow D^b_c(Y,\Lambda).
$$

For integral $M,N$ with $M$ of finite Tor amplitude,

$$
\operatorname{red}_{Y,n}R\mathcal Hom_{\widehat{\mathcal O}_{E,Y}}(M,N)
\xrightarrow{\sim}
R\mathcal Hom_{(\mathcal O_E/\varpi_E^n)_Y}
\bigl(\operatorname{red}_{Y,n}M,\operatorname{red}_{Y,n}N\bigr).
$$

The comparison commutes with ramified cofinal reindexing and common-stage
descent.
