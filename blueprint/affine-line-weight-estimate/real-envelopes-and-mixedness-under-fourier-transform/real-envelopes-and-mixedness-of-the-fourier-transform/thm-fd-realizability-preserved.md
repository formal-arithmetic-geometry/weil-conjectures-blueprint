+++
id = "thm-fd-realizability-preserved"
kind = "theorem"
title = "Fourier preservation of realizability for an extension by zero; the Kiehl–Weissauer property (c)"
order = 4248
uses = ["def-fd-nonexceptional", "def-fd-transform", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-iota-real", "def-wf-middle-extension", "fin2-lem-lisse-dense-open", "lem-fd-realified-kernel-concentration", "lem-fd-realified-kernel-real", "lem-fd-realness-pushforward"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and $\mathcal M$ be as in
[lem-fd-realified-kernel-real] — $j$ a dense open immersion with
$U_0=\mathbf A^1_{k_0}\setminus S_0$ and $\mathcal M$ an irreducible
lisse Weil sheaf on
$U_0$, unramified at infinity,
punctually $\iota$-pure of weight
$w$, with irreducible geometric fundamental representation of
[def-wf-fundamental-representation] and
middle extension that is
Fourier-nonexceptional — and let
$\mathcal K$ be the realified kernel of
[lem-fd-realified-kernel-real]. Then the restriction of the
Fourier–Deligne transform
$\operatorname{FT}_\psi(j_!\mathcal M)$ to every dense open
$U'_0\hookrightarrow\mathbf A^1_{k_0}$ over which it is lisse is
$\iota$-realizable in the sense of
[def-wf-iota-real]; in particular its generic lisse part is
$\iota$-realizable.

## Proof

By [lem-fd-realified-kernel-real] the realified kernel $\mathcal K$
is $\iota$-real, and by
[lem-fd-realified-kernel-concentration] only the degree $1$
cohomology of $p_{2,!}\mathcal K$ survives, with
$\operatorname{FT}_\psi(j_!\mathcal M)$ of [def-fd-transform] a
direct summand of the single
sheaf $R^{1}p_{2,!}\mathcal K$ placed in degree $0$. By
[lem-fd-realness-pushforward], applied to $\mathcal K$ and to that
vanishing, the sheaf $R^{1}p_{2,!}\mathcal K$ is $\iota$-real. Let
$U'_0$ be a dense open of the dual line on which both
$\operatorname{FT}_\psi(j_!\mathcal M)$ and
$R^{1}p_{2,!}\mathcal K$ are lisse; such a dense open exists by
[fin2-lem-lisse-dense-open] (applied to each of the two
constructible sheaves separately and intersected), and the direct-summand
relation restricts to one, restriction of Weil sheaves to an open being
exact and additive. On $U'_0$ the transform is therefore a direct
summand of the $\iota$-real lisse sheaf
$\bigl(R^{1}p_{2,!}\mathcal K\bigr)|_{U'_0}$, hence
$\iota$-realizable in the sense of [def-wf-iota-real]. The
*weight* of the generic part is deliberately not asserted here: the
$L^2$-calibration of the transformed sheaf is a separate step, and it
needs in addition the identification of the two generic parts recorded in
the extension-by-zero route.
