+++
id = "dag-sk-prop-sfb-cartesian-coefficients"
kind = "dag-lemma"
title = "Inverse image of the coefficient sheaves"
name_showing = false
order = 187503
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves"
dag_id = "sk-prop-sfb-cartesian-coefficients"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.cartesianCoefficientLift", "AlgebraicGeometry.ProEtale.cartesianCoefficientPullbackIso", "AlgebraicGeometry.ProEtale.CartesianCoefficientProperty", "AlgebraicGeometry.ProEtale.cartesianFinitePointRing", "AlgebraicGeometry.ProEtale.CartesianUntwistedAssertions", "AlgebraicGeometry.ProEtale.CartesianFiniteTwistAssertions", "AlgebraicGeometry.ProEtale.CartesianAdicComparison", "AlgebraicGeometry.ProEtale.CartesianAdicTwistAssertions", "AlgebraicGeometry.ProEtale.CartesianTwistAssertions", "AlgebraicGeometry.ProEtale.CartesianFiniteFreeAssertions", "AlgebraicGeometry.ProEtale.cartesianCoefficients"]
+++
Because all coefficient sheaves are pulled back from the point, they are compatible with
inverse image. The same holds for their Tate twists ([dag-sk-def-sp-tate-twist]), and a finite
extension of coefficient fields gives a finite free extension of coefficient sheaves.

Fix a prime $\ell$ and an algebraic closure $\Qlb$ of $\mathbf Q_\ell$.
Let $f\colon X\to Y$ be a morphism of schemes. Coefficient sheaves are the
pullbacks of condensed rings `sk-def-sfb-pulled-back-coefficients`. The admissible
coefficients are the finite commutative coefficient rings $A$ and
$\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb$. Give $A$ its discrete topology. The rings
$A,\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E$ are condensed as in `sk-def-sfb-condensed-ring`; the $\Qlb$ coefficient is specifically
the condensed ring of continuous maps taking values in some finite subextension,
as defined in `sk-def-sfb-qlbar-condensed`;
$E$ and $F$ below are finite subextensions of $\Qlb/\mathbf Q_\ell$.
The assertions about Tate twists are made on the domain of [dag-sk-def-sp-tate-twist]:
$\ell$ is invertible on $X$ and $Y$, and a finite coefficient ring $A$ being twisted
is annihilated by a power of $\ell$. No such invertibility assumption is imposed
on the untwisted assertions.

1. For every admissible $\Lambda$, the canonical map
   $$
   f^{-1}\Lambda_Y\longrightarrow\Lambda_X
   $$
   is an isomorphism of sheaves of rings on $X_{\mathrm{proét}}$ (this is the map $\alpha_f$
   of [dag-sk-def-sfb-coefficient-morphisms]). For every integer $d$, its Tate twists have the corresponding canonical
   isomorphism of coefficient module sheaves
   $f^{-1}(\Lambda_Y(d))\cong\Lambda_X(d)$ along $\alpha_f$, including the twists
   of a finite ring $A$.
2. If $E\subset F$ is a finite extension, then $\cO_{F,X}$ is a finite free
   $\cO_{E,X}$-module and $F_X$ is a finite free $E_X$-module.

By (1), the pullback $f^*\colon\Mod(Y_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$
of modules over these sheaves is exact. More precisely, it is canonically naturally
isomorphic to the lift of $f^{-1}$ whose underlying sheaf functor is $f^{-1}$
and whose $\Lambda_X$-action is obtained using $\alpha_f^{-1}$.

(SHEAF DAG node `sk-prop-sfb-cartesian-coefficients`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-module-objects`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
