+++
id = "prop-weil-purity-compatibility"
kind = "theorem"
title = "Frobenius compatibility of smooth purity"
order = 90
tags = ["latex:proposition"]
uses = ["def-frobenius-on-twists", "def-weil-exceptional-pullback-object", "def-weil-finite-coefficient-datum", "def-weil-pullback-object", "prop-smooth-purity"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $\Lambda\in\{E,\Qlb\}$,
let $f_0:X_0\to Y_0$ be a smooth morphism of pure relative dimension
$r$ between finite-type $k_0$-schemes, with
geometric fiber $f:X\to Y$, assume that $f$ is
exceptional-adjoint admissible at $\Lambda$, and let
$(L,\theta_L)$ be a derived Weil
object with $L\in D^b_{ctf}(Y,\Lambda)$. The purity isomorphism
has source $Rf^!L$, target $Lf^*L(r)[2r]$, and satisfies

$$
\operatorname{pur}_f(L)\circ\theta_{Rf^!L}
=\theta_{Lf^*L(r)[2r]}\circ Lg_X^*(\operatorname{pur}_f(L)).
$$

The Tate factor in the target contributes the geometric-Frobenius scalar
$q^{-r}$; this scalar is exactly the one in the purity orientation.
