+++
kind = "proof"
of = "sk-lem-geo-cartier"
+++
The map $c_D$ will be the boundary map of the extension of $i_*\mathbf Z_D$ by
$\mathbf G_m$ formed by meromorphic functions with poles along $D$, reduced
modulo $\ell^r$. This is the étale version of the divisor sequence
$0\to\mathcal O_Z\to\mathcal O_Z(D)\to\mathcal O_Z(D)|_D\to0$. We construct
$c_D$ in $D(Z_{\mathrm{ét}},\Lambda)$; as explained at the start of the
subsection, $\nu_Z^*$ transports it and its compatibilities to
$Z_{\mathrm{proét}}$.

Let $j:Z\setminus D\hookrightarrow Z$ be the open complement. Let
$\mathcal M_D\subset j_*\mathbf G_m$ be the subsheaf which, on an open where
$D$ has a regular equation $t$, consists of the products $ut^{-m}$ with $u$ a
unit and $m$ a locally constant integer on $D$; equivalently, it is generated
by $\mathbf G_m$ and $t^{-1}$. Replacing $t$ by a unit multiple gives the same
subsheaf, and hence $\mathcal M_D$ is globally defined. Sending $t^{-1}$ to
$1$, we obtain a short exact sequence of abelian sheaves on
$Z_{\mathrm{ét}}$

$$
0\longrightarrow\mathbf G_m\longrightarrow \mathcal M_D
  \longrightarrow i_*\mathbf Z_D\longrightarrow0. \qquad\text{(G1)}
$$

We check exactness on geometric stalks. Away from $D$, the quotient is zero.
At a point of $D$, no nonzero power of a regular nonunit $t$ is a unit, so the
exponent is well defined, and the map is surjective because exponents lift
locally to powers of $t^{-1}$.

The boundary of (G1) is a morphism $i_*\mathbf Z_D\to\mathbf G_m[1]$ in
$D(Z_{\mathrm{ét}},\mathbf Z)$, to which we apply
$-\otimes^{\mathbf L}_{\mathbf Z}\mathbf Z/\ell^r\mathbf Z$. The source becomes
$i_*\mathbf Z/\ell^r\mathbf Z$. For the target, the Kummer sequence
[Stacks, Tag 03PL](https://stacks.math.columbia.edu/tag/03PL) shows that the
cone of multiplication by $\ell^r$ on $\mathbf G_m$ has the single cohomology
sheaf $\mu_{\ell^r}$ in degree $-1$, and hence the target becomes
$\mu_{\ell^r}[2]$. This is $c_D$ for $\mathbf Z/\ell^r\mathbf Z$. For a finite
$\mathbf Z/\ell^r\mathbf Z$-algebra $\Lambda$, we apply
$-\otimes^{\mathbf L}_{\mathbf Z/\ell^r}\Lambda$. Since $\mu_{\ell^r}$ is
locally free of rank one over $\mathbf Z/\ell^r\mathbf Z$, the target becomes
$\Lambda_Z(1)[2]$.

To identify the composite with $c_1$, we cover $Z$ by opens with local
equations $t_\alpha$. The local lifts of the section $1$ of $i_*\mathbf Z_D$
through (G1) are the $t_\alpha^{-1}$, and their ratios are the transition
functions of $\mathcal O_Z(D)$ (this fixes the sign convention). Hence the
boundary of (G1) followed by the Kummer boundary is the class of
$\mathcal O_Z(D)$. Changing a local equation multiplies a lift by a unit, and
this changes the cocycle by a coboundary.

For naturality, we pull back the local equations, the units, and the sequence
(G1), and observe that the boundary maps are compatible. On the source we use
the identity $g^*i_*=i'_*g_D^*$ for a base change $g:Z'\to Z$ with
$i':D'\hookrightarrow Z'$ and $g_D:D'\to D$; it can be checked on geometric
stalks.
