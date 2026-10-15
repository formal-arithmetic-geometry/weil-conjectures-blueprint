+++
id = "sk-def-pe-derived-completion"
kind = "definition"
title = "Derived adic completeness"
order = 1545
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-tensor-hom"]
tags = ["sketch"]
+++
Let $E/\Ql$ be finite, with uniformizer $\pi_E$, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and $(\mathcal O_E/\pi_E^n)_X$ be
the integral and finite coefficient sheaves of
[sk-def-sfb-pulled-back-coefficients]. A complex
$K\in D(X_{\Proet},\mathcal O_E)$ is *derived complete* if its canonical map

$$
K\longrightarrow R\varprojlim_n\bigl(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X\bigr)
$$

is an isomorphism. For
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$, the canonical
transitions satisfy the derived reduction identities
$K_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq K_n$;
a compatible tower with these identities is called *normalized*.

Normalization is a property of the complexes $K_n$; their cohomology sheaves
$H^q(K_n)$ need not form a normalized tower under the ordinary tensor product.
