+++
id = "thm-fd-transform-mixed"
kind = "theorem"
title = "The transform is $\\iota$-mixed; the Kiehl–Weissauer property (c)"
order = 3038
uses = ["def-a1-constituent-nonexceptional", "def-fd-transform", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-iota-real", "lem-a1-constituent-nonexceptional-comparison", "lem-fd-constituent-nonexceptional-concentration", "lem-fd-realified-kernel-real", "lem-fd-realness-pushforward", "thm-wf-real-mixed-curve"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion
and let $\mathcal M$ be a nonzero irreducible lisse Weil sheaf on $U_0$,
punctually $\iota$-pure of weight
$w$, which is constituent-nonexceptional in the sense of
[def-a1-constituent-nonexceptional]; no unramifiedness at infinity and
no geometric irreducibility is assumed. This covers the setting of
[lem-fd-realified-kernel-real] (irreducible geometric fundamental
representation and Fourier-nonexceptional middle extension), by
[lem-a1-constituent-nonexceptional-comparison](2). Let $\mathcal K$ be
the realified kernel of
[lem-fd-realified-kernel-real]. Then the
Fourier–Deligne transform
$\operatorname{FT}_\psi(j_!\mathcal M)$ is
$\iota$-mixed.

## Proof

By the general form of [lem-fd-realified-kernel-real], which uses only
the purity of $\mathcal M$, the realified kernel
$\mathcal K$ is $\iota$-real in the sense of [def-wf-iota-real],
and by [lem-fd-constituent-nonexceptional-concentration](3) the compact-support
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
