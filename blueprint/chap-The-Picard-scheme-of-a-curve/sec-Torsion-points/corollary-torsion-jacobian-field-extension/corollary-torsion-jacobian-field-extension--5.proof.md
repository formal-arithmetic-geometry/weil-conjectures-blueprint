+++
kind = "proof"
of = "corollary-torsion-jacobian-field-extension--5"
order = 1558011
uses = ["corollary-degree-jacobian", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension--3"]
+++
For the quotient isomorphism, Lean uses the splitting
$\operatorname{Pic}(C)\simeq\mathbf Z\times J(C)(k)$ of
`AlgebraicGeometry.Scheme.exists_jacobian_addEquiv_prod`.
The second factor is $n$-divisible by
[corollary-torsion-jacobian-field-extension--3]. Thus
`AddSubgroup.nonempty_addEquiv_quotient_range_zsmul_int_prod`
identifies the quotient of the product by $n$ with
$\mathbf Z/n\mathbf Z$, and
`AddSubgroup.quotientRangeZsmulCongr` transports this isomorphism
back to $\operatorname{Pic}(C)$.

For the kernel equality, suppose $\deg\cL=md$. By
[corollary-degree-jacobian], choose $\cM$ of degree $d$.
Then $\cL\otimes(\cM^{\otimes m})^{-1}$ has degree zero, so
[corollary-torsion-jacobian-field-extension--3] supplies an
$m$-th root $\cN$ in $\operatorname{Pic}^0(C)$. It follows that
$\cL=(\cM\otimes\cN)^{\otimes m}$. Conversely, an $m$-th tensor
power has degree divisible by $m$.

This is `AlgebraicGeometry.Scheme.ker_picDegreeMod`, using
`AlgebraicGeometry.Scheme.surjective_picDegreeHom` and
`AlgebraicGeometry.Scheme.surjective_pow_picardZero`.
Surjectivity of degree then identifies the quotient map with
degree modulo $n$.
