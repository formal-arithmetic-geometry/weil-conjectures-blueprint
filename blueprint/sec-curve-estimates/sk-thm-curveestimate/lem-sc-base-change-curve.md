+++
id = "lem-sc-base-change-curve"
kind = "lemma"
title = "Base change of a curve"
lean = ["AlgebraicGeometry.IsConnectedCurve.baseChangeField_of_compactification", "AlgebraicGeometry.Scheme.Hom.baseChangeField_isCurve", "AlgebraicGeometry.IsConnectedCurve.baseChangeField"]
order = 1436
uses = ["def-sc-curves", "def-weil-pbc-scheme-conventions"]
+++
Let $k\subseteq k'$ be a field extension and let $C$ be a separated,
quasi-compact $k$-scheme which is smooth of relative dimension one over $k$.
Then $C_{k'}$ is a curve over $k'$ in the sense of [def-sc-curves] which is
smooth of relative dimension one; it is proper if $C$ is, and affine if $C$
is. If moreover $k$ is algebraically closed and $C$ is a smooth connected
curve over $k$ which is proper, or which is an open subscheme of a smooth
proper connected curve over $k$, then $C_{k'}$ is a connected curve over $k'$.
