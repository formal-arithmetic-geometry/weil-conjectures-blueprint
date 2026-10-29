+++
id = "sk-thm-curve-package"
kind = "theorem"
title = "Cohomology of curves over an algebraically closed field"
order = 1616
uses = ["sk-lem-curve-dense-open", "sk-prop-sf-comparison", "sk-thm-pe-classical-sheaves"]
tags = ["sketch"]
+++
*Conventions.* Cohomology means cohomology on $C_{\mathrm{proét}}$, and the
sheaves are *classical*: by [sk-thm-pe-classical-sheaves] a classical sheaf is
the inverse image $\nu_C^*$ of a sheaf on $C_{\mathrm{ét}}$ under the
comparison morphism $\nu_C$, and [sk-prop-sf-comparison] identifies its
cohomology, together with restriction and pullback maps, with étale
cohomology.

Let $k$ be algebraically closed, $C$ a separated scheme of finite type over
$k$ of dimension at most one, and $F$ a classical torsion abelian sheaf on
$C_{\mathrm{proét}}$. The following statements hold (compare
[def-weil-pbc-eight-curve-assertions]).

- $(C_1)$ $H^q(C,F)=0$ for $q>2$.
- $(C_2)$ If $C$ is affine, $H^q(C,F)=0$ for $q>1$.
- $(C_3)$ If $\operatorname{char}k=p>0$ and $F$ is $p$-primary, then
  $H^q(C,F)=0$ for $q>1$.
- $(C_4)$ If $F$ is constructible with finite stalks and its torsion orders
  are prime to $\operatorname{char}k$, all its cohomology groups are finite.
- $(C_5)$ If $C$ is proper and $F$ is constructible with finite stalks, all
  its cohomology groups are finite.
- $(C_6)$ For an extension $k'/k$ of algebraically closed fields, the natural
  pullback maps $H^q(C,F)\to H^q(C_{k'},F|_{C_{k'}})$ are isomorphisms if $F$
  is prime to the characteristic.
- $(C_7)$ If $C$ is proper, these pullback maps are isomorphisms for every
  classical torsion $F$.
- $(C_8)$ For every open $U\subseteq C$, the map
  $H^2(C,F)\to H^2(U,F|_U)$ is surjective.

In characteristic zero every torsion order is allowed in $(C_4)$ and $(C_6)$.

This is the pro-étale form of (Stacks, Tag 03SC).
