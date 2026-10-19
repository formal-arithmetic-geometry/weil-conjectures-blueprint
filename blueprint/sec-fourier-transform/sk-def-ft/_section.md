+++
id = "sk-def-ft"
kind = "definition"
title = "The Fourier–Deligne transform"
order = 3036
uses = ["sk-def-kernel", "sk-lem-as-properties", "sk-def-sf-setting", "sk-def-sfb-module-derived-lower-shriek", "sk-prop-sf-comp-coherence", "sk-prop-ctf-finite-comparison"]
tags = ["sketch"]
+++
With $\Lambda$, $\pi:V\to S$, $\pi':V'\to S$, $b$, $\Psi$ and the kernel
$\mathcal K_\psi$ of [sk-def-kernel], where $\Lambda$ is an admissible
coefficient ring regarded as a condensed ring ([sk-def-sf-setting]), let
$p_1:V\times_SV'\to V$ and $p_2:V\times_SV'\to V'$ be the projections, fix a
compactification of $p_2$, and let $r\in\mathbf Z$. The *Fourier–Deligne
transform* is the functor between the derived categories of
$\Lambda$-modules on the pro-étale sites

$$
\FT_\psi:D(V_{\mathrm{proét}},\Lambda)\to D(V'_{\mathrm{proét}},\Lambda),\qquad
\FT_\psi(K):=Rp_{2,!}\bigl(Lp_1^*K\otimes^L_\Lambda\mathcal K_\psi\bigr)[r],
$$

$\mathcal K_\psi$ being placed in degree $0$ and $Rp_{2,!}$ the derived lower
shriek of module objects for the chosen compactification
([sk-def-sfb-module-derived-lower-shriek]). On $\Dbc$ (on $\Dctf$ for finite
$\Lambda$) it does not depend on the compactification
([sk-prop-sf-comp-coherence]). In the application $V_0\to S_0$ is a vector
bundle of rank $r$ and $V'=V_0^\vee$ (Laumon's normalization); the transform
with the inverse character is the same construction with $\Psi^{-1}$ in
place of $\Psi$. On $\Aone$ one has $r=1$ and
$\FT_\psi(K)=Rp_{2,!}(p_1^*K\otimes^L\mathcal K_\psi)[1]$.

For a finite ring $\Lambda$ the same formula on the small étale sites,
$D(V_{\mathrm{\acute et}},\Lambda)\to D(V'_{\mathrm{\acute et}},\Lambda)$,
defines the étale transform; for finite admissible $\Lambda$ it corresponds
to $\FT_\psi$ under $\nu^*$ ([sk-prop-ctf-finite-comparison]). For
$\Lambda=\mathcal O_E,E,\Qlb$ only the pro-étale transform is used.
