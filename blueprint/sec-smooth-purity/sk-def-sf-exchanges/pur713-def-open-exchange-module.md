+++
id = "pur713-def-open-exchange-module"
kind = "definition"
title = "Open-extension base-change map, module objects"
order = 1868
tags = ["latex:bpdefinition"]
uses = ["pur713-def-base-changed-compactification", "pur713-lem-open-adjunction-module", "pur713-lem-open-pull-levelwise", "pur713-lem-pull-composition-module"]
+++
Under the inputs of Lemmas [pur713-lem-open-adjunction-module], [pur713-lem-open-pull-levelwise] and [pur713-lem-pull-composition-module], in Definition [pur713-def-base-changed-compactification], for $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$ and $K\in D(X_{\Proet},T)$, define

$$
b'_{j,\bar g,T,K}:\mathrm D(j'_{!,T})Lg'^*_TK\longrightarrow L\bar g^*_T\mathrm D(j_{!,T})K
$$

as the adjoint, under Lemma [pur713-lem-open-adjunction-module] for $j'$, of the composite

$$
Lg'^*_TK\xrightarrow{Lg'^*_T(\mathrm{unit})}Lg'^*_T\mathrm D(j^*_T)\mathrm D(j_{!,T})K
\cong Lg'^*_TLj^*_T\mathrm D(j_{!,T})K
\xrightarrow{\mu_{j,g',T}}L(jg')^*_T\mathrm D(j_{!,T})K
\xrightarrow{\mu^{-1}_{\bar g,j',T}}Lj'^*_TL\bar g^*_T\mathrm D(j_{!,T})K
\cong\mathrm D(j'^*_T)L\bar g^*_T\mathrm D(j_{!,T})K,
$$

where the unnamed isomorphisms are Lemma [pur713-lem-open-pull-levelwise], $\mu$ is Lemma [pur713-lem-pull-composition-module], and $L(jg')^*_T=L(\bar gj')^*_T$. It is a natural transformation of functors $D(X_{\Proet},T)\to D(\overline X'_{\Proet},T)$.
