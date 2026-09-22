+++
id = "def-kun-projection-formula-map"
kind = "definition"
title = "The projection-formula morphism"
order = 6098
lean = ["AlgebraicGeometry.Etale.projectionFormulaMap"]
uses = ["def-kun-derived-tensor", "lem-kun-inverse-image-monoidal"]
+++
Let $f:X\to Y$ be a morphism of schemes, $\Lambda$ a commutative ring,
$E\in D(X_{\Et},\Lambda)$, and $K\in D(Y_{\Et},\Lambda)$. The
*projection-formula morphism* is the morphism
$$
\mathrm{PF}_f(E,K):\quad Rf_*E\otimes^{\mathbf L}_\Lambda K\longrightarrow
Rf_*\bigl(E\otimes^{\mathbf L}_\Lambda f^{-1}K\bigr)
$$
in $D(Y_{\Et},\Lambda)$ adjoint to the composite
$$
f^{-1}(Rf_*E\otimes^{\mathbf L}_\Lambda K)\cong f^{-1}Rf_*E\otimes^{\mathbf L}_\Lambda f^{-1}K
\xrightarrow{\ \varepsilon_f\otimes1\ }E\otimes^{\mathbf L}_\Lambda f^{-1}K,
$$
where the first map is the monoidality isomorphism of
[lem-kun-inverse-image-monoidal] and $\varepsilon_f$ is the counit of the
derived adjunction.

Unresolved dependencies: def:weil-pbc-inverse-image
