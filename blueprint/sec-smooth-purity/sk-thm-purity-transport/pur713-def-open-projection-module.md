+++
id = "pur713-def-open-projection-module"
kind = "definition"
title = "Open-extension projection map, module objects"
order = 2359
uses = ["sk-def-sf-exchanges", "sk-def-sf-operations"]
+++
Under the inputs of Lemmas “Module-object derived open-extension adjunction” (`pur713-lem-open-adjunction-module`, in [sk-def-sf-operations]), “The module-object derived open inverse image is levelwise” (`pur713-lem-open-pull-levelwise`, in [sk-def-sf-operations]) and “Monoidal comparison for module-object derived inverse image” (`pur713-lem-monoidal-pullback-module`, in [sk-def-sf-exchanges]), for an open immersion $j:U\hookrightarrow X$, $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, $K\in D(U_{\Proet},T)$ and $N\in D(X_{\Proet},T)$, define

$$
\sigma_{j,K,N,T}:
\mathrm D(j_{!,T})\bigl(K\otimes^L_{\mathcal R_{U,T}}\mathrm D(j^*_T)N\bigr)
\longrightarrow\mathrm D(j_{!,T})K\otimes^L_{\mathcal R_{X,T}}N
$$

as the adjoint, under Lemma “Module-object derived open-extension adjunction” (`pur713-lem-open-adjunction-module`, in [sk-def-sf-operations]), of the map $K\otimes^L_{\mathcal R_{U,T}}\mathrm D(j^*_T)N\to\mathrm D(j^*_T)(\mathrm D(j_{!,T})K\otimes^L_{\mathcal R_{X,T}}N)$ obtained by tensoring the unit at $K$ with the identity and then applying the monoidal comparison of Lemma “Monoidal comparison for module-object derived inverse image” (`pur713-lem-monoidal-pullback-module`, in [sk-def-sf-exchanges]) for $j$, with Lemma “The module-object derived open inverse image is levelwise” (`pur713-lem-open-pull-levelwise`, in [sk-def-sf-operations]).
