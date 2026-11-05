+++
kind = "proof"
of = "lemma-products-composites-u-admissible-blow--1"
order = 1430004
uses = []
+++
On $T_1$, the ideal $\mathcal I\mathcal O_{T_1}$ is invertible, and it
remains invertible after the second blow-up. The pullback of
$\mathcal J\mathcal O_{T_1}$ becomes invertible there too. Hence the
pullback of $\mathcal I\mathcal J$ to the iterated blow-up is invertible,
and the universal property gives a morphism to the product blow-up.
This uses `AlgebraicGeometry.Scheme.IdealSheafData.isInvertible_comap_blowupMap`
and `AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup`.

Conversely, on the product blow-up the product of the two extended ideals
is invertible, so each factor is invertible. First lift to $T_1$ and then
to the blow-up of $\mathcal J\mathcal O_{T_1}$. Uniqueness in the universal
property, expressed by
`AlgebraicGeometry.Scheme.IdealSheafData.hom_ext_of_isInvertible_comap`,
shows that the two morphisms are inverse and that the isomorphism lies
over $T$.

For the common-refinement assertion, take ideals of finite type that are
the unit ideal on $U$. Their product has the same properties, by
`AlgebraicGeometry.Scheme.IdealSheafData.ofFiniteType.mul` and the formula
$V(\mathcal I\mathcal J)=V(\mathcal I)\cup V(\mathcal J)$.
The comparison gives a morphism from the product blow-up to the blow-up
of $\mathcal I$; exchanging the factors gives one to the blow-up of
$\mathcal J$. Induction gives the assertion for a finite family, starting
with the unit ideal for the empty family. Lean uses this construction for
two centers in `AlgebraicGeometry.nonempty_commonModification`.
