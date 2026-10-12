+++
id = "def-fd-transform"
kind = "definition"
title = "The Fourier–Deligne transform"
order = 2997
lean = ["AlgebraicGeometry.Etale.fourierTransform"]
uses = ["def-fd-kernel", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions"]
+++
Let $\Lambda$, $p$, $\pi:V\to S$, $\pi':V'\to S$, the pairing $b$, the
character $\Psi$ and the Fourier kernel $\mathcal K_\psi$ on
$V\times_SV'$ be as in [def-fd-kernel], let
$p_1:V\times_SV'\to V$ and $p_2:V\times_SV'\to V'$ be the projections,
and assume that $p_2$ admits a compactification, so that the
compact-support direct image $Rp_{2,!}$ is defined. For $r\in\mathbf Z$,
the *Fourier–Deligne transform* is the functor

$$
\operatorname{FT}_\psi:D(V_{\mathrm{\acute et}},\Lambda)\longrightarrow
D(V'_{\mathrm{\acute et}},\Lambda),\qquad
\operatorname{FT}_\psi(K):=Rp_{2,!}\bigl(p_1^*K\otimes^L_\Lambda\mathcal K_\psi\bigr)[r],
$$

between the derived categories of étale sheaves of $\Lambda$-modules,
where $\mathcal K_\psi$ is regarded as a complex concentrated in degree $0$
and $p_1^*$ is the derived pullback. In the application of
[def-fd-kernel], $V_0\to S_0$ is a vector bundle of rank $r$,
$V'=V_0^\vee$, and the shift $[r]$ by the relative dimension is Laumon's
normalization. The transform $\operatorname{FT}_{\psi^{-1}}$ is the same
construction with $\Psi^{-1}$ in place of $\Psi$.
