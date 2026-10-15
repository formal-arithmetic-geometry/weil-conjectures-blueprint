+++
id = "sk-prop-pbc-complete"
kind = "proposition"
title = "Proper base change for complete integral complexes"
order = 1066
uses = ["sk-cor-pbc-proet-finite", "sk-def-pe-derived-completion"]
tags = ["sketch"]
+++
To pass from finite coefficients to $\mathcal O_E$ one has to deal with
completeness: the inverse image
$g^*:D(Y_{\mathrm{proét}},\mathcal O_E)\to D(Y'_{\mathrm{proét}},\mathcal O_E)$,
exact on module sheaves, need not preserve derived completeness. For
$M\in D(Y_{\mathrm{proét}},\mathcal O_E)$ define its *completed inverse image*
$g^*_{\mathrm{comp}}M\in D(Y'_{\mathrm{proét}},\mathcal O_E)$ by

$$
g^*_{\mathrm{comp}}M=R\varprojlim_ng^*\bigl(M\otimes^{\mathbf L}_{\mathcal O_{E,Y}}(\mathcal O_E/\pi_E^n)_Y\bigr).
$$

This statement holds for arbitrary schemes. (Under the finite-type
$k$-scheme assumptions, the completed inverse image of a constructible
integral complex agrees with $g^*$, by the integral constructibility
criterion and the finite constant local models.)

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
