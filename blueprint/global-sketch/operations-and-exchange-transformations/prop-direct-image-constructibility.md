+++
id = "prop-direct-image-constructibility"
kind = "theorem"
title = "Direct-image constructibility and coefficient comparison"
order = 61
tags = ["latex:proposition"]
uses = ["def-derived-direct-image", "def-direct-image-exchange", "def-finite-reduction", "def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum", "prop-finite-proper-base-change", "prop-ramified-coefficient-change", "thm-qbar-functor-descent", "thm-rational-lattice-localization"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. Let $f:X\to Y$ be separated and of
finite type. At each explicitly
constructed coefficient level, derived direct image restricts to

$$
Rf_*:D^b_c(X,\Lambda)\longrightarrow D^b_c(Y,\Lambda).
$$

Here at finite level
$\Lambda=\mathcal O_E/\varpi_E^n$, at the integral level the ambient ring
sheaves are $\widehat{\mathcal O}_{E,X}$ and
$\widehat{\mathcal O}_{E,Y}$, at the rational level they are $E_X$ and
$E_Y$, and the $\Qlb$-statement is represented over one common finite
field. If $K\in D^b_c(X,\mathcal O_E)$, then

$$
\operatorname{red}_{Y,n}(Rf_*K)
\xrightarrow{\sim}Rf_{*,n}\operatorname{red}_{X,n}(K)
$$

for every $n$, and

$$
Rf_*K\xrightarrow{\sim}
R\varprojlim_n\operatorname{Res}_{Y,n}
Rf_{*,n}\operatorname{red}_{X,n}(K).
$$

Reduction carries $\operatorname{Ex}_*(K)$ to the finite-level exchange
component. For every finite extension $L/E$ inside $\Qlb$, with
ramification index $e$, completed scalar extension carries it to the
$L$-coefficient component after the cofinal reindex $n\mapsto en$.
If $f$ is proper, Proposition
[prop-finite-proper-base-change] at finite level and the displayed
comparisons imply that $\operatorname{Ex}_*$ is an isomorphism at every
coefficient level.
If both horizontal maps in the Cartesian square of
Definition [def-direct-image-exchange] are isomorphisms, then
$\operatorname{Ex}_*$ is an isomorphism without a properness assumption;
in particular this applies to every Frobenius square.
