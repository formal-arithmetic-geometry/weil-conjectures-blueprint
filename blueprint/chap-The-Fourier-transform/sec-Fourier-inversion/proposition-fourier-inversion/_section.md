+++
id = "proposition-fourier-inversion"
kind = "proposition"
title = "Fourier inversion"
order = 1231
lean = ["AlgebraicGeometry.nonempty_fourierTransform_comp_fourierTransform_inv_iso"]
uses = ["definition-weil-structure", "definition-tate-twists", "lemma-artin-schreier-character-sheaf"]
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
