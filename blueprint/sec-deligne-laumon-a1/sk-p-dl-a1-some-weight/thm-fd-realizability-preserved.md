+++
id = "thm-fd-realizability-preserved"
kind = "theorem"
title = "Fourier preservation of realizability for an extension by zero; the Kiehl–Weissauer property (c)"
order = 3037
uses = ["def-a1-constituent-nonexceptional", "def-fd-transform", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-iota-real", "fin2-lem-lisse-dense-open", "lem-a1-constituent-nonexceptional-comparison", "lem-fd-constituent-nonexceptional-concentration", "lem-fd-realified-kernel-real", "lem-fd-realness-pushforward"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion
with $U_0=\mathbf A^1_{k_0}\setminus S_0$ and let $\mathcal M$ be a
nonzero irreducible lisse Weil sheaf on $U_0$,
punctually $\iota$-pure of weight
$w$, which is constituent-nonexceptional in the sense of
[def-a1-constituent-nonexceptional]; no unramifiedness at infinity and
no geometric irreducibility is assumed. This covers the setting of
[lem-fd-realified-kernel-real] (irreducible geometric fundamental
representation and Fourier-nonexceptional middle extension), by
[lem-a1-constituent-nonexceptional-comparison](2). Let
$\mathcal K$ be the realified kernel of
[lem-fd-realified-kernel-real]. Then there is a dense open
$U'_0\hookrightarrow\mathbf A^1_{k_0}$ of the dual line — any dense open
over which both $\operatorname{FT}_\psi(j_!\mathcal M)$ and
$R^1p_{2,!}\mathcal K$ are lisse will do — on which the restriction of the
Fourier–Deligne transform
$\operatorname{FT}_\psi(j_!\mathcal M)$ is
$\iota$-realizable in the sense of
[def-wf-iota-real]; in particular its generic lisse part is
$\iota$-realizable.

## Proof

By the general form of [lem-fd-realified-kernel-real], which uses only
the purity of $\mathcal M$, the realified kernel $\mathcal K$
is $\iota$-real, and by
[lem-fd-constituent-nonexceptional-concentration](3) only the degree $1$
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
*weight* of the generic part is not asserted here; it is obtained
afterwards for the generic sheaf of the middle-extension transform, which
is a quotient of this transform on a dense open.
