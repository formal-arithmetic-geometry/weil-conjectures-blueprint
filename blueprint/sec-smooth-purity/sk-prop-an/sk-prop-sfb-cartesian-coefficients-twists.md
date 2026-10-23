+++
id = "det-prop-sfb-cartesian-coefficients-twists"
kind = "lemma"
title = "Inverse image of Tate twists"
order = 2947
uses = ["sk-def-sp-tate-twist", "def-pur-roots-of-unity-sheaf", "det-def-sp-tate-twist-locally-free", "det-prop-sfb-qlbar-colimit-x-pullback", "lem-sfb-alpha-iso"]
+++
Let $f\colon X\to Y$ be a morphism of schemes on which $\ell$ is invertible, and let
$\Lambda\in\{A,\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb\}$ be admissible. There are canonical
isomorphisms
$$
f^{-1}\mu_{\ell^n,Y}\cong\mu_{\ell^n,X},\qquad
f^{-1}\bigl(\Lambda_Y(d)\bigr)\cong\Lambda_X(d)\quad(d\in\mathbf Z),
$$
compatible with the isomorphism $\alpha_f\colon f^{-1}\Lambda_Y\cong\Lambda_X$ of
[lem-sfb-alpha-iso] and the module structures, and with the Kummer transition maps.
Consequently $f^*(K(d))\cong(f^*K)(d)$ for $K\in D(Y_{\mathrm{proét}},\Lambda)$.
