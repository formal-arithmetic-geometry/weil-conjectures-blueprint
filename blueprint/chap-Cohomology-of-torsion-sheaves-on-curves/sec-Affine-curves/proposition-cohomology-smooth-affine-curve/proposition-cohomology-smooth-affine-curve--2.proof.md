+++
kind = "proof"
of = "proposition-cohomology-smooth-affine-curve--2"
order = 1579005
uses = ["lemma-cohomology-multiplicative-group", "corollary-torsion-jacobian-field-extension", "lemma-proper-smooth-model", "theorem-cohomology-curves--2", "theorem-bounded-below-cohomology-comparison"]
+++
We work on the étale site and transport the result by
[theorem-bounded-below-cohomology-comparison]. A primitive $n$th root of
unity gives the isomorphism of coefficient sheaves. Connectedness computes
the global sections of the constant sheaf. The Kummer long exact sequence,
with the vanishing of the Brauer group from
[lemma-cohomology-multiplicative-group], supplies the homomorphisms in
degree one.

Choose a smooth proper compactification using [lemma-proper-smooth-model].
The orders at its finitely many boundary points identify
$\mathcal O(U)^\times/k^\times$ with a subgroup of a finite free abelian
group. Since $k^\times$ is $n$-divisible, the quotient of the units by
$n$th powers is finite. Also $\operatorname{Pic}(U)$ is a quotient of the
group of points of a Jacobian by a finitely generated subgroup. The
Jacobian has finite $n$-torsion and is $n$-divisible by
[corollary-torsion-jacobian-field-extension]; the same properties follow
for this quotient. These are
`AlgebraicGeometry.IsConnectedCurve.finite_units_quotient` and
`AlgebraicGeometry.IsConnectedCurve.surjective_zsmul_pic_and_finite_torsionBy`.

For the higher degrees, Lean applies the affine cohomological-dimension
bound [theorem-cohomology-curves--2] to the torsion sheaf $\mathbf Z/n$.
The bound is proved independently by comparison with the generic point
and reduction to smooth connected curves; it is
`AlgebraicGeometry.IsCurve.subsingleton_sheafH_of_two_le_of_isAffine`.
