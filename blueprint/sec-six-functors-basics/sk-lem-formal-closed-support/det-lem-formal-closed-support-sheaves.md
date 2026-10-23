+++
id = "det-lem-formal-closed-support-sheaves"
kind = "lemma"
title = "Sections with support: the sheaf-level adjunction"
order = 2154
uses = ["sk-prop-sf-open-closed-triangle", "sk-prop-sfb-cartesian-coefficients"]
+++
Let $\Lambda$ be admissible, let $X$ be a standing scheme, and let
$i\colon Z\hookrightarrow X$ be a closed immersion with open complement
$j\colon V\hookrightarrow X$. Use $\Lambda_Z=i^{-1}\Lambda_X$ and
$\Lambda_V=j^{-1}\Lambda_X$ as coefficient rings
([sk-prop-sfb-cartesian-coefficients]). For
$M\in\Mod(X_{\mathrm{proét}},\Lambda)$ put
$\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$, where $M\to j_*j^*M$ is the
unit of $j^*\dashv j_*$.

1. $\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$, naturally in $M$.
2. $\underline\Gamma_Z\colon\Mod(X_{\mathrm{proét}},\Lambda)\to\Mod(Z_{\mathrm{proét}},\Lambda)$
   is right adjoint to the exact functor
   $i_*\colon\Mod(Z_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$;
   in particular it is left exact and preserves limits.
3. $\underline\Gamma_Z$ sends K-injective complexes to K-injective complexes,
   and injective modules to injective modules.
