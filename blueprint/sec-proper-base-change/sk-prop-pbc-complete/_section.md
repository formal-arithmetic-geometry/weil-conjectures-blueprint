+++
id = "sk-prop-pbc-complete"
kind = "proposition"
title = "Proper base change for complete integral complexes"
order = 2018
uses = ["sk-cor-pbc-proet-finite", "sk-thm-properbasechange", "sk-def-pe-derived-completion"]
tags = ["sketch"]
+++
The passage from finite coefficients to $\mathcal O_E$ is a question of
completeness. The inverse image
$g^*:D(Y_{\mathrm{proét}},\mathcal O_E)\to D(Y'_{\mathrm{proét}},\mathcal O_E)$,
which is exact on sheaves of modules, need not preserve derived completeness. For
$M\in D(Y_{\mathrm{proét}},\mathcal O_E)$, we define its *completed inverse image*
$g^*_{\mathrm{comp}}M\in D(Y'_{\mathrm{proét}},\mathcal O_E)$ by

$$
g^*_{\mathrm{comp}}M=R\varprojlim_ng^*\bigl(M\otimes^{\mathbf L}_{\mathcal O_{E,Y}}(\mathcal O_E/\pi_E^n)_Y\bigr).
$$

For $Y$ and $Y'$ of finite type over $k$ and $M\in\Dctf(Y,\mathcal O_E)$, the
criterion for integral constructibility and the finite constant local models
([sk-prop-integral-criterion], [sk-def-sfb-constructible]) show that
$g^*_{\mathrm{comp}}M=g^*M$. Until we know that proper direct image preserves
constructibility, we can only state base change with the completed inverse
image.

In the cartesian square of [sk-cor-pbc-proet-finite] (with $p$ proper), fix
$E/\Ql$ finite. Suppose that $K\in D(X_{\mathrm{proét}},\mathcal O_E)$ is
derived $\pi_E$-complete and that each reduction

$$
K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X
$$

belongs to $D^+_{\mathrm{class}}(X_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$.
Then the completed exchange map, constructed in the proof,

$$
g^*_{\mathrm{comp}}Rp_*K\xrightarrow{\ \sim\ }Rp'_*g'^*_{\mathrm{comp}}K
$$

is an isomorphism in $D(Y'_{\mathrm{proét}},\mathcal O_E)$.
