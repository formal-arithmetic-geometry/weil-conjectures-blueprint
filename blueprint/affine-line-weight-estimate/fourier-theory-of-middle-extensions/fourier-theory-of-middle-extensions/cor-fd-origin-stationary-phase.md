+++
id = "cor-fd-origin-stationary-phase"
kind = "theorem"
title = "The origin fiber is the stationary-phase contribution"
order = 4238
tags = ["latex:corollary"]
uses = ["def-fd-nonexceptional", "def-fd-transform", "def-weil-ordinary-compact-cohomology", "def-wf-middle-extension", "lem-fd-hc2-vanishing", "lem-fd-stalk-at-origin", "lem-wf-boundary-stalk-invariants"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and let $\mathcal M$ be
irreducible and lisse on $U_0$, unramified at infinity, with
Fourier-nonexceptional middle
extension, and suppose the Fourier transform takes the middle-extension
shape
$\operatorname{FT}_\psi(j_{!*}\mathcal M[1])=j'_{!*}\mathcal M'[1]$
of [def-fd-transform] (the perverse shape certified in the
middle-extension input). Then the degree $-1$ part of the fiber at
the origin of the dual line is the $H_c^1$-term of the local Fourier
exact sequence at the origin:

$$
\mathcal H^{-1}\Bigl(\operatorname{FT}_\psi(j_{!*}\mathcal M[1])_{0'}\Bigr)
\cong H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)\;=\;\bigl(\mathcal M'_{\bar\eta}\bigr)^{I_{0'}},
$$

the second identification being the invariants of the local inertia
$I_{0'}$ at the origin of the dual line: the stationary phase term is
therefore the origin part of the transformed middle extension.

## Proof

The first identification is [lem-fd-stalk-at-origin]: the fiber of
the transform at the origin is $R\Gamma_c(\mathbf A^1,j_*\mathcal M)[1]$,
whose degree $-1$ part is $H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$,
while its degree $0$ part is
$H_c^2(\mathbf A^1_{k_0},j_*\mathcal M)$, which vanishes by
[lem-fd-hc2-vanishing] — the input $\mathcal M$ is irreducible
with irreducible geometric representation by the datum, and
nongeometrically-constant by
Fourier-nonexceptionality.

For the second identification, the transformed object has the shape
$j'_{!*}\mathcal M'[1]$ of [def-wf-middle-extension], a single
sheaf placed in degree $-1$; its fiber at the boundary point $0'$ of
the dual line is therefore concentrated in degree $-1$, and there it
is the boundary stalk of the middle extension,
$\bigl(j'_{!*}\mathcal M'\bigr)_{0'} =\bigl(\mathcal M'_{\bar\eta}\bigr)^{I_{0'}}$, the inertia invariants of
the local geometric generic stalk, by the boundary-stalk description of
[lem-wf-boundary-stalk-invariants]. Comparing the two descriptions
of the degree $-1$ part of the same fiber gives the displayed
identification, in the compact-support convention of
[def-weil-ordinary-compact-cohomology].
