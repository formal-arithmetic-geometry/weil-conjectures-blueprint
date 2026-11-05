+++
kind = "proof"
of = "lemma-detection-proper-direct-image--1"
order = 569004
uses = ["lemma-finite-morphisms", "proposition-extension-zero-restriction-closed-subscheme--8", "proposition-proper-direct-image-extension-zero--8", "theorem-results-from-etale-theory--3"]
+++
If $Y$ is empty, then $K=0$. Otherwise $S$ is nonempty, so the exponent
condition descends to $k$. Since $S$ is of finite type over $k$ and $b$
is proper, $S$, $Y$ and $Z$ are noetherian, and $j$ is quasi-compact.

The étale version of the open–closed sequence in
[proposition-extension-zero-restriction-closed-subscheme--8] gives the
distinguished triangle

$$
j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K
\longrightarrow j_!j^*K[1].
$$

This is `AlgebraicGeometry.Etale.exists_distTriang_openClosed`.
Extension by zero preserves bounded constructibility, by
`AlgebraicGeometry.Etale.boundedConstructible_mapDerivedCategory_openImmersionLowerShriek`;
the corresponding assertion with finite Tor amplitude is
[proposition-proper-direct-image-extension-zero--8]. Thus $j_!j^*K$ is
bounded constructible. Proper finiteness, the proper case of
[theorem-results-from-etale-theory--3], shows that $Rb_*j_!j^*K$ is
bounded constructible. Applying $Rb_*$ to the triangle, and using the
hypothesis on $Rb_*K$, gives

$$
R(bi)_*i^*K\simeq Rb_*Ri_*i^*K\in\Dbc(S,A).
$$

Finite direct image reflects bounded constructibility on noetherian
schemes. Indeed, it is exact by [lemma-finite-morphisms], and its stalk
formula detects zero sheaves. It therefore detects cohomological bounds.
For a sheaf $F$ whose finite direct image $h_*F$ is constructible, the
counit $h^*h_*F\to F$ is surjective. Its source and kernel are
constructible, so its cokernel presentation makes $F$ constructible.
Applied to the cohomology sheaves, this is
`AlgebraicGeometry.Etale.DerivedCategory.boundedConstructible_of_rightDerivedLowerStar`.
It gives $i^*K\in\Dbc(Z,A)$. The finite direct image $Ri_*$ preserves
bounded constructibility, so the original triangle gives
$K\in\Dbc(Y,A)$.
