+++
id = "sk-thm-picard-perfect"
kind = "lemma"
title = "Coherent base change for invertible sheaves"
order = 749
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sec-abelian-varieties", "sec-nagata-compactification", "sk-def-picard-pic", "sk-thm-picard-rr", "sk-prop-picard-pic-split"]
lean = ["AlgebraicGeometry.Scheme.Modules.isOpen_setOf_hFiber_le", "AlgebraicGeometry.Scheme.Modules.isZero_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOfRank_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.nonempty_higherDirectImage_iso_pullback_of_isPullback", "AlgebraicGeometry.Scheme.Modules.exists_opens_range_subset_iff_isFiniteLocallyFreeInDegree", "AlgebraicGeometry.exists_isIso_canonicalModuleBaseChange_of_isFlatOver", "AlgebraicGeometry.noetherian_perfect_directImage"]
tags = ["sketch"]
+++
Let $C/k$ be a smooth projective geometrically connected curve, let $T$
be a locally Noetherian $k$-scheme, write $f_T:C_T=C\times_kT\to T$, and
let $\cL$ be invertible on $C_T$. Then $Rf_{T,*}\cL$ is locally represented
by a bounded complex of finite locally free $\cO_T$-modules.
For any $a:T'\to T$, the base change map
$La^*Rf_{T,*}\cL\to Rf_{T',*}\cL_{T'}$ is an isomorphism in the derived
category of $\cO_{T'}$-modules. The locus where this complex is an
invertible module in degree $0$ is open. On this locus, $f_{T,*}\cL$ is
invertible, its formation commutes with arbitrary base change, and
$R^1f_{T,*}\cL=0$.

The base change isomorphism and the open locus need no Noetherian
hypothesis on $T$: the general form below holds for an arbitrary test
scheme $T$.

*General form.* The detailed nodes prove this in the following
generality (the case $i=0$, $r=1$, $\cF=\cL$ is the lemma). Let
$f:X\to T$ be proper of finite presentation and $\cF$ an
$\cO_X$-module of finite presentation, flat over $T$; fix integers $i\ge0$ and
$r\ge0$ and write $h^q(t):=\dim_{\kappa(t)}H^q(X_t,\cF_t)$.
The locus

$$
U_{i,\le r}:=\{t\in T:\ h^q(t)=0\ \text{for all }q\neq i\ \text{and}\ h^i(t)\le r\}
$$

is *open* in $T$, and over it the higher direct images of $\cF$ are,
Zariski locally on $U_{i,\le r}$, those of a finite free module placed in
degree $i$, of rank $h^i(t)$ near $t$; the same holds after every base
change $T'\to U_{i,\le r}$. Consequently $h^i$ is locally constant on
$U_{i,\le r}$, the locus

$$
U_{i,r}:=\{t\in T:\ h^q(t)=0\ \text{for all }q\neq i\ \text{and}\ h^i(t)=r\}
$$

is open as well, and on $U_{i,r}$ one has $R^qf_*\cF=0$ for $q\neq i$,
$R^if_*\cF$ finite locally free of rank $r$, so that
$Rf_*\cF|_{U_{i,r}}\cong R^if_*\cF[-i]$. For every $g:T'\to T$, with
$f':X'\to T'$ and $\cF'$ the base changes, the base change map
$Lg^*Rf_*\cF\to Rf'_*\cF'$ is an isomorphism in the derived category of
$\cO_{T'}$-modules; for $g$ landing in $U_{i,r}$ it gives
$R^if'_*\cF'\cong g^*R^if_*\cF$ and $R^qf'_*\cF'=0$ for $q\neq i$. A morphism $T'\to T$
factors through $U_{i,r}$ if and only if $Rf_{T',*}\cF_{T'}$ is
isomorphic to a finite locally free $\cO_{T'}$-module of rank $r$
placed in degree $i$ (i.e. $R^qf_{T',*}\cF_{T'}=0$ for $q\neq i$ and
$R^if_{T',*}\cF_{T'}$ is finite locally free of rank $r$). No reducedness of $T$ is needed.
