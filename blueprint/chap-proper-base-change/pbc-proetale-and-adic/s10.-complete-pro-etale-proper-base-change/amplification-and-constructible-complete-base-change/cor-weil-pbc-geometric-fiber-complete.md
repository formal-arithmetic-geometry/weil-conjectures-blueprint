+++
id = "cor-weil-pbc-geometric-fiber-complete"
kind = "theorem"
title = "Complete-adic geometric-fiber formula"
order = 2029
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-etale-origin-witness", "lem-weil-pbc-completed-map-reduction", "thm-weil-pbc-complete-proetale"]
tags = ["latex:corollary"]
+++
In the setup of the finite-level geometric-fiber corollary, let $(A,I)$
satisfy the adic coefficient datum and let $K\in D(X_{\Proet},A)$ satisfy
the completeness and compatible etale-origin
[def-weil-pbc-etale-origin-witness] hypotheses of
[thm-weil-pbc-complete-proetale]. Then the completed-pullback exchange
morphism is an isomorphism
$$
 L\bar y^*_{\mathrm{comp}}Rf_*K
 \xrightarrow{\sim}
 Ra_{\bar y,*}L(i_{\bar y})^*_{\mathrm{comp}}K
 \quad\text{in }D((\operatorname{Spec}\Omega)_{\Proet},A).
$$
Its reduction modulo $I^n$ is the finite-level pro-etale geometric-fiber
isomorphism for $K_n$.

## Proof

Specialize [thm-weil-pbc-complete-proetale] to the geometric-point base
change; the reduction statement is the finite reduction of
[lem-weil-pbc-completed-map-reduction].
