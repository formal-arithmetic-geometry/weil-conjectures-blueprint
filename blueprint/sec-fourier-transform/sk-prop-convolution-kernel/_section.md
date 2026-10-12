+++
id = "sk-prop-convolution-kernel"
kind = "proposition"
title = "P12: the convolution of the kernels is the delta kernel"
order = 3051
lean = ["AlgebraicGeometry.Etale.fourierKernelConvolutionIso"]
uses = ["sk-lem-as-properties", "sk-prop-an", "sk-prop-kernel-lisse", "sk-prop-stalk", "sk-thm-derived-duality"]
tags = ["sketch"]
+++
Let $S=\Spec k$ and $V=\mathbf A^r_k$. Then

$$
\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi\cong
\Delta_*\underline{E}(-r)[-2r],
\qquad
\mathcal K_\psi\ast\mathcal K_\psi\cong
(\operatorname{id}\times\iota')_*\Delta_*\underline{E}(-r)[-2r],
$$

$\Delta:V\to V\times_SV$ being the diagonal and $\iota'$ the reflection of the
addition.
