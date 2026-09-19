+++
id = "def-weil-tensor-object"
kind = "definition"
title = "Tensor product of derived Weil objects"
order = 80
uses = ["def-derived-tensor-product", "def-derived-weil-object", "def-weil-finite-coefficient-datum", "prop-tensor-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $Y_0$ be of finite type
over $k_0$ with geometric fiber $Y$, and let
$\Lambda\in\{E,\Qlb\}$. For derived Weil objects
$(K,\theta_K)$ and $(L,\theta_L)$ with
$K,L\in D^b_{ctf}(Y,\Lambda)$,
monoidality of pullback gives

$$
\beta_{\otimes}:Lg_Y^*(K\otimes^L L)
\xrightarrow{\sim}Lg_Y^*K\otimes^LLg_Y^*L.
$$

Define

$$
\theta_{K\otimes L}:=
(\theta_K\otimes^L\theta_L)\circ\beta_{\otimes}:
Lg_Y^*(K\otimes^LL)\xrightarrow{\sim}K\otimes^LL.
$$
