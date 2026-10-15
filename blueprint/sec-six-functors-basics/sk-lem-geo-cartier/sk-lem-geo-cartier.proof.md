+++
kind = "proof"
of = "sk-lem-geo-cartier"
+++
We construct the map in $D(Z_{\mathrm{ét}},\Lambda)$ and apply
$\nu_Z^*\colon D(Z_{\mathrm{ét}},\Lambda)\to D(Z_{\mathrm{proét}},\Lambda)$. Closed
direct image and inverse image comparison identify its source with
$i_*\Lambda_D$ on $Z_{\mathrm{proét}}$, and exactness and tensor compatibility of
$\nu_Z^*$ identify the target and all base-change maps; only bounded below
complexes occur.

The idea is that $c_D$ is the boundary map of the extension of
$i_*\mathbf Z_D$ by $\mathbf G_m$ formed by meromorphic functions with poles
along $D$, reduced modulo $\ell^r$.

Let $j:Z\setminus D\hookrightarrow Z$ be the open complement. Let
$\mathcal M_D\subset j_*\mathbf G_m$ be the subsheaf which, on an open where
$D$ has a regular equation $t$, consists of the products $ut^{-a}$ with $u$ a
unit and $a$ a locally constant integer on $D$; equivalently, it is generated
by $\mathbf G_m$ and $t^{-1}$. Replacing $t$ by a unit multiple gives the same
subsheaf, so $\mathcal M_D$ is globally defined. Sending $t^{-1}$ to $1$ gives
a short exact sequence of abelian sheaves on $Z_{\mathrm{ét}}$

$$
0\longrightarrow\mathbf G_m\longrightarrow \mathcal M_D
  \longrightarrow i_*\mathbf Z_D\longrightarrow0. \qquad\text{(G1)}
$$

Exactness is checked on geometric stalks. Away from $D$ the quotient is zero.
At a point of $D$, no nonzero power of a regular nonunit $t$ is a unit, so the
exponent is well defined, and it is surjective because exponents lift locally
to powers of $t^{-1}$.

The boundary of (G1) is a morphism $i_*\mathbf Z_D\to\mathbf G_m[1]$ in
$D(Z_{\mathrm{ét}},\mathbf Z)$. Apply
$-\otimes^{\mathbf L}_{\mathbf Z}\mathbf Z/\ell^r\mathbf Z$. The source becomes
$i_*\mathbf Z/\ell^r\mathbf Z$. For the target, the Kummer sequence
(Stacks, Tag [03PL](https://stacks.math.columbia.edu/tag/03PL)) shows that the cone of multiplication by $\ell^r$ on
$\mathbf G_m$ has the single cohomology sheaf $\mu_{\ell^r}$ in degree $-1$,
so the target becomes $\mu_{\ell^r}[2]$. This is $c_D$ for
$\mathbf Z/\ell^r\mathbf Z$. For a finite $\mathbf Z/\ell^r\mathbf Z$-algebra
$\Lambda$, apply $-\otimes^{\mathbf L}_{\mathbf Z/\ell^r}\Lambda$; since
$\mu_{\ell^r}$ is locally free of rank one over $\mathbf Z/\ell^r\mathbf Z$,
this gives $\Lambda_Z(1)$ whether or not $\Lambda$ is flat.

To identify the composite with $c_1$, cover $Z$ by opens with local equations
$t_a$. The local lifts of the section $1$ of $i_*\mathbf Z_D$ through (G1) are
the $t_a^{-1}$, and their ratios are the transition functions of
$\mathcal O_Z(D)$ (this fixes the sign convention). So the boundary of (G1)
followed by the Kummer boundary is the class of $\mathcal O_Z(D)$. Changing a
local equation multiplies a lift by a unit and changes the cocycle by a
coboundary.

For naturality, pull back the local equations, the units, and the sequence
(G1); the boundary maps are compatible. On the source one uses the
base-change identity $g^*i_*=i'_*g_D^*$ of functors
$\Mod(D_{\mathrm{ét}},\Lambda)\to\Mod(Z'_{\mathrm{ét}},\Lambda)$, for a base
change $g:Z'\to Z$ with $i':D'\hookrightarrow Z'$ and $g_D:D'\to D$, checked on
geometric stalks.
