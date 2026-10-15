+++
id = "pur713-def-open-exchange-module"
kind = "definition"
title = "Open-extension base-change map, module objects"
order = 2356
uses = ["pur713-def-base-changed-compactification", "sk-def-sf-exchanges", "sk-def-sf-operations"]
+++
Under the inputs of Lemmas “Module-object derived open-extension adjunction” (`pur713-lem-open-adjunction-module`, in [sk-def-sf-operations]), “The module-object derived open inverse image is levelwise” (`pur713-lem-open-pull-levelwise`, in [sk-def-sf-operations]) and “Composition comparison for module-object derived inverse image” (`pur713-lem-pull-composition-module`, in [sk-def-sf-exchanges]), in Definition [pur713-def-base-changed-compactification], for $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$ and $K\in D(X_{\Proet},T)$, define

$$
b'_{j,\bar g,T,K}:\mathrm D(j'_{!,T})Lg'^*_TK\longrightarrow L\bar g^*_T\mathrm D(j_{!,T})K
$$

as the adjoint, under Lemma “Module-object derived open-extension adjunction” (`pur713-lem-open-adjunction-module`, in [sk-def-sf-operations]) for $j'$, of the composite

$$
Lg'^*_TK\xrightarrow{Lg'^*_T(\mathrm{unit})}Lg'^*_T\mathrm D(j^*_T)\mathrm D(j_{!,T})K
\cong Lg'^*_TLj^*_T\mathrm D(j_{!,T})K
\xrightarrow{\mu_{j,g',T}}L(jg')^*_T\mathrm D(j_{!,T})K
\xrightarrow{\mu^{-1}_{\bar g,j',T}}Lj'^*_TL\bar g^*_T\mathrm D(j_{!,T})K
\cong\mathrm D(j'^*_T)L\bar g^*_T\mathrm D(j_{!,T})K,
$$

where the unnamed isomorphisms are Lemma “The module-object derived open inverse image is levelwise” (`pur713-lem-open-pull-levelwise`, in [sk-def-sf-operations]), $\mu$ is Lemma “Composition comparison for module-object derived inverse image” (`pur713-lem-pull-composition-module`, in [sk-def-sf-exchanges]), and $L(jg')^*_T=L(\bar gj')^*_T$. It is a natural transformation of functors $D(X_{\Proet},T)\to D(\overline X'_{\Proet},T)$.
