+++
kind = "proof"
of = "proposition-p-torsion-smooth-proper-curve--3"
order = 1584007
uses = ["theorem-nagata-s-compactification-theorem", "lemma-coherent-base-change-invertible-sheaves"]
+++
Apply derived global sections to the Artin–Schreier short exact
sequence, supplied by `AlgebraicGeometry.artinSchreier_shortExact`:

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{\varphi-1}\mathbf G_a\longrightarrow0.
$$

The additive cohomology agrees with coherent cohomology and vanishes
in degrees at least two, by
`AlgebraicGeometry.isZero_etaleCohomology_additive_of_two_le`.
The smooth connected curve is either proper or affine, using
compactification [theorem-nagata-s-compactification-theorem]. In the
affine case $H^1(C,\mathbf G_a)=0$; in the proper case it has its
finite-dimensional scalar action, by coherent finiteness
[lemma-coherent-base-change-invertible-sheaves]. The induced
Artin–Schreier map is Frobenius minus the identity.

For a Frobenius-linear map on a finite-dimensional space,
`LinearMap.Frobenius.surjective_sub_id` proves surjectivity by
induction on the dimension. The span of the iterates of a nonzero
vector is a nonzero invariant subspace. On this subspace, solving the
coordinate equations reduces to a polynomial with derivative $-1$,
which has a root over the algebraically closed field. Induction
solves on the quotient, and a correction in the invariant subspace
solves on the whole space. Thus
`AlgebraicGeometry.epi_etaleCohomology_artinSchreier_one` makes the
Artin–Schreier map surjective on $H^1$.

Exactness now makes $H^2(C,\mathbf F_p)$ zero. For $q\geq3$, the two
adjacent additive cohomology groups are already zero, so the same
long exact sequence gives the asserted vanishing.
