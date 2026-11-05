+++
id = "theorem-cohomology-curves--5"
kind = "theorem"
title = "Cohomology of curves (5)"
name_showing = false
order = 360006
aliases = ["bp-r109-5"]
lean = ["AlgebraicGeometry.IsCurve.primeCoefficientCurveAssertions"]
uses = ["definition-torsion-sheaves", "definition-constructible-sheaves"]
+++
Let $k$ be algebraically closed, let $C$ be a reduced proper scheme
of finite type over $k$ with $\dim C\leq1$, let $\ell$ be a prime, and
let $F$ be a constructible sheaf of $\mathbf F_\ell$-vector spaces on
$C_{\acute{e}t}$. Then every $H^q(C,F)$, $q\geq0$, is finite.
Cohomology is taken on the underlying abelian sheaf; constructibility
here gives finite stalks. This is the constructible prime-coefficient
case of $(C_5)$ used in the Lean route.
