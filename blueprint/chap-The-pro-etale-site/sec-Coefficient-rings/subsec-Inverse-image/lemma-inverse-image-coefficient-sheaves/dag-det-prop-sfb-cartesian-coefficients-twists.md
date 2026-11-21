+++
id = "dag-det-prop-sfb-cartesian-coefficients-twists"
kind = "dag-lemma"
title = "Inverse image of Tate twists"
name_showing = false
order = 187515
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "det-prop-sfb-cartesian-coefficients-twists"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spRoots_cartesian", "AlgebraicGeometry.ProEtale.spCoefficientIso_existsUnique", "AlgebraicGeometry.ProEtale.spCoefficientIso", "AlgebraicGeometry.ProEtale.spIntegralComparison_existsUnique", "AlgebraicGeometry.ProEtale.spIntegralComparison", "AlgebraicGeometry.ProEtale.spTwistFunctor", "AlgebraicGeometry.ProEtale.SpSignedComparison", "AlgebraicGeometry.ProEtale.spFiniteTwists_cartesian", "AlgebraicGeometry.ProEtale.SpInternalCartesian", "AlgebraicGeometry.ProEtale.spTwists_cartesian"]
uses = ["dag-sk-def-sp-tate-twist", "dag-def-pur-roots-of-unity-sheaf"]
+++
Let $f\colon X\to Y$ be a morphism of schemes on which $\ell$ is invertible, and let
$\Lambda\in\{A,\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb\}$ be admissible. There are canonical
isomorphisms
$$
f^{-1}\mu_{\ell^n,Y}\cong\mu_{\ell^n,X},\qquad
f^{-1}\bigl(\Lambda_Y(d)\bigr)\cong\Lambda_X(d)\quad(d\in\mathbf Z),
$$
compatible with the isomorphism $\alpha_f\colon f^{-1}\Lambda_Y\cong\Lambda_X$ of
[dag-lem-sfb-alpha-iso] and the module structures, and with the Kummer transition maps.
Consequently $f^*(K(d))\cong(f^*K)(d)$ for $K\in D(Y_{\mathrm{proét}},\Lambda)$.

(SHEAF DAG node `det-prop-sfb-cartesian-coefficients-twists`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.spRationalComparison_existsUnique`. Statement dependencies not drawn: `lem-sfb-alpha-iso`, `def-weil-proetale-inverse-image`, `sk-def-sfb-condensed-ring`, `sk-def-sfb-pulled-back-coefficients`, `def-sfb-module-upper-star`, `sk-def-sfb-derived-categories`, `def-cbc-strict-constant-tower-operations`.
