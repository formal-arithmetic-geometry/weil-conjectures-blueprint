+++
id = "prop-weil-pbc-direct-image-limits"
kind = "theorem"
title = "Direct image, derived limits, and completeness"
order = 1344
uses = ["det-pbc-complete-towers", "det-pbc-complete-tower-calculus", "def-weil-derived-limit", "sk-prop-pe-milnor", "det-pe-derived-nakayama-resolution", "sk-def-pe-derived-completion", "def-weil-pbc-projection-formula-map", "lemma-weil-pbc-perfect-projection-formula"]
tags = ["latex:proposition"]
+++
Let $f\colon X\to Y$ be a morphism of schemes, and use the tower categories,
reduction towers and completion maps of [det-pbc-complete-towers] over
$\mathcal O_{E,X}$ and $\mathcal O_{E,Y}$.

1. For every $M_\bullet\in D(\operatorname{Tow}(X))$ the canonical map
   $$
    Rf_*R\varprojlim M_\bullet\xrightarrow{\sim}R\varprojlim\bigl(Rf_*^{\operatorname{Tow}}M_\bullet\bigr)
   $$
   is an isomorphism, with $\operatorname{ev}_nRf_*^{\operatorname{Tow}}M_\bullet\simeq Rf_*M_n$.
   Under the Milnor cones of [sk-prop-pe-milnor] (derived limits in the sense of
   [def-weil-derived-limit]) it is induced by
   $Rf_*\prod_nM_n\simeq\prod_nRf_*M_n$ and its commutation with $1-T$.
2. For every $K\in D(X_{\mathrm{proét}},\mathcal O_E)$ there is a canonical
   isomorphism
   $$
    \operatorname{red}(Rf_*K)\xrightarrow{\sim}Rf_*^{\operatorname{Tow}}\operatorname{red}(K)
   $$
   in $D(\operatorname{Tow}(Y))$, natural in $K$. Its level $n$ is the
   projection-formula isomorphism
   $(Rf_*K)\otimes^{\mathbf L}_{\mathcal O_{E,Y}}(\mathcal O_E/\pi_E^n)_Y\xrightarrow{\sim}
   Rf_*K_n$ of [def-weil-pbc-projection-formula-map] and
   [lemma-weil-pbc-perfect-projection-formula], so these isomorphisms commute
   with the reductions $(\mathcal O_E/\pi_E^{n+1})\to(\mathcal O_E/\pi_E^n)$.
3. Under (1) and (2), the completion map of $Rf_*K$ is
   $$
    Rf_*K\xrightarrow{Rf_*\kappa_K}Rf_*R\varprojlim\operatorname{red}(K)
    \xrightarrow{\sim}R\varprojlim Rf_*^{\operatorname{Tow}}\operatorname{red}(K)
    \simeq R\varprojlim\operatorname{red}(Rf_*K).
   $$
   In particular, if $K$ is derived $\pi_E$-complete
   ([sk-def-pe-derived-completion]), then so is $Rf_*K$, and
   $Rf_*K\simeq R\varprojlim_nRf_*K_n$.
