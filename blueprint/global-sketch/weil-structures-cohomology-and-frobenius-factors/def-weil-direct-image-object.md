+++
id = "def-weil-direct-image-object"
kind = "definition"
title = "Direct image of a derived Weil object"
order = 82
uses = ["def-derived-direct-image", "def-derived-weil-object", "def-direct-image-exchange", "def-weil-finite-coefficient-datum", "prop-direct-image-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and let
$\Lambda\in\{E,\Qlb\}$. Let $f_0:X_0\to Y_0$ be a separated
finite-type morphism between finite-type $k_0$-schemes, and let
$f:X\to Y$ be its geometric fiber.
The Frobenius square for $f_0$ is Cartesian and the direct-image exchange
of Definition [def-direct-image-exchange] has the specialized form

$$
\operatorname{FrEx}_{f,*}:Lg_Y^*Rf_*\xrightarrow{\sim}Rf_*Lg_X^*.
$$

For a derived Weil object $(K,\theta_K)$ with
$K\in D^b_c(X,\Lambda)$, define

$$
\theta_{Rf_*K}:Lg_Y^*Rf_*K
\xrightarrow{\operatorname{FrEx}_{f,*}(K)}Rf_*Lg_X^*K
\xrightarrow{Rf_*(\theta_K)}Rf_*K.
$$
