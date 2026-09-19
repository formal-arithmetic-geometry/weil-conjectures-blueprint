+++
id = "prop-weil-cup-product-compatibility"
kind = "theorem"
title = "Frobenius compatibility of cup product"
order = 94
tags = ["latex:proposition"]
uses = ["def-ordinary-cup-product-transformation", "def-weil-direct-image-object", "def-weil-finite-coefficient-datum", "def-weil-pullback-object", "def-weil-tensor-object"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $\Lambda\in\{E,\Qlb\}$,
and let $Y_0$ be of finite type over $k_0$, with geometric fiber
$Y$. For derived Weil objects $(K,\theta_K)$ and
$(L,\theta_L)$ in $D^b_c(Y,\Lambda)$, the cup-product arrow

$$
\smile:\RGamma(Y,K)\otimes^L\RGamma(Y,L)
\longrightarrow\RGamma(Y,K\otimes^LL)
$$

satisfies

$$
\smile\circ\theta_{\RGamma K\otimes\RGamma L}
=\theta_{\RGamma(K\otimes L)}\circ Lg_{\Spec k}^*(\smile).
$$
