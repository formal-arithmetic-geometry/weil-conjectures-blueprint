+++
id = "sk-def-pe-derived-completion"
kind = "definition"
title = "Derived adic completeness"
order = 1219
uses = ["sk-prop-sf-open-closed-triangle"]
tags = ["sketch"]
+++
We treat integral coefficients through their reductions modulo powers of $\pi_E$. This is
possible for complexes that are recovered from their reductions, the derived complete ones.
Derived completeness is the analogue for complexes of the condition
$M=\varprojlim_nM/\pi_E^nM$ on a module. For example, $\mathcal O_{E,X}$ itself is derived
complete, while $E_X$ is not, since all its reductions vanish.

Let $E/\Ql$ be finite, with uniformizer $\pi_E$, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and $(\mathcal O_E/\pi_E^n)_X$ be
the integral and finite coefficient sheaves of
[det-def-sfb-pulled-back-coefficients]. A complex
$K\in D(X_{\Proet},\mathcal O_E)$ is *derived complete* if its canonical map

$$
K\longrightarrow R\varprojlim_n\bigl(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X\bigr)
$$

is an isomorphism. For
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$, the canonical
transitions satisfy the derived reduction identities
$K_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq K_n$;
a compatible tower with these identities is called *normalized*.

Normalization is a property of the complexes $K_n$. Their cohomology sheaves
$H^q(K_n)$ in general do not form a normalized tower under the ordinary
tensor product.
