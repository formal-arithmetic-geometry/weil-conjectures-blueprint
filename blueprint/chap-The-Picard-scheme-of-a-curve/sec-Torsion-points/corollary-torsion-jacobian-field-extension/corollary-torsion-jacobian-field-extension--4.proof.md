+++
kind = "proof"
of = "corollary-torsion-jacobian-field-extension--4"
order = 1558010
uses = ["corollary-degree-jacobian", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension--1"]
+++
`AlgebraicGeometry.Scheme.exists_jacobian_addEquiv_prod` combines
[corollary-degree-jacobian] with the Jacobian of
[theorem-picard-scheme-jacobian-over-separably] to give an additive
isomorphism

$$
E:\operatorname{Pic}(C)\simeq\mathbf Z\times J(C)(k)
$$

whose first coordinate is degree. Since $n>0$, the $n$-torsion of
$\mathbf Z$ is zero. Restricting $E$ to torsion and projecting to
the second factor therefore gives
$\operatorname{Pic}(C)[n]\simeq J(C)(k)[n]$.

In Lean these steps are `AddSubgroup.torsionByCongr` and
`AddSubgroup.nonempty_addEquiv_torsionBy_int_prod`, inside the proof
of `AlgebraicGeometry.Scheme.nonempty_addEquiv_torsionBy_pic_and_quotient`.
Finally apply [corollary-torsion-jacobian-field-extension--1].
