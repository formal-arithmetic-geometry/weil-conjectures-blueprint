+++
id = "lem-fd-base-change"
kind = "lemma"
title = "Base change of the transform"
order = 3047
lean = ["AlgebraicGeometry.Etale.fourierTransformBaseChangeIso"]
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-pbc-scheme-conventions", "lem-fd-as-lisse", "sk-def-sfb-bounded-constructible", "sk-def-sfb-open-base-change", "sk-thm-sfb-proper-base-change", "sk-thm-sfb-shriek-base-change"]
+++
Let $g:S'\to S$ be a morphism of separated finite-type schemes over $k_0$, and let $V'=V\times_SS'$. For $\Lambda=E$ or $\overline{\mathbf Q}_\ell$ and $K\in D^b_c(V,\Lambda)\subset D(V_{\mathrm{proét}},\Lambda)$ ([sk-def-sfb-bounded-constructible]) there is a canonical identification

$$
\operatorname{FT}_\psi(g^*K)\cong g^*\operatorname{FT}_\psi(K).
$$
