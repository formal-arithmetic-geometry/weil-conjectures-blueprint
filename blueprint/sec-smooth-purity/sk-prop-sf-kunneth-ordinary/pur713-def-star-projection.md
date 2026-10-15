+++
id = "pur713-def-star-projection"
kind = "definition"
title = "Direct-image projection transformation, finite coefficients"
order = 1980
uses = ["sk-def-sf-exchanges"]
+++
Assume Input “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`). For $f:X\to Y$, $K\in D(X_{\Proet},\mathcal O_E/\varpi^n)$ and $L\in D(Y_{\Proet},\mathcal O_E/\varpi^n)$, define

$$
P_{f,K,L,\mathcal O_E/\varpi^n}:
Rf_{*,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}L
\longrightarrow Rf_{*,\mathcal O_E/\varpi^n}
\bigl(K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L\bigr)
$$

in $D(Y_{\Proet},\mathcal O_E/\varpi^n)$ as the adjoint under Lemma “Finite-coefficient derived inverse-image adjunction” (`pur713-lem-star-adjunction`) of

$$
Lf^*_{\mathcal O_E/\varpi^n}\bigl(Rf_{*,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}L\bigr)
\xrightarrow{\sim}Lf^*_{\mathcal O_E/\varpi^n}Rf_{*,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L
\xrightarrow{\varepsilon_{f,K}\otimes1}K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L,
$$

the first arrow being the comparison of Lemma “Monoidal comparison for finite-coefficient derived inverse image” (`pur713-lem-monoidal-pullback`, in [sk-def-sf-exchanges]). No boundedness assertion on its values is made.
