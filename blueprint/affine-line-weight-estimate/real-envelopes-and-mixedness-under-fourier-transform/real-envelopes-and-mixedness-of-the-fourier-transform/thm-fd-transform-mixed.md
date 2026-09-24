+++
id = "thm-fd-transform-mixed"
kind = "theorem"
title = "The transform is $\\iota$-mixed; the Kiehl–Weissauer property (c)"
order = 4249
uses = ["def-fd-transform", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-iota-real", "lem-fd-realified-kernel-concentration", "lem-fd-realified-kernel-real", "lem-fd-realness-pushforward", "thm-wf-real-mixed-curve"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and $\mathcal M$ be as in
[lem-fd-realified-kernel-real] — a dense open immersion and an
irreducible lisse Weil
sheaf, unramified at infinity,
punctually $\iota$-pure of weight
$w$ — and let $\mathcal K$ be the realified kernel of
[lem-fd-realified-kernel-real]. Then the
Fourier–Deligne transform
$\operatorname{FT}_\psi(j_!\mathcal M)$ is
$\iota$-mixed.

## Proof

By [lem-fd-realified-kernel-real] the realified kernel
$\mathcal K$ is $\iota$-real in the sense of [def-wf-iota-real],
and by [lem-fd-realified-kernel-concentration] the compact-support
direct image $p_{2,!}\mathcal K$ has cohomology in degree $1$ only,
with $\operatorname{FT}_\psi(j_!\mathcal M)$ a direct summand of the
single sheaf $R^{1}p_{2,!}\mathcal K$ placed in degree $0$. By
[lem-fd-realness-pushforward] that sheaf is $\iota$-real, and it is
a constructible Weil sheaf on $\mathbf A^1_{k_0}$, a smooth
geometrically connected affine curve; by
[thm-wf-real-mixed-curve] it is therefore
$\iota$-mixed. Mixedness is
inherited by subobjects and by quotients — a subsheaf of a punctually
pure sheaf is punctually pure of the same weight, its eigenvalues being
eigenvalues of the ambient module — hence by the direct summand
$\operatorname{FT}_\psi(j_!\mathcal M)$.
