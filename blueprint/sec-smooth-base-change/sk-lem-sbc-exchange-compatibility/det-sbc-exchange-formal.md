+++
id = "det-sbc-exchange-formal"
kind = "lemma"
title = "Exchange maps of adjunctions: naturality, identity and pasting"
uses = ["def-weil-pbc-proetale-operations"]
+++
For every cartesian square $X'\xrightarrow{u}X$, $f':X'\to Y'$, $f:X\to Y$,
$g:Y'\to Y$ and every coefficient ring $\Lambda$, let
$\operatorname{Ex}_{g,f}(K):g^*Rf_*K\to Rf'_*u^*K$ be the adjoint transpose, for
$f'^*\dashv Rf'_*$, of $f'^*g^*Rf_*K\simeq u^*f^*Rf_*K\xrightarrow{u^*\epsilon_f}u^*K$,
for the adjunctions $Lu^*\dashv Ru_*$ of [def-weil-pbc-proetale-operations].

1. **(1)** $K\mapsto\operatorname{Ex}_{g,f}(K)$ is a natural transformation
   $g^*Rf_*\to Rf'_*u^*$ of functors
   $D(X_{\mathrm{pro\acute et}},\Lambda)\to D(Y'_{\mathrm{pro\acute et}},\Lambda)$.
2. **(2)** For the identity square ($g=\mathrm{id}_Y$, $u=\mathrm{id}_X$, $f'=f$),
   $\operatorname{Ex}_{\mathrm{id},f}$ is the identity of $Rf_*$, after the identifications
   $\mathrm{id}^*=\mathrm{id}$.
3. **(3)** For a second cartesian square $X''\xrightarrow{u'}X'$, $f'':X''\to Y''$,
   $h:Y''\to Y'$, the exchange map of the outer rectangle (base change $gh$) is the composite

   $$
   h^*g^*Rf_*K\xrightarrow{\ h^*\operatorname{Ex}_{g,f}(K)\ }h^*Rf'_*u^*K
   \xrightarrow{\ \operatorname{Ex}_{h,f'}(u^*K)\ }Rf''_*u'^*u^*K
   $$

   under the composition isomorphisms $(gh)^*\simeq h^*g^*$ and $(uu')^*\simeq u'^*u^*$.
   For composable $X\xrightarrow{f}Y\xrightarrow{e}Z$ and a base change $Z'\to Z$, the exchange map
   for $ef$ is likewise the composite of the exchange map for $e$ applied to $Rf_*K$ with
   $Re'_*$ of the exchange map for $f$.
