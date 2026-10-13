+++
id = "pur713-def-shriek-exchange-module"
kind = "definition"
title = "Compact-support exchange, module objects"
order = 1873
tags = ["latex:bpdefinition"]
uses = ["pur713-def-base-changed-compactification", "pur713-def-lower-shriek-module", "pur713-def-star-exchange-module", "pur713-lem-open-exchange-module"]
+++
Under the inputs of Definition [pur713-def-star-exchange-module] and Lemma [pur713-lem-open-exchange-module], for $c_f$, $c'$ as in Definition [pur713-def-base-changed-compactification] and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the compact-support exchange

$$
\operatorname{Ex}_{!,\square,T}:Lg^*_TRf_{!,T}\longrightarrow R_{c',T}Lg'^*_T,
$$

a natural transformation of functors $D(X_{\Proet},T)\to D(Y'_{\Proet},T)$ between the functors of Definition [pur713-def-lower-shriek-module], has component at $K$ the composite

$$
Lg^*_TRp_{*,T}\mathrm D(j_{!,T})K
\xrightarrow{\operatorname{Ex}_{*,\square_p,T}}Rp'_{*,T}L\bar g^*_T\mathrm D(j_{!,T})K
\xrightarrow{Rp'_{*,T}(b_{j,\bar g,T,K})}
Rp'_{*,T}\mathrm D(j'_{!,T})Lg'^*_TK,
$$

with $\operatorname{Ex}_{*,\square_p,T}$ of Definition [pur713-def-star-exchange-module] and $b$ of Lemma [pur713-lem-open-exchange-module]. This is an exchange between module-object functors; no completed pullback is inserted.
