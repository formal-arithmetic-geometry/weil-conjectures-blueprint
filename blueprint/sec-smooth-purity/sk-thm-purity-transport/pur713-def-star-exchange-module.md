+++
id = "pur713-def-star-exchange-module"
kind = "definition"
title = "Direct-image exchange, module objects"
order = 2355
uses = ["pur713-def-pullback-comparison-module", "sk-def-sf-exchanges", "sk-def-sf-operations"]
+++
Under the inputs of Lemmas “Module-object derived inverse-image adjunction” (`pur713-lem-star-adjunction-module`, in [sk-def-sf-operations]) and “Composition comparison for module-object derived inverse image” (`pur713-lem-pull-composition-module`, in [sk-def-sf-exchanges]), for $\square$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the direct-image exchange is the natural transformation

$$
\operatorname{Ex}_{*,\square,T}:Lg^*_TRf_{*,T}\longrightarrow Rf'_{*,T}Lg'^*_T
$$

of functors $D(X_{\Proet},T)\to D(Y'_{\Proet},T)$ whose component at $K$ is the adjoint, under Lemma “Module-object derived inverse-image adjunction” (`pur713-lem-star-adjunction-module`, in [sk-def-sf-operations]) for $f'$, of

$$
Lf'^*_TLg^*_TRf_{*,T}K
\xrightarrow{c_{\square,T}}
Lg'^*_TLf^*_TRf_{*,T}K
\xrightarrow{Lg'^*_T\varepsilon_{f,T,K}}Lg'^*_TK,
$$

where $\varepsilon_{f,T}$ is the counit of $Lf^*_T\dashv Rf_{*,T}$ and $c_{\square,T}$ is Definition [pur713-def-pullback-comparison-module]. No invertibility is asserted.
