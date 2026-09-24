+++
id = "lem-a1-fourier-ready-dichotomy"
kind = "lemma"
title = "The constant–Artin–Schreier dichotomy for a pure constituent"
order = 4277
uses = ["def-fd-artin-schreier-sheaf", "def-fd-nonexceptional", "def-weil-punctual-weights", "def-wf-constant-weil-twist", "def-wf-iota-real", "def-wf-middle-extension", "lem-wf-pure-realizable"]
+++
Let $k_0=\mathbf F_q$, let $U_0$ be a smooth geometrically connected
affine curve over $k_0$, and let $\mathcal N$ be a
punctually $\iota$-pure lisse Weil
sheaf of weight $w$ on $U_0$ whose geometric restriction is
irreducible and not constant. Then exactly one of the following holds.

1. **(i)** The geometric restriction of $\mathcal N$ is the restriction
of an Artin–Schreier sheaf
$\mathcal L_{\psi(ax)}$: geometrically, $\mathcal N$ is a constant
Weil twist of an Artin–Schreier
sheaf.
1. **(ii)** The middle extension of
$\mathcal N$ is
Fourier-nonexceptional.

In case (ii), $\mathcal N$ is
$\iota$-realizable in the sense of
[def-wf-iota-real].

## Proof

[def-fd-nonexceptional] defines the middle extension of a lisse
input to be Fourier-nonexceptional when, after geometric base change, it
is neither a constant sheaf up to a constant
Weil twist nor the restriction of
an Artin–Schreier sheaf. The two exclusions and their conjunction
therefore partition the geometric possibilities, and it remains to see
that the first exclusion is automatic under the hypotheses. Were the
geometric restriction of $\mathcal N$ a constant Weil twist of the
constant sheaf, then — the twist being of rank one and the geometric
restriction being irreducible — $\mathcal N$ would have geometric rank
one and constant geometric restriction, contrary to the hypothesis that
it is not constant. Hence the geometric restriction of $\mathcal N$
is either the restriction of an Artin–Schreier sheaf, which is (i), or
neither it nor any constant twist of the middle extension is constant,
which is exactly the defining condition of (ii); the two cases are
mutually exclusive because the second exception of
[def-fd-nonexceptional] excludes precisely the Artin–Schreier
sheaves.

For the final assertion, punctual $\iota$-purity of weight $w$ in the
sense of [def-weil-punctual-weights] is the
hypothesis of the envelope construction of
[lem-wf-pure-realizable]: with $b=\iota^{-1}(q^w)$ the sheaf
$\mathcal N\oplus(\mathcal N^\vee\otimes\mathcal B_b)$ is $\iota$-real
and $\mathcal N$ is its direct summand, so $\mathcal N$ is
$\iota$-realizable in the sense of [def-wf-iota-real].
