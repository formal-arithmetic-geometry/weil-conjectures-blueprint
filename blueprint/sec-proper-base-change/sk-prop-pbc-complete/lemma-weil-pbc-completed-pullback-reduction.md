+++
id = "lemma-weil-pbc-completed-pullback-reduction"
kind = "lemma"
title = "Reduction commutes with completed pullback"
order = 1330
uses = ["det-pbc-complete-towers", "det-pbc-complete-tower-calculus", "det-pbc-complete-derived-completion", "sk-def-pe-derived-completion", "det-pe-derived-nakayama-resolution", "sk-prop-sfb-module-pullback-exact"]
+++
Let $g\colon T'\to T$ be a morphism of schemes and
$M\in D(T_{\mathrm{proét}},\mathcal O_E)$. The *completed inverse image* is

$$
g^*_{\mathrm{comp}}M=R\varprojlim\bigl(g^*_{\operatorname{Tow}}\operatorname{red}(M)\bigr)
=R\varprojlim_ng^*\bigl(M\otimes^{\mathbf L}_{\mathcal O_{E,T}}(\mathcal O_E/\pi_E^n)_T\bigr)
\in D(T'_{\mathrm{proét}},\mathcal O_E),
$$

in the notation of [det-pbc-complete-towers]. Then:

1. there is a canonical isomorphism
   $g^*_{\operatorname{Tow}}\operatorname{red}(M)\simeq\operatorname{red}(g^*M)$ in
   $D(\operatorname{Tow}(T'))$, natural in $M$, whose level $n$ is
   $g^*(M_n)\simeq(g^*M)_n$; hence $g^*_{\mathrm{comp}}M\simeq\widehat{g^*M}$ is the
   derived completion of $g^*M$;
2. $g^*_{\mathrm{comp}}M$ is derived $\pi_E$-complete, and for every $n$ there is
   an isomorphism $(g^*_{\mathrm{comp}}M)\otimes^{\mathbf L}_{\mathcal O_{E,T'}}
   (\mathcal O_E/\pi_E^n)_{T'}\simeq g^*M_n$, functorial in $M$ and compatible
   with the transition maps;
3. the completion map $\kappa_{g^*M}\colon g^*M\to g^*_{\mathrm{comp}}M$ is an
   isomorphism if and only if $g^*M$ is derived $\pi_E$-complete.
