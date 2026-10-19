+++
id = "det-tf-ibc-pasting"
kind = "lemma"
title = "Base change along a product projection through a compactification"
uses = ["det-tf-ibc-proper-step", "det-geo-open-finiteness-base-change", "cor-fin-deligne-open-finite-coefficients", "lemma-weil-pbc-derived-exchange-coherence", "thm-nagata-compactification"]
+++
Let $A$, $f:X\to Y$, $T$, $M\in\Dbc(X,A)$, $h=f\times\operatorname{id}_T$, $p_X$ and
$p_Y$ be as in the lemma on base change along a product projection, and let
$f=\bar fj$ with $j:X\hookrightarrow\bar X$ an open immersion and $\bar f:\bar X\to Y$
proper. Write $j_T=j\times\operatorname{id}_T$, $\bar h=\bar f\times\operatorname{id}_T$
and $p_{\bar X}\colon\bar X\times T\to\bar X$. Then the base change map
$p_Y^*Rf_*M\to Rh_*p_X^*M$ equals the composite

$$
p_Y^*Rf_*M\simeq p_Y^*R\bar f_*Rj_*M
\longrightarrow R\bar h_*p_{\bar X}^*Rj_*M
\longrightarrow R\bar h_*Rj_{T*}p_X^*M\simeq Rh_*p_X^*M
$$

of the base change map for $\bar f$ applied to $Rj_*M$ and $R\bar h_*$ of the base
change map for $j$ applied to $M$. Both of these are isomorphisms, so the base change
map for $f$ is an isomorphism in $D((Y\times T)_{\mathrm{pro\acute et}},A)$.
