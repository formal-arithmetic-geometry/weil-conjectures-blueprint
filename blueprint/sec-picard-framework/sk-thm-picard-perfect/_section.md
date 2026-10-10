+++
id = "sk-thm-picard-perfect"
kind = "theorem"
title = "Openness of the perfect locus"
order = 677
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.Scheme.Modules.isOpen_setOf_hFiber_le", "AlgebraicGeometry.Scheme.Modules.isZero_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOfRank_higherDirectImage_restrict"]
tags = ["sketch"]
+++
With $f$ and $\cF$ as above, fix $i\in\Z$ and $r\ge0$ and write
$h^q(t):=\dim_{\kappa(t)}H^q(X_t,\cF_t)$. The locus

$$
U_{i,\le r}:=\{t\in T:\ h^q(t)=0\ \text{for all }q\neq i\ \text{and}\ h^i(t)\le r\}
$$

is *open* in $T$, and over it $Rf_*\cF$ is, Zariski locally on
$U_{i,\le r}$, isomorphic to a finite free module placed in degree $i$,
of rank $h^i(t)$, its formation commuting with every base change
$T'\to U_{i,\le r}$. Consequently $h^i$ is locally constant on
$U_{i,\le r}$, the locus

$$
U_{i,r}:=\{t\in T:\ h^q(t)=0\ \text{for all }q\neq i\ \text{and}\ h^i(t)=r\}
$$

is open as well, and on $U_{i,r}$ one has $R^qf_*\cF=0$ for $q\neq i$,
$R^if_*\cF$ finite locally free of rank $r$, and the base-change maps of
[sk-thm-picard-semicon] are isomorphisms; a morphism $T'\to T$
factors through $U_{i,r}$ if and only if $Rf_{T',*}\cF_{T'}$ is
isomorphic to a finite locally free $\cO_{T'}$-module of rank $r$
placed in degree $i$. No reducedness of $T$ is needed.
