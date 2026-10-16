+++
id = "lem-sc-base-change-curve"
kind = "lemma"
title = "Base change of a curve"
lean = ["AlgebraicGeometry.IsConnectedCurve.baseChangeField_of_compactification", "AlgebraicGeometry.Scheme.Hom.baseChangeField_isCurve", "AlgebraicGeometry.IsConnectedCurve.baseChangeField"]
order = 1037
uses = ["def-sc-curves", "def-weil-pbc-scheme-conventions"]
+++
Let $k\subseteq k'$ be algebraically closed and let $C$ be a
curve over $k$. Then $C_{k'}$ is a curve over $k'$ of the same
dimension. If $C$ is smooth (resp. proper, resp. affine), then so is
$C_{k'}$; and if $C$ is a connected curve, then so is $C_{k'}$.
