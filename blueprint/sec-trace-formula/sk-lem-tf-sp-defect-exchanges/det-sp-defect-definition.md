+++
id = "det-sp-defect-definition"
kind = "definition"
title = "Specialization to the normal cone and its defect"
uses = ["det-sp-dnc-definition", "det-sp-nearby-cycles-exchanges", "det-sp-constant-family-vanishing"]
+++
Let $X$ be a separated finite-type $k$-scheme, $i\colon Z\hookrightarrow X$ a closed subscheme,
and $\mathcal D_ZX$, $N_ZX$, $\widetilde e\colon Z\times S\hookrightarrow\mathcal D_ZX$ and
$e\colon Z\hookrightarrow N_ZX$ as in [det-sp-dnc-definition]. For
$L\in D^b_c(X_{\mathrm{\acute et}},A)$ let $L_\eta$ be its pullback to the generic fibre $X_\eta$ of
$\mathcal D_ZX$.

1. The *specialization functor*
   $\operatorname{Sp}_{X,Z}\colon D^b_c(X_{\mathrm{\acute et}},A)\to D^b_c((N_ZX)_{\mathrm{\acute et}},A)$
   is $\operatorname{Sp}_{X,Z}(L)=R\Psi_{\mathcal D_ZX}(L_\eta)$, with $R\Psi$ as in
   [det-sp-nearby-cycles-exchanges].
1. The *zero-section map* is the natural transformation

   $$
   \epsilon_{X,Z}(L):e^*\operatorname{Sp}_{X,Z}(L)
   \longrightarrow R\Psi_{Z\times S}((i^*L)_\eta)\xrightarrow{\sim}i^*L,
   $$

   the pullback exchange of [det-sp-nearby-cycles-exchanges] along $\widetilde e$ followed by the
   inverse of the specialization unit $\sigma_Z(i^*L)$, which is invertible by
   [det-sp-constant-family-vanishing].
1. The *defect* is $C_{X,Z}(L)=\operatorname{cofib}(\epsilon_{X,Z}(L))$ in
   $D^b_c(Z_{\mathrm{\acute et}},A)$, computed in a derived enhancement, so that $C_{X,Z}$ is an
   exact functor.
