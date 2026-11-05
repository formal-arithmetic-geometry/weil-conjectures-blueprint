+++
id = "theorem-elimination-indeterminacy--1"
kind = "theorem"
title = "The constructed elimination blow-up"
name_showing = false
order = 1443001
aliases = ["bp-r450-1"]
lean = ["AlgebraicGeometry.coe_support_eliminationCentre", "AlgebraicGeometry.isOpenImmersion_strictTransformMap_eliminationBlowup"]
uses = ["definition-admissible-blow-up", "definition-strict-transform", "definition-compactification-refinement"]
+++
Let $T$ be qcqs, let $U\subseteq T$ be a quasi-compact open, and let
$q:W\to T$ be separated and of finite type, with $W_U\to U$ an
isomorphism. Let $\mathcal K$ be the ideal
`AlgebraicGeometry.eliminationCentre` selected by the construction below,
and let
$$
b:T'=\operatorname{Bl}_{\mathcal K}(T)\longrightarrow T
$$
be its $U$-admissible blow-up
`AlgebraicGeometry.eliminationBlowup`. Then
$V(\mathcal K)=T\setminus U$, and the strict transform $W'\to T'$ of
$q$ is an open immersion. In particular, $b^{-1}(U)$ is schematically
dense in $T'$.
