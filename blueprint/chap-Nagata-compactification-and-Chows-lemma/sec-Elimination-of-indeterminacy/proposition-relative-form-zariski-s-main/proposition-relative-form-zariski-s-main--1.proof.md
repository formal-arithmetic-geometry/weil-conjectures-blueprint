+++
kind = "proof"
of = "proposition-relative-form-zariski-s-main--1"
order = 1435003
+++
Let $T_0$ be the normalization of $T$ in $Z$. The morphism
$T_0\to T$ is affine, so $T_0$ is quasi-affine by
`AlgebraicGeometry.Scheme.IsQuasiAffine.of_isAffineHom`.
Since $f$ is quasi-compact and $T$ is quasi-compact, $Z$ is
quasi-compact, as expressed by
`AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace`.
Zariski's Main Theorem makes the canonical map $Z\to T_0$ an
open immersion. Applying
`AlgebraicGeometry.Scheme.IsQuasiAffine.of_isImmersion` to this
map shows that $Z$ is quasi-affine.
