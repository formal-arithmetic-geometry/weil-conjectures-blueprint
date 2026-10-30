+++
id = "sk-def-pe-derived-completion"
kind = "definition"
title = "Derived adic completeness"
order = 121
uses = ["sk-prop-sf-open-closed-triangle"]
tags = ["sketch"]
+++
Let $E/\Ql$ be finite, with uniformizer $\pi_E$, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and
$(\mathcal O_E/\pi_E^n)_X$ be the integral and finite coefficient
sheaves of Section [sec-n-coefficients]. A complex $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ is
*derived complete* if its canonical map

$$
K\longrightarrow R\varprojlim_n
(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^{n})_X)
$$

is an isomorphism. For $K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^{n})_X$,
the canonical transition maps induce isomorphisms
$K_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^{n})_X\simeq K_n$;
a compatible tower with these isomorphisms is called *normalized*.
