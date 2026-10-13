+++
id = "pur713-def-open-projection-module"
kind = "definition"
title = "Open-extension projection map, module objects"
order = 1879
tags = ["latex:bpdefinition"]
uses = ["pur713-lem-monoidal-pullback-module", "pur713-lem-open-adjunction-module", "pur713-lem-open-pull-levelwise"]
+++
Under the inputs of Lemmas [pur713-lem-open-adjunction-module], [pur713-lem-open-pull-levelwise] and [pur713-lem-monoidal-pullback-module], for an open immersion $j:U\hookrightarrow X$, $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, $K\in D(U_{\Proet},T)$ and $N\in D(X_{\Proet},T)$, define

$$
\sigma_{j,K,N,T}:
\mathrm D(j_{!,T})\bigl(K\otimes^L_{\mathcal R_{U,T}}\mathrm D(j^*_T)N\bigr)
\longrightarrow\mathrm D(j_{!,T})K\otimes^L_{\mathcal R_{X,T}}N
$$

as the adjoint, under Lemma [pur713-lem-open-adjunction-module], of the map $K\otimes^L_{\mathcal R_{U,T}}\mathrm D(j^*_T)N\to\mathrm D(j^*_T)(\mathrm D(j_{!,T})K\otimes^L_{\mathcal R_{X,T}}N)$ obtained by tensoring the unit at $K$ with the identity and then applying the monoidal comparison of Lemma [pur713-lem-monoidal-pullback-module] for $j$, with Lemma [pur713-lem-open-pull-levelwise].
