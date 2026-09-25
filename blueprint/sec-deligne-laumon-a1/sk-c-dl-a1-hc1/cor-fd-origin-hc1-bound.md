+++
id = "cor-fd-origin-hc1-bound"
kind = "theorem"
title = "The origin fibre of the transform carries the $H^1_c$-bound; the Kiehl–Weissauer Claim 1.6.3"
order = 2984
tags = ["latex:corollary"]
uses = ["def-fd-transform", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "lem-fd-realified-kernel-real", "lem-fd-stalk-at-origin", "lem-fd-transform-concentration", "lem-fd-transform-hc0-vanishing", "lem-wf-l2-constructible-rigidity", "prop-fd-l2-upper-weight-shift", "thm-fd-transform-mixed"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and $\mathcal M$ be as in
[lem-fd-realified-kernel-real] — a dense open immersion and an
irreducible lisse Weil
sheaf, unramified at infinity,
punctually $\iota$-pure of weight
$w$ — and put $\mathcal G':=\operatorname{FT}_\psi(j_!\mathcal M)$, the
Fourier–Deligne transform. Then the fibre
of $\mathcal G'$ at the origin of the dual line has weights at most
$w+1$; and, identifying that fibre with the compact-support cohomology
by [lem-fd-stalk-at-origin], every eigenvalue $\alpha$ of the local
Frobenius on
$\hyperref[def:weil-ordinary-compact-cohomology]{H^1_c} (\mathbf A^1_{k_0},j_!\mathcal M)=H^1_c(U,\mathcal M)$ satisfies

$$
|\iota(\alpha)|^2\le q^{w+1}.
$$

## Proof

By [lem-fd-transform-concentration], the transform
$\mathcal G'$ is a sheaf. By [lem-fd-stalk-at-origin], its
origin stalk is $H_c^1(U,\mathcal M)$.
If $\mathcal G'=0$, the assertion is immediate.
Otherwise [thm-fd-transform-mixed] supplies mixedness, namely a
finite filtration with punctually pure graded pieces as in
[def-weil-punctual-weights].
Moreover [lem-fd-transform-hc0-vanishing] gives
$H_c^0(\mathbf A^1,\mathcal G')=0$.
Thus the sheaf version of the dictionary
[lem-wf-l2-constructible-rigidity] applies: every stalk has
weights at most $W=\|\mathcal G'\|$.
The Plancherel estimate [prop-fd-l2-upper-weight-shift] gives
$W\leq w+1$. This proves the claimed bound at the origin.
