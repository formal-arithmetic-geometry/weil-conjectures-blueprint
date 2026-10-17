+++
id = "det-pbc-complete-constructible"
kind = "lemma"
title = "Completed and ordinary exchange agree on constructible complexes"
order = 1404
uses = ["det-pbc-complete-exchange-map", "det-pbc-complete-exchange-iso", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-pbc-direct-image-limits", "sk-prop-integral-criterion", "det-prop-integral-criterion-reductions", "sk-thm-pe-constructible-comparison", "sk-lem-integral-models", "det-thm-sfb-proper-base-change-integral"]
+++
In the cartesian square of [det-pbc-complete-exchange-map], let $p\colon X\to Y$
be proper and $g\colon Y'\to Y$ arbitrary, with $X$, $Y$ and $Y'$ of finite type
over $k$, and let $K\in\Dbc(X,\mathcal O_E)$. Then:

1. each reduction $K_n$ lies in
   $D^+_{\mathrm{class}}(X_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$, so
   $\operatorname{Ex}^{\mathrm{comp}}_K$ is an isomorphism
   ([det-pbc-complete-exchange-iso]);
2. the completion maps $g^*Rp_*K\to g^*_{\mathrm{comp}}Rp_*K$ and
   $g'^*K\to g'^*_{\mathrm{comp}}K$ are isomorphisms;
3. under these isomorphisms $\operatorname{Ex}^{\mathrm{comp}}_K$ is the ordinary
   base change morphism, so
   $$
   \operatorname{Ex}_K\colon g^*Rp_*K\xrightarrow{\ \sim\ }Rp'_*g'^*K
   \qquad\text{in }\Dbc(Y',\mathcal O_E).
   $$
