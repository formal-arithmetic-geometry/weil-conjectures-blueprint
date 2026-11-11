+++
id = "theorem-cohomology-curves"
kind = "theorem"
title = "Cohomology of curves"
order = 360
lean = ["AlgebraicGeometry.IsCurve.Assertions.of_finite_coefficients"]
uses = ["definition-torsion-sheaves"]
+++
Let $k$ be algebraically closed, let $C$ be a separated scheme of finite
type over $k$ with $\dim C\leq1$, and let $F$ be a classical torsion
abelian sheaf on $C_{\mathrm{pro}\acute{e}t}$. With cohomology taken on
$C_{\mathrm{pro}\acute{e}t}$, the following assertions hold:

- $(C_{1})$ $H^q(C,F)=0$ for $q>2$.
- $(C_{2})$ If $C$ is affine, $H^q(C,F)=0$ for $q>1$.
- $(C_{3})$ If $\operatorname{char}k=p>0$ and $F$ is $p$-primary,
  $H^q(C,F)=0$ for $q>1$.
- $(C_{4})$ If $F$ is constructible with finite stalks and prime to
  $\operatorname{char}k$, all $H^q(C,F)$ are finite.
- $(C_{5})$ If $C$ is proper and $F$ is constructible with finite stalks,
  all $H^q(C,F)$ are finite.
- $(C_{6})$ If $k'/k$ is an extension of algebraically closed fields and $F$
  is prime to $\operatorname{char}k$, the pullback maps
  $H^q(C,F)\to H^q(C_{k'},F|)$ are isomorphisms.
- $(C_{7})$ If $C$ is proper, the maps in $(C_6)$ are isomorphisms for every
  torsion $F$.
- $(C_{8})$ For any open $U\subseteq C$, restriction
  $H^2(C,F)\to H^2(U,F|_U)$ is surjective.
