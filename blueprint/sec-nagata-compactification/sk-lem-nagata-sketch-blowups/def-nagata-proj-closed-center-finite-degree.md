+++
id = "def-nagata-proj-closed-center-finite-degree"
kind = "definition"
title = "Finite-degree data attached to a closed center in Proj"
order = 138
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center", "AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center_le_blowup"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-relative-proj", "lemma-nagata-affine-blowup-complement", "lemma-nagata-chart-extended-ideal-principal", "lemma-nagata-dense-flat-pullback", "lemma-nagata-extended-ideal-affine-chart", "lemma-nagata-finite-type-ideal-extension-exists", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-localization-ideal-pow", "lemma-nagata-proj-closed-center-finite-degree-exists", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
Let $\mathcal I$ be a finite type quasi-coherent ideal on a qcqs scheme
$X$, let $b\colon X'=\operatorname{Bl}_{\mathcal I}(X)\to X$ be its blow-up
with exceptional ideal $\mathcal I_E=\mathcal I\mathcal O_{X'}$, and let
$Z'\hookrightarrow X'$ be the closed subscheme defined by a finite type
quasi-coherent ideal $\mathcal I_{Z'}\subseteq\mathcal O_{X'}$. Choose a pair
$(d,\mathcal F)$ consisting of an integer $d>0$ and a finite type
quasi-coherent ideal $\mathcal F\subseteq\mathcal I^d$ on $X$ such that

$$
\mathcal F\mathcal O_{X'}=\mathcal I_E^d\,\mathcal I_{Z'}
\qquad\text{and}\qquad
|V(\mathcal F)|=|V(\mathcal I)|\cup b(|Z'|);
$$

such pairs exist (Stacks Tag 0803; see
[lemma-nagata-proj-closed-center-finite-degree-exists]). Denote the
chosen pair by $\mathsf{FD}(Z')=(d(Z'),\mathcal F(Z'))$.

In terms of the Rees algebra $\mathcal A=\bigoplus_{n\geq0}\mathcal I^n$,
with $X'=\operatorname{Proj}_X(\mathcal A)$, the equality
$\mathcal F\mathcal O_{X'}=\mathcal I_E^d\,\mathcal I_{Z'}$ says that

$$
Z'=\operatorname{Proj}_X\bigl(\mathcal A/\mathcal F(Z')\mathcal A\bigr),
$$

and the support of $\mathcal I^{d(Z')}/\mathcal F(Z')$ lies in the union of
the first center $V(\mathcal I)$ and the image $b(|Z'|)$.
