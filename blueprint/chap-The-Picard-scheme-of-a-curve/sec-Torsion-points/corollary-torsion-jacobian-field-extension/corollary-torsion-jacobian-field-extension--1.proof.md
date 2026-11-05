+++
kind = "proof"
of = "corollary-torsion-jacobian-field-extension--1"
order = 1558007
uses = ["proposition-multiplication-n", "corollary-torsion-jacobian-field-extension--3", "theorem-picard-scheme-jacobian-over-separably"]
+++
By [corollary-torsion-jacobian-field-extension--3], the abelian
group $A(k)$ is divisible. If a prime $\ell$ divides $n$, then
$\ell$ is invertible in $k$ and [proposition-multiplication-n]
makes $A[\ell]$ finite étale of rank $\ell^{2d}$.
`AlgebraicGeometry.torsionByEquiv` identifies its points with
$A(k)[\ell]$, and
`AlgebraicGeometry.card_points_eq_finrankΓ` gives
$\#A(k)[\ell]=\ell^{2d}$.

`AddSubgroup.nonempty_addEquiv_torsionBy_of_forall_prime` now
applies: divisibility gives the torsion structure for prime powers,
and the Chinese remainder theorem combines the prime-power parts.
For the specialization to $J(C)$, use
[theorem-picard-scheme-jacobian-over-separably]; the equality of its
dimension with $g$ is recorded in
`AlgebraicGeometry.Scheme.exists_jacobian_addEquiv_prod`.
