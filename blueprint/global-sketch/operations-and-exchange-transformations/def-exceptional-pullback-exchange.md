+++
id = "def-exceptional-pullback-exchange"
kind = "definition"
title = "Exceptional-pullback exchange"
order = 60
uses = ["def-compact-support-exchange", "def-derived-pullback", "def-direct-image-exchange", "def-exceptional-inverse-image", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. Assume that $f$ and $f'$ in the
Cartesian square of Definition
[def-direct-image-exchange] are exceptional-adjoint admissible and that
$\operatorname{Ex}_!$ is invertible. The mate of
$\operatorname{Ex}_!^{-1}:Rf'_!Lg'^*\to Lg^*Rf_!$ under
$Rf_!\dashv Rf^!$ and $Rf'_!\dashv Rf'^!$ is

$$
\operatorname{Ex}^{!}:Lg'^*Rf^!\longrightarrow Rf'^!Lg^*.
$$

Its component at $L\in D^b_c(Y,\Lambda)$ is the unique arrow whose
adjoint is

$$
Rf'_!Lg'^*Rf^!L
\xrightarrow{\operatorname{Ex}_!^{-1}}
Lg^*Rf_!Rf^!L
\xrightarrow{Lg^*(\epsilon_f)}Lg^*L.
$$
