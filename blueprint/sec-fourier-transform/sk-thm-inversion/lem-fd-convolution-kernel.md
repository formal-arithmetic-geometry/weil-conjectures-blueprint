+++
id = "lem-fd-convolution-kernel"
kind = "lemma"
title = "The convolution of the Fourier kernels is the delta kernel"
order = 4173
uses = ["def-wf-tate-twist", "def-fd-kernel", "lem-fd-kernel-composition", "prop-kernel-lisse", "lem-fd-as-lisse", "lem-wft-as-unit-trivialization", "lem-fd-character-integral", "lem-fd-stalk-formula", "sk-prop-sf-open-closed-triangle", "thm-pur-vector-bundle-thom", "def-sf-setting"]
+++
Let $S$ be a separated finite-type $k_0$-scheme and $V\to S$ a vector bundle
of rank $r$, identified with $V^{\vee\vee}$, and let $\Lambda=E$ or
$\overline{\mathbf Q}_\ell$ ([def-sf-setting]). Let $r_{ij}$ be the
projections of $V\times_SV^\vee\times_SV$ and put

$$
C=Rr_{13!}\bigl(r_{12}^*\mathcal K_\psi\otimes r_{23}^*\mathcal K_{\psi^{-1}}\bigr)
\in\Dbc(V\times_SV,\Lambda),
$$

the unshifted convolution kernel $\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi$ of
[lem-fd-kernel-composition]. Then there is a canonical isomorphism

$$
\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi\cong
\Delta_*\Lambda_V(-r)[-2r],
\qquad\text{and likewise}\qquad
\mathcal K_\psi\ast\mathcal K_\psi\cong
(\operatorname{id}\times\iota')_*\Delta_*\Lambda_V(-r)[-2r],
$$

where $\Delta:V\to V\times_SV$ is the diagonal and $\iota'=[-1]_V$ is the
inverse of the addition. The isomorphism is the composite of the
localization isomorphism $C\cong\Delta_*\Delta^*C$, the unit
trivialization of the character sheaf on the diagonal and the vector-bundle
trace of $V^\vee$.
