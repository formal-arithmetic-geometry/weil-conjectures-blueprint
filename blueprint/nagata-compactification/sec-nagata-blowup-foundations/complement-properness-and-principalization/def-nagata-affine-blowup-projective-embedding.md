+++
id = "def-nagata-affine-blowup-projective-embedding"
kind = "definition"
title = "Projective-space map of an affine blow-up"
order = 245
lean = ["AlgebraicGeometry.AffineBlowup.toProjectiveSpace"]
uses = ["def-nagata-affine-blowup", "def-nagata-rees-polynomial-map", "def-nagata-relative-proj", "def-nagata-relative-projective-space", "prop-nagata-relative-proj-functoriality"]
+++
Under the data of [def-nagata-rees-polynomial-map], define

$$
e_I\colon\operatorname{Bl}_I(\operatorname{Spec}A)
\longrightarrow\mathbf P^r_A
$$

to be the contravariant relative-Proj morphism supplied by
[prop-nagata-relative-proj-functoriality], induced by $\rho_I$.
