+++
id = "prop-weil-duality-compatibility"
kind = "theorem"
title = "Frobenius compatibility of Verdier duality"
order = 91
tags = ["latex:proposition"]
uses = ["def-verdier-duality-functor", "def-weil-compact-support-object", "def-weil-direct-image-object", "def-weil-finite-coefficient-datum", "def-weil-internal-hom-object", "prop-verdier-duality"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $\Lambda\in\{E,\Qlb\}$,
and let $Y_0$ be of finite type over $k_0$, with geometric fiber
$Y$ and exceptional-adjoint admissible structure morphism
$a_Y:Y\to\Spec k$. For a derived Weil object
$(K,\theta_K)$ with $K\in D^b_{ctf}(Y,\Lambda)$, equip
$\omega_Y=Ra_Y^!\Lambda$ with the structure induced by exceptional
pullback. The internal-Hom formula gives $D_YK$ its derived Weil object
structure. Biduality $b_K:K\to D_YD_YK$ satisfies

$$
b_K\circ\theta_K
=\theta_{D_YD_YK}\circ Lg_Y^*(b_K).
$$

Moreover, for every separated finite-type map $f_0:X_0\to Y_0$, with
geometric fiber $f:X\to Y$, such that $a_X=a_Y\circ f$ is
exceptional-adjoint admissible, and every derived Weil object
$(K,\theta_K)$ with $K\in D^b_{ctf}(X,\Lambda)$, the duality exchange
$\delta_f:D_YRf_!K\to Rf_*D_XK$ satisfies

$$
\delta_f\circ\theta_{D_YRf_!K}
=\theta_{Rf_*D_XK}\circ Lg_Y^*(\delta_f).
$$
