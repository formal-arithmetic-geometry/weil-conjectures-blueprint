+++
id = "lem-fd-convolution-kernel"
kind = "lemma"
title = "The convolution of the Fourier kernels is the delta kernel"
order = 3058
uses = ["def-pod-perfect-complex-on-x", "def-wf-tate-twist", "fix-prop-projection-formula", "lem-fd-as-cover-affine-line", "lem-fd-as-lisse", "lem-fd-cohomology-affine-line-character", "lem-fd-kernel-composition", "lem-fd-stalk-formula", "prop-kernel-lisse", "thm-pod-degreewise-perfectness-over-a-field", "thm-pur-vector-bundle-thom", "sk-def-sf-setting"]
+++
Let $S=\Spec k$ and $V=\mathbf A^r_k$, and work with the coefficient ring
$\overline{\mathbf Q}_\ell$ of [sk-def-sf-setting], in
$D^b_c(V\times_SV,\overline{\mathbf Q}_\ell)\subset D((V\times_SV)_{\mathrm{proét}},\overline{\mathbf Q}_\ell)$. Then

$$
\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi\cong
\Delta_*\overline{\mathbf Q}_\ell(-r)[-2r],
\qquad
\mathcal K_\psi\ast\mathcal K_\psi\cong
(\operatorname{id}\times\iota')_*\Delta_*\overline{\mathbf Q}_\ell(-r)[-2r],
$$

where $\Delta:V\to V\times_SV$ is the diagonal and $\iota'$ is the inverse
of the addition.
