+++
id = "pur713-def-open-projection"
kind = "definition"
title = "Open-extension projection map, finite coefficients"
order = 1878
tags = ["latex:bpdefinition"]
uses = ["pur713-lem-monoidal-pullback"]
+++
Assume Input “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`). For an open immersion $j:U\hookrightarrow X$, $K\in D(U_{\Proet},\mathcal O_E/\varpi^n)$ and $N\in D(X_{\Proet},\mathcal O_E/\varpi^n)$, define

$$
\sigma_{j,K,N,\mathcal O_E/\varpi^n}:
\mathrm D(j_{!,\mathcal O_E/\varpi^n})
\bigl(K\otimes^L_{\mathcal O_E/\varpi^n}\mathrm D(j^*_{\mathcal O_E/\varpi^n})N\bigr)
\longrightarrow\mathrm D(j_{!,\mathcal O_E/\varpi^n})K\otimes^L_{\mathcal O_E/\varpi^n}N
$$

as the adjoint, under Lemma “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`), of the map $K\otimes^L_{\mathcal O_E/\varpi^n}\mathrm D(j^*_{\mathcal O_E/\varpi^n})N\to\mathrm D(j^*_{\mathcal O_E/\varpi^n})(\mathrm D(j_{!,\mathcal O_E/\varpi^n})K\otimes^L_{\mathcal O_E/\varpi^n}N)$ obtained by tensoring the unit at $K$ with the identity and then applying the monoidal comparison of Lemma [pur713-lem-monoidal-pullback] for $j$, with the identification $\mathrm D(j^*_{\mathcal O_E/\varpi^n})\cong Lj^*_{\mathcal O_E/\varpi^n}$ of Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`).
