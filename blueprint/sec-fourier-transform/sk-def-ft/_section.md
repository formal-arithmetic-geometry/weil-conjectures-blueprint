+++
id = "sk-def-ft"
kind = "definition"
title = "The Fourier–Deligne transform"
order = 3036
lean = ["AlgebraicGeometry.Etale.fourierTransform"]
uses = ["sk-def-kernel", "sk-lem-as-properties"]
tags = ["sketch"]
+++
With $\Lambda$, $\pi:V\to S$, $\pi':V'\to S$, $b$, $\Psi$ and the kernel
$\mathcal K_\psi$ of [sk-def-kernel], let $p_1:V\times_SV'\to V$ and
$p_2:V\times_SV'\to V'$ be the projections, assume $p_2$ admits a
compactification, and let $r\in\mathbf Z$. The *Fourier–Deligne transform*
is the functor between the derived categories of étale sheaves of
$\Lambda$-modules

$$
\FT_\psi:D(V_{\mathrm{\acute et}},\Lambda)\to D(V'_{\mathrm{\acute et}},\Lambda),\qquad
\FT_\psi(K):=Rp_{2,!}\bigl(p_1^*K\otimes^L_\Lambda\mathcal K_\psi\bigr)[r],
$$

$\mathcal K_\psi$ being placed in degree $0$. In the application $V_0\to S_0$
is a vector bundle of rank $r$ and $V'=V_0^\vee$ (Laumon's normalization);
the transform with the inverse character is the same construction with
$\Psi^{-1}$ in place of $\Psi$. On $\Aone$ one has $r=1$ and
$\FT_\psi(K)=Rp_{2,!}(p_1^*K\otimes^L\mathcal K_\psi)[1]$.
