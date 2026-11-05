+++
id = "theorem-cohomology-curves--8"
kind = "theorem"
title = "Cohomology of curves (8)"
name_showing = false
order = 360009
aliases = ["bp-r109-8"]
lean = ["AlgebraicGeometry.IsCurve.primeCoefficientCurveAssertions"]
uses = ["definition-torsion-sheaves", "definition-constructible-sheaves"]
+++
Let $k$ be algebraically closed, let $C$ be a reduced separated scheme
of finite type over $k$ with $\dim C\leq1$, let $\ell$ be a prime, and
let $F$ be a constructible sheaf of $\mathbf F_\ell$-vector spaces on
$C_{\acute{e}t}$. For every open immersion $a:U\hookrightarrow C$, the
restriction map
$$
H^2(C,F)\longrightarrow H^2(U,a^*F)
$$
is surjective. Cohomology is taken on the underlying abelian sheaves.
This is the constructible prime-coefficient case of $(C_8)$ used in
the Lean route.
