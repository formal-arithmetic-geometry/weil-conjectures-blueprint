+++
id = "lemma-nagata-composition-center-ideal"
kind = "lemma"
title = "Support of the constructed composition center"
order = 132
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp", "AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center"]
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "def-nagata-proj-closed-center-finite-degree", "lemma-nagata-affine-blowup-complement", "lemma-nagata-blowup-invertible-factor", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-product-ideal-common-blowup", "lemma-nagata-proj-closed-center-finite-degree-exists", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-complement", "thm-nagata-global-blowup-proper"]
+++
Let $X$ be qcqs, let $\mathcal I\subseteq\mathcal O_X$ be a finite-type
quasi-coherent ideal, put
$X'=\operatorname{Bl}_{\mathcal I}(X)$ with structure map
$b\colon X'\to X$, and let $Z'\hookrightarrow X'$ be a
finite-presentation closed immersion. Write
$Z=V(\mathcal I)\hookrightarrow X$. With
$\mathsf{FD}(Z')=(d,\mathcal F)$, define

$$
\mathcal J(Z')=\mathcal F\subseteq\mathcal I^d\subseteq\mathcal O_X,
\qquad
\mathcal K(Z')=\mathcal I\mathcal J(Z'),
\qquad
Y(Z')=V(\mathcal K(Z')).
$$

Then the ideal $\mathcal K(Z')$ is finite type and

$$
|Y(Z')|=|V(\mathcal I)|\cup b(|Z'|).
$$
