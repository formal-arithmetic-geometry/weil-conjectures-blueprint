+++
kind = "proof"
of = "proposition-integral-tate-module--1"
order = 1509005
uses = ["proposition-multiplication-n"]
+++
By [proposition-multiplication-n], multiplication by every positive
integer on $A$ is finite and surjective. Over the algebraically closed
field $k$, every point therefore lifts, so $A(k)$ is divisible
(`AlgebraicGeometry.surjective_npow_points`).

For every prime $\ell\mid m$, the group scheme $A[\ell]$ is finite
étale of rank $\ell^{2g}$. Its $k$-points are the $\ell$-torsion of
$A(k)$ (`AlgebraicGeometry.torsionByEquiv`), and their number is its
rank (`AlgebraicGeometry.card_points_eq_finrankΓ`). Choose an
$\Fell$-basis of this torsion group and lift it along multiplication
by powers of $\ell$. The lifted elements generate the torsion at
each level, and their integer relations have coefficients divisible
by the corresponding power of $\ell$. This gives the required
isomorphism for prime powers. The Chinese remainder theorem combines
these isomorphisms for general $m$, as in
`AddSubgroup.nonempty_addEquiv_torsionBy_of_forall_prime`.
