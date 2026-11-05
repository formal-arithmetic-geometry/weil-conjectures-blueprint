+++
kind = "proof"
of = "proposition-p-torsion-smooth-proper-curve--4"
order = 1584008
uses = ["proposition-p-torsion-smooth-proper-curve--1", "proposition-p-torsion-smooth-proper-curve--2", "proposition-p-torsion-smooth-proper-curve--3", "lemma-sheaves-finite-support-finite-morphisms", "proposition-smooth-proper-curves-torsion-prime--2", "proposition-smooth-proper-curves-torsion-prime--3", "proposition-smooth-proper-curves-torsion-prime--4", "proposition-multiplication-n", "lemma-cohomology-modules-underlying-abelian"]
+++
First suppose that $r=p=\operatorname{char}k$. In degree zero,
[proposition-p-torsion-smooth-proper-curve--1] gives the calculation
for $\mathbf F_p$. In degree one, surjectivity of the degree-zero
Artin–Schreier map makes $H^1(C,\mathbf F_p)$ inject into the kernel
of Frobenius minus the identity on first additive cohomology. This
kernel is finite. Indeed, a finite family of fixed vectors that is
linearly independent over $\mathbf F_p$ is linearly independent over
$k$: normalize a relation of minimal support, apply Frobenius and
subtract. Minimality forces all its coefficients to lie in the prime
field. This bounds the dimension of the fixed space by that of the
scalar model, and the prime field is finite. This is
`LinearMap.Frobenius.finite_fixedPoints`, used by the private helper
`finite_ker_artinSchreier_one` in `Curve/SmoothCalculations.lean`.
Higher degrees vanish by
[proposition-p-torsion-smooth-proper-curve--3]. A connected smooth
zero-dimensional scheme over $k$ is a point, whose positive-degree
cohomology vanishes [lemma-sheaves-finite-support-finite-morphisms].

For $r\ne\operatorname{char}k$, the proper-curve Kummer calculations
[proposition-smooth-proper-curves-torsion-prime--2],
[proposition-smooth-proper-curves-torsion-prime--3] and
[proposition-smooth-proper-curves-torsion-prime--4], together with
finiteness of the torsion of the Jacobian
[proposition-multiplication-n], give finiteness for $\mathbf F_r$.
If $\Lambda/r\Lambda$ is finite, a basis over $\mathbf F_r$ expresses
its constant abelian sheaf as a finite direct sum of constant
$\mathbf F_r$-sheaves. Additivity of cohomology gives the stated
finiteness. The passage to underlying abelian sheaves is justified by
[lemma-cohomology-modules-underlying-abelian].

For base change, Lean separates degrees zero, one and at least two
in `AlgebraicGeometry.IsCurve.proper_constant_base_change_zero`,
`AlgebraicGeometry.IsCurve.proper_constant_base_change_one` and
`AlgebraicGeometry.IsCurve.proper_constant_base_change_higher`.
Degree zero is the comparison of constant sections on the connected
curves. In characteristic $r$, the degree-one comparison for
$\mathbf F_r$ is the map on Frobenius kernels in
[proposition-p-torsion-smooth-proper-curve--2]. The map
$v\mapsto1\otimes v$ is bijective on these kernels, by
`LinearMap.Frobenius.bijective_tmul_fixedPoints`: in a basis, the
coordinates of a fixed vector after extension span a finite-dimensional
$k$-space containing all their iterated $p$th powers. They are therefore
algebraic over $k$, and lie in $k$ since $k$ is algebraically closed.
Injectivity follows from injectivity of scalar extension.

For arbitrary $\Lambda/r\Lambda$, choose a basis over $\mathbf F_r$
and express its constant sheaf as a filtered colimit of finite sums.
Étale cohomology on these quasi-compact quasi-separated schemes
commutes with this colimit. The degree-one comparison becomes the
same bijection on finitely supported families of fixed vectors;
this is
`AlgebraicGeometry.IsCurve.exists_constantModSheaf_one_frobenius_baseChange_model`.
In higher degrees the characteristic-$r$ groups vanish. When $r$ is
invertible in $k$, Lean uses the comparison on global sections of
injective $\Lambda$-module sheaves and acyclicity of their pullbacks,
through `AlgebraicGeometry.Etale.bijective_cohomologyMap_of_prime_injective_acyclic`.
Transport along the isomorphism with the standard pullback square
then gives the result for the specified base change.
