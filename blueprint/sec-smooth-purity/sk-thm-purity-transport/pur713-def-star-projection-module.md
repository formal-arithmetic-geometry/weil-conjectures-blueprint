+++
id = "pur713-def-star-projection-module"
kind = "definition"
title = "Direct-image projection transformation, module objects"
order = 2358
uses = ["sk-def-sf-exchanges", "sk-def-sf-operations"]
+++
Under the inputs of Lemmas “Module-object derived inverse-image adjunction” (`pur713-lem-star-adjunction-module`, in [sk-def-sf-operations]) and “Monoidal comparison for module-object derived inverse image” (`pur713-lem-monoidal-pullback-module`, in [sk-def-sf-exchanges]), for $f:X\to Y$, $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, $K\in D(X_{\Proet},T)$ and $L\in D(Y_{\Proet},T)$, define

$$
P_{f,K,L,T}:Rf_{*,T}K\otimes^L_{\mathcal R_{Y,T}}L
\longrightarrow Rf_{*,T}\bigl(K\otimes^L_{\mathcal R_{X,T}}Lf^*_TL\bigr)
$$

in $D(Y_{\Proet},T)$ as the adjoint under Lemma “Module-object derived inverse-image adjunction” (`pur713-lem-star-adjunction-module`, in [sk-def-sf-operations]) of

$$
Lf^*_T\bigl(Rf_{*,T}K\otimes^L_{\mathcal R_{Y,T}}L\bigr)
\xrightarrow{\sim}Lf^*_TRf_{*,T}K\otimes^L_{\mathcal R_{X,T}}Lf^*_TL
\xrightarrow{\varepsilon_{f,T,K}\otimes 1}
K\otimes^L_{\mathcal R_{X,T}}Lf^*_TL,
$$

the first arrow being the comparison of Lemma “Monoidal comparison for module-object derived inverse image” (`pur713-lem-monoidal-pullback-module`, in [sk-def-sf-exchanges]).
