+++
id = "prop-tensor-constructibility"
kind = "theorem"
title = "Tensor constructibility and coefficient comparison"
order = 63
tags = ["latex:proposition"]
uses = ["def-derived-tensor-product", "def-finite-reduction", "def-finite-tor-amplitude", "def-weil-finite-coefficient-datum", "prop-ramified-coefficient-change", "thm-qbar-functor-descent"]
+++
Fix a scheme $Y$, an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. At every coefficient level, derived tensor
product restricts to

$$
D^b_{ctf}(Y,\Lambda)\times D^b_c(Y,\Lambda)
\longrightarrow D^b_c(Y,\Lambda).
$$

For integral $M,N$ with $M$ of finite Tor amplitude,

$$
\operatorname{red}_{Y,n}(M\otimes^L_{\widehat{\mathcal O}_{E,Y}}N)
\xrightarrow{\sim}
\operatorname{red}_{Y,n}(M)
\otimes^L_{(\mathcal O_E/\varpi_E^n)_Y}
\operatorname{red}_{Y,n}(N).
$$

These isomorphisms satisfy the finite-extension tower equation and descend
to the common-stage coefficient category.
