+++
id = "def-global-geometric-frobenius"
kind = "definition"
title = "Global geometric Frobenius"
order = 89
uses = ["def-cohomology-complexes", "def-derived-weil-object", "def-weil-compact-support-object", "def-weil-direct-image-object", "def-weil-finite-coefficient-datum", "def-weil-frobenius"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $Y_0$ be separated and of
finite type over $k_0$, with geometric fiber $Y$, and let
$\Lambda\in\{E,\Qlb\}$. For a derived Weil object
$(K,\theta_K)$ with $K\in D^b_c(Y,\Lambda)$, define the ordinary geometric
Frobenius endomorphism by

$$
\RGamma(Y,K)\xrightarrow{\sim}\RGamma(Y,Lg_Y^*K)
\xrightarrow{\RGamma(\theta_K)}\RGamma(Y,K),
$$

and define the compactly supported operator from the specified structure on
$Ra_{Y!}K$ of Definition [def-weil-compact-support-object]. Their
actions on cohomology are also denoted $F$.
