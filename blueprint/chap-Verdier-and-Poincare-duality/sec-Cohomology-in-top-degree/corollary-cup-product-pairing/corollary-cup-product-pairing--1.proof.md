+++
kind = "proof"
of = "corollary-cup-product-pairing--1"
order = 871004
uses = ["theorem-trace-isomorphism-top-degree", "proposition-relative-dualizing-complex"]
+++
Take the Frobenius-compatible trace isomorphism in top degree from
[theorem-trace-isomorphism-top-degree]. The construction in
`AlgebraicGeometry.WeilSheaf.exists_traceCup_isPerfect_of_linearEquiv`
uses this trace to produce the required structure.

The geometric fibre $X$ is smooth, proper and connected. In every
nonnegative degree, identify the cohomology of the constant Weil sheaf
with the pro-étale cohomology of $\Qbarl$ on $X$; this identification
intertwines geometric Frobenius with pullback along the geometric
Galois Frobenius. Transport the cup products from the finite coefficient
levels through these identifications, and set the product equal to zero
when either degree is negative. Compatibility with pullback and graded
commutativity give the corresponding properties of $T$.

At each finite level $\Z/\ell^r\Z$, the orientation of
[proposition-relative-dualizing-complex] gives a trace–cup pairing
nondegenerate on both sides. Thus the finite-level cup product is
nondegenerate. The finite cohomology groups give finitely generated
integral cohomology modules; the finite-level nondegeneracy, followed by
extension of scalars to $\Qbarl$, makes the cup product followed by the
chosen trace perfect. This is
`AlgebraicGeometry.ProEtale.isPerfPair_adicConstantHCup`.
Transporting along the cohomology identifications preserves perfectness.

Finally, if $i+j=2d$ and one degree is negative, both complementary
groups vanish by [theorem-trace-isomorphism-top-degree]. Their pairing
is therefore perfect as well. The chosen trace is already an
isomorphism, so $T$ has all the asserted properties.
