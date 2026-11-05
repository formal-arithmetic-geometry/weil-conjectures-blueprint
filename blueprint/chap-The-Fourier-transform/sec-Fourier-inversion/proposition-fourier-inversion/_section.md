+++
id = "proposition-fourier-inversion"
kind = "proposition"
title = "Fourier inversion"
order = 1234
lean = ["AlgebraicGeometry.nonempty_iso_fourierTransform_comp_inv", "AlgebraicGeometry.nonempty_iso_fourierTransform_comp_self"]
uses = ["lemma-stability", "proposition-six-operations-change-coefficients", "lemma-artin-schreier-character-sheaf", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Under $V^{\vee\vee}=V$ there are natural isomorphisms of functors
$\Dbc(V,E)\to\Dbc(V,E)$

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)
\simeq K(-r),
\qquad
\operatorname{FT}_{\psi}\operatorname{FT}_\psi(K)
\simeq [-1]_V^*K(-r).
$$
