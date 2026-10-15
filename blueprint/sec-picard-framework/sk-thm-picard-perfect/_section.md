+++
id = "sk-thm-picard-perfect"
kind = "lemma"
title = "Coherent base change for invertible sheaves"
order = 606
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-thm-picard-coherence", "sk-thm-picard-semicon"]
lean = ["AlgebraicGeometry.Scheme.Modules.isOpen_setOf_hFiber_le", "AlgebraicGeometry.Scheme.Modules.isZero_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOfRank_higherDirectImage_restrict"]
tags = ["sketch"]
+++
Let $C/k$ be a smooth projective geometrically connected curve, let $T$
be a locally Noetherian $k$-scheme, write $f_T:C_T=C\times_kT\to T$, and
let $\cL$ be invertible on $C_T$. Then $Rf_{T,*}\cL$ is locally
represented by a bounded complex of finite locally free
$\cO_T$-modules. For any $a:T'\to T$, its derived pullback is
canonically $Rf_{T',*}\cL_{T'}$. The locus where this complex is an
invertible module in degree $0$ is open; there $f_{T,*}\cL$ is
invertible, its formation commutes with arbitrary base change, and
$R^1f_{T,*}\cL=0$.

For an arbitrary test scheme $T$, the same open locus is obtained locally
by descending the finitely presented line bundle to a finitely generated
$k$-algebra and pulling back; the derived base-change isomorphism makes
the result independent of the chosen model.

*General form.* The detailed nodes prove this in the following
generality (the case $i=0$, $r=1$, $\cF=\cL$ is the lemma). Let
$f:X\to T$ be proper of finite presentation and $\cF$ an
$\cO_X$-module of finite presentation, flat over $T$; fix $i\in\Z$ and
$r\ge0$ and write $h^q(t):=\dim_{\kappa(t)}H^q(X_t,\cF_t)$.
The locus

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
