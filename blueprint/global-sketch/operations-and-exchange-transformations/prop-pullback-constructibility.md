+++
id = "prop-pullback-constructibility"
kind = "theorem"
title = "Pullback constructibility and coefficient comparison"
order = 62
tags = ["latex:proposition"]
uses = ["def-derived-pullback", "def-finite-reduction", "def-weil-finite-coefficient-datum", "prop-ramified-coefficient-change", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. For every morphism $f:X\to Y$, derived
pullback restricts at each
coefficient level to

$$
Lf^*:D^b_c(Y,\Lambda)\longrightarrow D^b_c(X,\Lambda).
$$

For $K\in D^b_c(Y,\mathcal O_E)$, the canonical comparison is

$$
\operatorname{red}_{X,n}(Lf^*K)
\xrightarrow{\sim}f_n^*\operatorname{red}_{Y,n}(K).
$$

For every finite extension $L/E$ inside $\Qlb$, with ramification
index $e$, completed scalar extension carries this comparison to the
corresponding one over $L$, with the cofinal reindex $n\mapsto en$;
common-stage descent gives the $\Qlb$-statement.
