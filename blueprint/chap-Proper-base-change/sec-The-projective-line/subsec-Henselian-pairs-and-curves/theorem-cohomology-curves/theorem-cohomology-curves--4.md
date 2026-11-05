+++
id = "theorem-cohomology-curves--4"
kind = "theorem"
title = "Cohomology of curves (4)"
name_showing = false
order = 360005
aliases = ["bp-r109-4"]
lean = ["AlgebraicGeometry.IsCurve.primeCoefficientCurveAssertions"]
uses = ["definition-torsion-sheaves", "definition-constructible-sheaves"]
+++
Let $k$ be algebraically closed, let $C$ be a reduced separated scheme
of finite type over $k$ with $\dim C\leq1$, let $\ell$ be a prime, and
let $F$ be a constructible sheaf of $\mathbf F_\ell$-vector spaces on
$C_{\acute{e}t}$. If the torsion in its geometric stalks is prime to
$\operatorname{char}k$, then every $H^q(C,F)$, $q\geq0$, is finite.
Cohomology is taken on the underlying abelian sheaf; constructibility
here gives finite stalks. This is the constructible prime-coefficient
case of $(C_4)$ used in the Lean route.
