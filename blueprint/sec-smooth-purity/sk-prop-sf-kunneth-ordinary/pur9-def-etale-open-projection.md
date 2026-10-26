+++
id = "pur9-def-etale-open-projection"
kind = "definition"
title = "Étale open-extension projection map"
order = 3076
uses = ["sk-thm-sf-comp-composition"]
+++
For an open immersion $j:U\hookrightarrow X$, $K\in D(U_{\Et},\mathcal O_E/\pi_E^n)$ and $N\in D(X_{\Et},\mathcal O_E/\pi_E^n)$, let

$$
\sigma^{\Et}_{j,K,N}:\mathrm D(j_{!,\Et,\mathcal O_E/\pi_E^n})\bigl(K\otimes^L_{\mathcal O_E/\pi_E^n}Lj^*_{\Et,\mathcal O_E/\pi_E^n}N\bigr)\longrightarrow\mathrm D(j_{!,\Et,\mathcal O_E/\pi_E^n})K\otimes^L_{\mathcal O_E/\pi_E^n}N
$$

be the adjoint, under Lemma “The étale open-extension adjunction” (`pur456-pbc-open-adjunction`, in [sk-thm-sf-comp-composition]), of the unit at $K$ tensored with the identity, followed by the derived monoidal comparison of $Lj^*_{\Et,\mathcal O_E/\pi_E^n}$ supplied by Input “Unbounded étale derived inverse-image adjunction” (`pur713-input-etale-unbounded-adjunction`).
