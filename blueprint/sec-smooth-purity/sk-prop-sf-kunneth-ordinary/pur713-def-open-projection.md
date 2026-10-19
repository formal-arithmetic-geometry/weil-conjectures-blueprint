+++
id = "pur713-def-open-projection"
kind = "definition"
title = "Open-extension projection map, finite coefficients"
order = 1981
uses = ["sk-def-sf-exchanges"]
+++
Assume Input “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`). For an open immersion $j:U\hookrightarrow X$, $K\in D(U_{\Proet},\mathcal O_E/\pi_E^n)$ and $N\in D(X_{\Proet},\mathcal O_E/\pi_E^n)$, define

$$
\sigma_{j,K,N,\mathcal O_E/\pi_E^n}:
\mathrm D(j_{!,\mathcal O_E/\pi_E^n})
\bigl(K\otimes^L_{\mathcal O_E/\pi_E^n}\mathrm D(j^*_{\mathcal O_E/\pi_E^n})N\bigr)
\longrightarrow\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K\otimes^L_{\mathcal O_E/\pi_E^n}N
$$

as the adjoint, under Lemma “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`), of the map $K\otimes^L_{\mathcal O_E/\pi_E^n}\mathrm D(j^*_{\mathcal O_E/\pi_E^n})N\to\mathrm D(j^*_{\mathcal O_E/\pi_E^n})(\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K\otimes^L_{\mathcal O_E/\pi_E^n}N)$ obtained by tensoring the unit at $K$ with the identity and then applying the monoidal comparison of Lemma “Monoidal comparison for finite-coefficient derived inverse image” (`pur713-lem-monoidal-pullback`, in [sk-def-sf-exchanges]) for $j$, with the identification $\mathrm D(j^*_{\mathcal O_E/\pi_E^n})\cong Lj^*_{\mathcal O_E/\pi_E^n}$ of Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`).
