+++
id = "lemma-fourier-transform-constant-sheaf"
kind = "lemma"
title = "Transform of the constant sheaf"
order = 1237
lean = ["AlgebraicGeometry.nonempty_iso_fourierTransform_obj_adicConstant", "AlgebraicGeometry.nonempty_iso_fourierTransform_obj_delta"]
uses = ["lemma-stability", "proposition-six-operations-change-coefficients", "lemma-artin-schreier-character-sheaf", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $V=\mathbf A^1_{k_0}$ over $S=\operatorname{Spec}k_0$, and let
$\delta_0$ be the constant skyscraper sheaf $E$ at the origin. There are
isomorphisms of Weil complexes

$$
\operatorname{FT}_\psi(E)\simeq\delta_0(-1)[-1],
\qquad \operatorname{FT}_\psi(\delta_0)\simeq E[1].
$$
