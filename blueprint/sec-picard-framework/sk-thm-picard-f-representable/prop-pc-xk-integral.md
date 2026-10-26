+++
id = "prop-pc-xk-integral"
kind = "theorem"
title = "Base changes of $X$ are integral smooth proper curves"
lean = ["AlgebraicGeometry.Scheme.GlobalSectionsBijective.of_isSepClosed", "AlgebraicGeometry.isIso_pushforwardUnitMap_of_globalSectionsBijective", "AlgebraicGeometry.Scheme.smoothOfRelativeDimension_baseChange", "AlgebraicGeometry.Scheme.isProper_baseChange", "AlgebraicGeometry.Scheme.isReduced_baseChange", "AlgebraicGeometry.GeometricallyIntegral.of_smooth_of_geometricallyConnected", "AlgebraicGeometry.GeometricallyIntegral.of_isSepClosed", "AlgebraicGeometry.Scheme.isIntegral_baseChange", "AlgebraicGeometry.Scheme.GlobalSectionsBijective.pullback", "AlgebraicGeometry.Scheme.arithmeticGenus_pullback"]
order = 791
tags = ["latex:proposition"]
uses = ["def-pc-curve", "def-pc-separably-closed", "def-pc-smooth-projective-curve", "lem-pc-closed-imm-base-change", "lem-pc-dim-base-change", "lem-pc-flat-base-change-cohom", "lem-pc-flat-field", "lem-pc-h0-geom-connected", "lem-pc-proper-base-change", "lem-sc-smooth-regular", "rem-pc-regular-normal"]
+++
Let $k$ be a separably closed field and let $X$ be a connected
$k$-scheme which is smooth of relative dimension $1$ and proper over $k$
(for instance a smooth projective curve over $k$).
Then:

1. $H^0(X,\mathcal{O}_X)=k$ and $f_*\mathcal{O}_X=\mathcal{O}_k$ (where $f:X\to\operatorname{Spec} k$);
1. for every field extension $K/k$, the
base change $X_K$ is integral, smooth of relative dimension $1$ and
proper over $K$, hence a curve over $K$ (in particular $X$ is
geometrically integral), with $H^0(X_K,\mathcal{O}_{X_K})=K$ and
$\dim_KH^1(X_K,\mathcal{O}_{X_K})=\dim_kH^1(X,\mathcal{O}_X)$.
