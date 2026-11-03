+++
id = "sk-thm-curve-package"
kind = "theorem"
title = "Cohomology of curves"
order = 198
uses = ["sk-lem-curve-dense-open", "sk-prop-sf-comparison", "sk-thm-pe-classical-sheaves"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed, let $C$ be a separated scheme of finite
type over $k$ with $\dim C\leq1$, and let $F$ be a classical torsion
abelian sheaf on $C_{\mathrm{pro}\acute{e}t}$. With cohomology taken on
$C_{\mathrm{pro}\acute{e}t}$, the following assertions hold:

- $(C_1)$ $H^q(C,F)=0$ for $q>2$.
- $(C_2)$ If $C$ is affine, $H^q(C,F)=0$ for $q>1$.
- $(C_3)$ If $\operatorname{char}k=p>0$ and $F$ is $p$-primary,
  $H^q(C,F)=0$ for $q>1$.
- $(C_4)$ If $F$ is constructible with finite stalks and prime to
  $\operatorname{char}k$, all $H^q(C,F)$ are finite.
- $(C_5)$ If $C$ is proper and $F$ is constructible with finite stalks,
  all $H^q(C,F)$ are finite.
- $(C_6)$ If $k'/k$ is an extension of algebraically closed fields and $F$
  is prime to $\operatorname{char}k$, the pullback maps
  $H^q(C,F)\to H^q(C_{k'},F|)$ are isomorphisms.
- $(C_7)$ If $C$ is proper, the maps in $(C_6)$ are isomorphisms for every
  torsion $F$.
- $(C_8)$ For any open $U\subseteq C$, restriction
  $H^2(C,F)\to H^2(U,F|_U)$ is surjective.
