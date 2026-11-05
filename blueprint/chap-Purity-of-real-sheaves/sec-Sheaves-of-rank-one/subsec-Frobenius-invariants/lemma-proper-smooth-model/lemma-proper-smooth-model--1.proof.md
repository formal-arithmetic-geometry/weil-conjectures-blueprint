+++
kind = "proof"
of = "lemma-proper-smooth-model--1"
order = 1091002
uses = ["theorem-nagata-s-compactification-theorem"]
+++
Smoothness makes $U_0$ regular, and geometric connectedness makes it
nonempty and connected. Thus $U_0$ is integral of dimension one, with
integrally closed local rings.

Choose a compactification $U_0\hookrightarrow Z_0$ by
[theorem-nagata-s-compactification-theorem], and let $C_0$ be the relative
normalization of $Z_0$ in $U_0$. The map $C_0\to Z_0$ is finite by
`AlgebraicGeometry.Scheme.Hom.isFinite_fromNormalization`, so $C_0$ is
proper over $k_0$. Normalization commutes with the open base change
$U_0\hookrightarrow Z_0$, and $j_0:U_0\to C_0$ is an open immersion.
The scheme $C_0$ is integral and has dimension one, since it contains
$U_0$ as a nonempty open subscheme.

The local rings of $C_0$ are integrally closed by
`AlgebraicGeometry.Scheme.Hom.isIntegrallyClosed_stalk_normalization`.
As $C_0$ is locally noetherian of dimension one, these local rings are
fields or discrete valuation rings. Hence $C_0$ is regular, and it is
smooth over the perfect field $k_0$ by
`AlgebraicGeometry.smooth_of_isRegular`. Its dimension gives smoothness
of relative dimension one.

After any field extension, the open subscheme obtained from $U_0$
remains connected and dense in the base change of $C_0$. Consequently
$C_0$ is geometrically connected, as in
`AlgebraicGeometry.GeometricallyConnected.of_isOpenImmersion`. Finally,
in an irreducible noetherian scheme of dimension one the complement of
a nonempty open subset is a finite set of closed points. This also
shows that $j_0$ has dense image.
