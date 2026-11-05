+++
kind = "proof"
of = "lemma-normalization-constant-sheaf--1"
order = 1600003
uses = ["lemma-finite-morphisms"]
+++
Surjectivity of $\nu$ is preserved by base change, so $\nu'$ is
surjective. The unit

$$
\underline R_U\longrightarrow\nu'_*\nu'^*\underline R_U
$$

is a monomorphism by
`AlgebraicGeometry.Etale.mono_unit_app_of_surjective`. Identify
$\nu'^*\underline R_U$ with $\underline R_{U'}$, apply the exact functor
$j_!$, and compose with the finite direct image comparison

$$
j_!\nu'_*\underline R_{U'}\xrightarrow{\sim}
\nu_*j'_!\underline R_{U'}.
$$

This comparison is `AlgebraicGeometry.Etale.finiteOpenComparison`; it is
an isomorphism by
`AlgebraicGeometry.Etale.isIso_finiteOpenComparison_app`, using finite
base change from [lemma-finite-morphisms] on $U$ and vanishing outside
$U$. The composite gives the required monomorphism $\alpha$.

The cokernel calculation is
`AlgebraicGeometry.normalization_mono_properties`. The scheme $C$ is
Noetherian. The source of $\alpha$ is constructible by extension by zero
of a constant sheaf with finite stalks, and its target is constructible
by `AlgebraicGeometry.finite_pushforward_open_constantModSheaf_constructible`.
Constructibility is preserved by cokernels, so $Q$ is constructible.

Over $V$, finite base change and base change for extension by zero
identify the source and target of $\alpha$ as sheaves; this is
`AlgebraicGeometry.normalization_comparison_on_iso_locus`. Their
geometric stalks are finite. The restricted monomorphism therefore
induces injections between finite sets of the same cardinality, hence
bijections. Geometric stalks detect isomorphisms, so $\alpha|_V$ is an
isomorphism. Since inverse image preserves cokernels, $Q|_V=0$.
