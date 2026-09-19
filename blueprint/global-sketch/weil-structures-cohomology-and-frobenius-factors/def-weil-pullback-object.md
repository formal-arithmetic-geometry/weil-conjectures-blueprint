+++
id = "def-weil-pullback-object"
kind = "definition"
title = "Pullback of a derived Weil object"
order = 79
uses = ["def-derived-pullback", "def-derived-weil-object", "def-weil-finite-coefficient-datum", "prop-pullback-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and let
$\Lambda\in\{E,\Qlb\}$. Let $f_0:X_0\to Y_0$ be a separated
finite-type morphism between finite-type $k_0$-schemes, and let
$f:X\to Y$ be its geometric fiber. The identity
$f\circ g_X=g_Y\circ f$ gives

$$
\beta_{f}^{*}:Lg_X^*Lf^*\xrightarrow{\sim}Lf^*Lg_Y^*.
$$

For a derived Weil object $(K,\theta_K)$ with
$K\in D^b_c(Y,\Lambda)$, the specified structure on $Lf^*K$ is

$$
\theta_{Lf^*K}:Lg_X^*Lf^*K
\xrightarrow{\beta_f^*}Lf^*Lg_Y^*K
\xrightarrow{Lf^*(\theta_K)}Lf^*K.
$$
