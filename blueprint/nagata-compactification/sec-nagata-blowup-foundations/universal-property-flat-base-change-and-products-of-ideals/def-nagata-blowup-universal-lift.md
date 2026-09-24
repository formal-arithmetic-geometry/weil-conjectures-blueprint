+++
id = "def-nagata-blowup-universal-lift"
kind = "definition"
title = "Universal lift construction"
order = 276
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-blowup-universal-graded-map", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-relative-proj", "def-nagata-sheaf-rees-algebra", "lemma-nagata-relative-proj-base-change-arbitrary", "lemma-nagata-relative-proj-invertible-tensor-powers", "prop-nagata-global-blowup-cover-independent"]
+++
Under the data of
[def-nagata-blowup-universal-graded-map], use the inverse of the canonical isomorphism in
[lemma-nagata-relative-proj-invertible-tensor-powers], apply the
contravariant relative-Proj map induced by $\alpha_f$. Then use the
arbitrary base-change comparison in
[lemma-nagata-relative-proj-base-change-arbitrary] to identify the
resulting target with $Y\times_X\operatorname{Bl}_{\mathcal I}(X)$. Here
$\operatorname{Proj}_X(\mathcal R_X(\mathcal I))$ is identified with
[def-nagata-global-blowup]: both are obtained by gluing the same affine
Rees-algebra Proj schemes, and the comparison respects the restriction
cocycles. Compose
the resulting map with the second projection
$Y\times_X\operatorname{Bl}_{\mathcal I}(X)\to \operatorname{Bl}_{\mathcal I}(X)$, and
define

$$
\widetilde f\colon Y\longrightarrow\operatorname{Bl}_{\mathcal I}(X)
$$

to be the resulting composite. The affine maps and their gluing data are
part of the relative-Proj interface; no identification of $Y$ with a Proj
is left implicit.
