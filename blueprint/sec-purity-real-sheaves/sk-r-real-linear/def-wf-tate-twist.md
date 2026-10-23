+++
id = "def-wf-tate-twist"
kind = "definition"
title = "Tate twists"
lean = ["AlgebraicGeometry.WeilSheaf.cyclotomicUnit", "AlgebraicGeometry.WeilSheaf.tateTwistSheafNat", "AlgebraicGeometry.WeilSheaf.tateTwistSheaf", "AlgebraicGeometry.WeilComplex.tateTwist"]
order = 3810
uses = ["def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "sk-def-sp-tate-twist"]
+++
Let $\Lambda\in\{E,\Qlb\}$, or more generally any admissible coefficient ring, and
let $X=X_0\times_{k_0}k$. The Tate twists $\Lambda_X(m)$, $m\in\mathbf Z$, are the
invertible $\Lambda_X$-modules on $X_{\mathrm{proét}}$ of [sk-def-sp-tate-twist]: for
$\Lambda=E$, $\cO_{E,X}(1)=\varprojlim_n(\cO_E/\ell^n)_X(1)$ is built from the sheaves
$\mu_{\ell^n,X}$ with transition the $\ell$-th power map, $E_X(1)$ is obtained by
inverting $\ell$, $\overline{\mathbf Q}_{\ell,X}(1)$ by the colimit over $E$,
$\Lambda_X(m)$ for $m>0$ is the $m$-fold tensor power, and
$\Lambda_X(-m)$ its dual. Each $\Lambda_X(m)$ carries its canonical Weil structure
$\tau_m:\operatorname{Fr}_X^*\Lambda_X(m)\xrightarrow{\sim}\Lambda_X(m)$ of
[sk-def-sf-weil-complexes], induced by the pullback of roots of unity.

The *Tate twist* of a Weil complex $(K,\varphi_K)$, $K\in\Dbc(X,\Lambda)$
([sk-def-sf-weil-complexes], [def-weil-weil-sheaf-complex]), is

$$
(K,\varphi_K)(m)=\bigl(K(m),\ \varphi_K\otimes\tau_m\bigr),\qquad
K(m)=K\otimes^{\mathbf L}_{\Lambda_X}\Lambda_X(m),
$$

where $\varphi_K\otimes\tau_m$ is composed with the canonical isomorphism
$\operatorname{Fr}_X^*(K\otimes^{\mathbf L}\Lambda_X(m))\cong
\operatorname{Fr}_X^*K\otimes^{\mathbf L}\operatorname{Fr}_X^*\Lambda_X(m)$. On
morphisms of Weil complexes it is $h\mapsto h\otimes\mathrm{id}$. It preserves
constructible Weil sheaves, since $\Lambda_X(m)$ is locally free of rank one.
