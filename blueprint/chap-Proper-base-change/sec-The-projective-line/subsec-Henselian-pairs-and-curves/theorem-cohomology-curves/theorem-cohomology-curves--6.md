+++
id = "theorem-cohomology-curves--6"
kind = "theorem"
title = "Cohomology of curves (6)"
name_showing = false
order = 360007
aliases = ["bp-r109-6"]
lean = ["AlgebraicGeometry.IsCurve.primeCoefficientCurveAssertions"]
uses = ["definition-torsion-sheaves", "definition-constructible-sheaves"]
+++
Let $k$ be algebraically closed, let $C$ be a reduced separated scheme
of finite type over $k$ with $\dim C\leq1$, let $\ell$ be a prime, and
let $F$ be a constructible sheaf of $\mathbf F_\ell$-vector spaces on
$C_{\acute{e}t}$. If the torsion in its geometric stalks is prime to
$\operatorname{char}k$, then for every extension $k'/k$ of algebraically
closed fields the pullback maps
$$
H^q(C,F)\longrightarrow H^q(C_{k'},F|_{C_{k'}})
$$
are isomorphisms for all $q\geq0$. Cohomology is taken on the underlying
abelian sheaf. This is the constructible prime-coefficient case of
$(C_6)$ used in the Lean route.
