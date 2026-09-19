+++
id = "def-weil-pbc-underived-exchange"
kind = "definition"
title = "Underived exchange map: corrected categorical construction"
order = 641
lean = ["AlgebraicGeometry.Etale.baseChangeMap", "AlgebraicGeometry.Etale.upperStar_map_baseChangeMap_app_counit"]
uses = ["def-weil-pbc-cartesian-square"]
+++
Let $F$ be a sheaf of abelian groups on $X_{\mathrm{et}}$. The chosen
Cartesian identification gives a canonical isomorphism of inverse-image
functors

$$
f'^{-1}g^{-1}\;\xrightarrow{\sim}\;g'^{-1}f^{-1}.
$$

Define $\operatorname{Ex}_{\square,F}$ to be the adjoint of the composite

$$
f'^{-1}g^{-1}f_*F
\xrightarrow{\sim}g'^{-1}f^{-1}f_*F
\xrightarrow{g'^{-1}\varepsilon_f}g'^{-1}F.
$$

Thus

$$
\operatorname{Ex}_{\square,F}:g^{-1}f_*F\longrightarrow
f'_*g'^{-1}F
$$

is a globally constructed morphism of sheaves. Naturality, identity, and
pasting are properties of this fixed mate; no family of stalk maps is used to
construct it.
