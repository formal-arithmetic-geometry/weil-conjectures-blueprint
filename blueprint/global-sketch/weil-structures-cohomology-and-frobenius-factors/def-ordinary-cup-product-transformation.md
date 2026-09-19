+++
id = "def-ordinary-cup-product-transformation"
kind = "definition"
title = "Ordinary cup-product transformation"
order = 93
uses = ["def-cohomology-complexes", "def-derived-direct-image", "def-derived-pullback", "def-derived-tensor-product", "def-point-fiber-functor", "def-weil-finite-coefficient-datum", "prop-pullback-direct-image-adjunction", "prop-tensor-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. For the structure morphism
$a_Y:Y\to s=\Spec k$ and
$K,L\in D^b_{ctf}(Y,\Lambda)$, define

$$
\smile_{K,L}:\RGamma(Y,K)\otimes^L\RGamma(Y,L)
\longrightarrow\RGamma(Y,K\otimes^LL)
$$

as the arrow corresponding under $La_Y^*\dashv Ra_{Y*}$ to

$$
La_Y^*(Ra_{Y*}K\otimes^LRa_{Y*}L)
\xrightarrow{\sim}La_Y^*Ra_{Y*}K\otimes^LLa_Y^*Ra_{Y*}L
\xrightarrow{\epsilon_K\otimes\epsilon_L}K\otimes^LL.
$$

Apply $\operatorname{Fib}_{s,\Lambda}$ to the resulting arrow on the point. This
is the lax-monoidal ordinary direct-image construction; it does not use
compact support.
