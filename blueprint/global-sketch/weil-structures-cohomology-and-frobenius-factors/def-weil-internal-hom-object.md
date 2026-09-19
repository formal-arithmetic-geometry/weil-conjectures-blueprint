+++
id = "def-weil-internal-hom-object"
kind = "definition"
title = "Internal Hom of derived Weil objects"
order = 81
uses = ["def-derived-internal-hom", "def-derived-weil-object", "def-weil-finite-coefficient-datum", "prop-internal-hom-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $Y_0$ be of finite type
over $k_0$ with geometric fiber $Y$, and let
$\Lambda\in\{E,\Qlb\}$. For derived Weil objects
$(K,\theta_K)$, $(L,\theta_L)$ with
$K\in D^b_{ctf}(Y,\Lambda)$ and $L\in D^b_c(Y,\Lambda)$, pullback gives

$$
\beta_{\mathcal H om}:Lg_Y^*R\mathcal Hom(K,L)
\xrightarrow{\sim}R\mathcal Hom(Lg_Y^*K,Lg_Y^*L).
$$

Contravariance in the first variable forces the inverse of $\theta_K$.
Define

$$
\theta_{R\mathcal Hom(K,L)}:=
R\mathcal Hom(\theta_K^{-1},\theta_L)\circ\beta_{\mathcal H om}:
Lg_Y^*R\mathcal Hom(K,L)\xrightarrow{\sim}R\mathcal Hom(K,L).
$$
