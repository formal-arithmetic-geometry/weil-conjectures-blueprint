+++
id = "theorem-cohomology-curves--3"
kind = "theorem"
title = "Cohomology of curves (3)"
name_showing = false
order = 360004
aliases = ["bp-r109-3"]
lean = ["AlgebraicGeometry.IsCurve.primeCoefficientCurveAssertions"]
uses = ["definition-torsion-sheaves", "definition-constructible-sheaves"]
+++
Let $k$ be algebraically closed, let $C$ be a reduced separated scheme
of finite type over $k$ with $\dim C\leq1$, let $\ell$ be a prime, and
let $F$ be a constructible sheaf of $\mathbf F_\ell$-vector spaces on
$C_{\acute{e}t}$. If $\operatorname{char}k=p>0$ and the geometric stalks
of $F$ are $p$-primary, then
$$
H^q(C,F)=0\qquad(q>1).
$$
Here cohomology is taken on the underlying abelian sheaf. This is the
constructible prime-coefficient case of $(C_3)$ used in the Lean route.
