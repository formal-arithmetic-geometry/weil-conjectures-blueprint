+++
id = "def-weil-exceptional-pullback-object"
kind = "definition"
title = "Exceptional pullback of a derived Weil object"
order = 84
uses = ["def-derived-weil-object", "def-exceptional-inverse-image", "def-exceptional-pullback-exchange", "def-weil-finite-coefficient-datum", "prop-exceptional-pullback-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and let
$\Lambda\in\{E,\Qlb\}$. Let $f_0:X_0\to Y_0$ be a separated
finite-type morphism between finite-type $k_0$-schemes, with geometric
fiber $f:X\to Y$, and assume
$f$ is exceptional-adjoint admissible at $\Lambda$. The Frobenius specialization
of Definition [def-exceptional-pullback-exchange] is

$$
\operatorname{FrEx}_{f}^{!}:Lg_X^*Rf^!\xrightarrow{\sim}Rf^!Lg_Y^*.
$$

For a derived Weil object $(L,\theta_L)$ with
$L\in D^b_c(Y,\Lambda)$, define

$$
\theta_{Rf^!L}:Lg_X^*Rf^!L
\xrightarrow{\operatorname{FrEx}_{f}^{!}(L)}Rf^!Lg_Y^*L
\xrightarrow{Rf^!(\theta_L)}Rf^!L.
$$
