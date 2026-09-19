+++
id = "prop-weil-trace-compatibility"
kind = "theorem"
title = "Frobenius compatibility of the trace"
order = 92
tags = ["latex:proposition"]
uses = ["def-weil-compact-support-object", "def-weil-exceptional-pullback-object", "def-weil-finite-coefficient-datum", "prop-exceptional-pullback-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $\Lambda\in\{E,\Qlb\}$,
and let $Y_0$ be of finite type over $k_0$, with geometric fiber
$Y$ and exceptional-adjoint admissible structure morphism
$a_Y:Y\to\Spec k$. The adjunction
counit

$$
\operatorname{tr}_Y:Ra_{Y!}Ra_Y^!\Lambda\longrightarrow\Lambda
$$

has the exact Frobenius equation

$$
\operatorname{tr}_Y\circ\theta_{Ra_{Y!}Ra_Y^!\Lambda}
=\theta_\Lambda\circ Lg_{\Spec k}^*(\operatorname{tr}_Y).
$$
