+++
id = "cor-a1-fourier-middle-hc1"
kind = "theorem"
title = "Fourier bound for middle-extension cohomology"
order = 2985
tags = ["latex:corollary"]
uses = ["cor-fd-origin-hc1-bound", "def-fd-nonexceptional", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-middle-extension", "lem-fd-realified-kernel-real", "p-linear-filtration"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion and
let $\mathcal M$ be an irreducible
lisse Weil sheaf on
$U_0$, unramified at infinity,
punctually $\iota$-pure of weight
$w$, with irreducible geometric fundamental representation of
[def-wf-fundamental-representation] and
Fourier-nonexceptional
middle extension
$j_*\mathcal M$. Then
$H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$ has
weights at most $w+1$.

## Proof

The ordinary middle extension of [def-wf-middle-extension]
fits into the short exact sequence

$$
0\to j_!\mathcal M\to j_*\mathcal M\to i_*i^*j_*\mathcal M\to0.
$$

The finite-support last term has no positive compact-support
cohomology. The long exact sequence therefore gives a
Frobenius-equivariant surjection
$H_c^1(U_0,\mathcal M)\twoheadrightarrow H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$.
The source has weights at most $w+1$ by
[cor-fd-origin-hc1-bound]. By [p-linear-filtration], eigenvalues on a quotient are among
those of the source, so the same bound holds in the convention of
[def-weil-punctual-weights].
