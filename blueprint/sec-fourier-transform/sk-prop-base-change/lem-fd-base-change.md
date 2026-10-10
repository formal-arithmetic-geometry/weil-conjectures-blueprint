+++
id = "lem-fd-base-change"
kind = "lemma"
title = "Base change of the transform"
order = 2703
lean = ["AlgebraicGeometry.Etale.fourierTransformBaseChangeIso"]
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-pbc-scheme-conventions", "lem-fd-as-lisse", "sbc-prop-extension-by-zero-and-arbitrary-base-change", "thm-weil-pbc-qbar"]
+++
Let $g:S'\to S$ be a morphism of separated finite-type schemes over $k_0$, and let $V'=V\times_SS'$. For $K\in D^b_c(V,E)$ there is a canonical identification

$$
\operatorname{FT}_\psi(g^*K)\cong g^*\operatorname{FT}_\psi(K).
$$
