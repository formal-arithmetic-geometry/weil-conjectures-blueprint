+++
id = "def-nagata-dense-valuation-probe"
kind = "definition"
title = "Valuation probe through a schematically dense source"
order = 451
lean = ["AlgebraicGeometry.ValuativeCommSqWithPt"]
uses = ["lemma-nagata-dense-valuation-probe-exists"]
+++
Let $h\colon T\to P$ be quasi-compact, assume its image
inclusion $\operatorname{SIm}(h)\hookrightarrow P$ is an isomorphism, assume
$P$ is affine, and let $z\in P$.
Select a witness from
[lemma-nagata-dense-valuation-probe-exists] and denote it by

$$
\mathsf{VP}(h,z)=
(A'_{h,z},K'_{h,z},\eta_{h,z},\alpha_{h,z}),
$$

where $A'_{h,z}$ is the selected valuation ring, $K'_{h,z}$ its fraction
field, $\eta_{h,z}\colon\operatorname{Spec}(K'_{h,z})\to T$ the selected
generic lift, and
$\alpha_{h,z}\colon\operatorname{Spec}(A'_{h,z})\to P$ the selected centred
valuation map.
