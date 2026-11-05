+++
kind = "proof"
of = "proposition-cohomology-smooth-affine-curve--3"
order = 1579006
uses = ["proposition-cohomology-smooth-affine-curve--2", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension"]
+++
Let $a:\mathbf Z^D\to\operatorname{Pic}(\overline C)$ send a divisor
supported on $D$ to its line bundle, and put $M=\ker(a)$ and
$\Lambda=\operatorname{im}(a)$. Orders of units and extension of line
bundles give

$$
\mathcal O(U)^\times/(\mathcal O(U)^\times)^n\simeq M/nM,
\qquad
\operatorname{Pic}(U)\simeq\operatorname{Pic}(\overline C)/\Lambda.
$$

This is the presentation in
`AlgebraicGeometry.IsConnectedCurve.exists_units_pic_presentation`:
the divisor map from units has image $M$, and every element of its
kernel is an $n$th power. The Kummer sequence in
[proposition-cohomology-smooth-affine-curve--2] therefore gives

$$
\#H^1(U,\mathbf Z/n)
=\#(M/nM)\,\#\operatorname{Pic}(U)[n].
$$

Apply the cardinality identity for multiplication by $n$ in a short
exact sequence to

$$
0\longrightarrow M\longrightarrow\mathbf Z^D
\longrightarrow\Lambda\longrightarrow0,
\qquad
0\longrightarrow\Lambda\longrightarrow\operatorname{Pic}(\overline C)
\longrightarrow\operatorname{Pic}(U)\longrightarrow0.
$$

The identity is `AddSubgroup.natCard_quotient_range_zsmul_mul_eq`.
The degree and Jacobian calculations
([corollary-degree-jacobian], [corollary-torsion-jacobian-field-extension])
give

$$
\operatorname{Pic}(\overline C)[n]\simeq(\mathbf Z/n)^{2g},
\qquad
\operatorname{Pic}(\overline C)/n\operatorname{Pic}(\overline C)
\simeq\mathbf Z/n.
$$

Also $\operatorname{Pic}(U)$ is $n$-divisible. Substituting these values
and cancelling the nonzero finite factors gives
$\#H^1(U,\mathbf Z/n)\,n=n^{\#D+2g}$.
