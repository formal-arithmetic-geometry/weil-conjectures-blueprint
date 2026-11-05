+++
kind = "proof"
of = "theorem-trace-formula-euler-product--2"
order = 1036008
uses = []
+++
A closed point of positive degree at most $n$ has degree dividing $n!$,
so it admits a point over $\mathbf F_{q^{n!}}$. Choosing such a point
gives an injection of the closed points of degree at most $n$ into the
finite set $X_0(\mathbf F_{q^{n!}})$. This proves
`AlgebraicGeometry.Scheme.Hom.finite_setOf_degreeOver_le`.

The polynomial $\det(1-T\operatorname{Frob}_x\mid\mathcal F_{\bar x})$
has constant coefficient $1$. Substituting $T^{\deg(x)}$ makes its
difference from $1$ divisible by $T^{\deg(x)}$. Its inverse has the
same congruence, since its constant coefficient is invertible. This is
`AlgebraicGeometry.WeilSheaf.X_pow_dvd_lFactor_sub_one` after applying
$\iota$.
