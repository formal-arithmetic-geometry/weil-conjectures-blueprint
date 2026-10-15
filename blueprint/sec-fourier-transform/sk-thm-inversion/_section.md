+++
id = "sk-thm-inversion"
kind = "theorem"
title = "P13: invertibility of the transform"
order = 3059
lean = ["AlgebraicGeometry.Etale.nonempty_iso_affineFourierTransform_comp_inv", "AlgebraicGeometry.Etale.nonempty_iso_affineFourierTransform_comp_self"]
uses = ["sk-lem-kernel-composition", "sk-prop-convolution-kernel"]
tags = ["sketch"]
+++
Let $V\cong\mathbf A^r_k$ and let $K$ be a constructible Weil complex on $V$;
let $\iota':V\to V$ be the reflection of the addition. Then there are
functorial isomorphisms

$$
\FT_{\psi^{-1}}\FT_\psi(K)\cong K(-r),\qquad
\FT_\psi\FT_\psi(K)\cong{\iota'}^*K(-r).
$$
