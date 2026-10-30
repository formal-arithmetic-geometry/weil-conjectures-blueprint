+++
id = "sk-thm-inversion"
kind = "proposition"
title = "Base change and Fourier inversion"
order = 723
uses = ["sk-lem-as-properties", "sk-lem-wft-character-integral", "sk-thm-sf-ctf-stability", "sk-prop-cohsm", "sk-thm-sfb-proper-base-change", "sk-thm-sf-package", "sk-prop-sf-open-closed-triangle", "sk-prop-an", "sk-def-sf-weil-complexes"]
tags = ["sketch"]
+++
The transform commutes with arbitrary base change on $S$, and with
tensoring by the pullback of a bounded constructible complex on $S$.
For a geometric point $\bar y$ of $V^\vee$, the proper base change map
gives

$$
(\operatorname{FT}_\psi K)_{\bar y}
\simeq
R\Gamma_c\bigl(V_{\bar y},
K|_{V_{\bar y}}\otimes
\mathcal L_{\psi\langle x,y\rangle}\bigr)[r].
\tag{18.2}
$$

Under $V^{\vee\vee}=V$ there are natural isomorphisms

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)
\simeq K(-r),
\qquad
\operatorname{FT}_{\psi}\operatorname{FT}_\psi(K)
\simeq [-1]_V^*K(-r).
$$

For a line over $k_0$, with $\delta_0$ the constant skyscraper at zero,

$$
\operatorname{FT}_\psi(E)=\delta_0(-1)[-1],
\qquad \operatorname{FT}_\psi(\delta_0)=E[1].
$$

All the maps are compatible with Weil structures and Frobenius.

*Complement.* The kernel and the transform are defined more generally for
any pairing $b$ on $V\times_SV'$ and any admissible coefficient ring (and on
the étale site for finite coefficients), and $\mathcal K_\psi$ is
multiplicative in $\psi$: $\mathcal K_\psi\otimes\mathcal K_{\psi'}\cong
\mathcal K_{\psi\psi'}$, $\mathcal K_\psi^{-1}\cong\mathcal K_{\psi^{-1}}$.
Composites of kernel transforms are kernel transforms with the convolution
kernel, and Tate twists commute with the transform.
