+++
id = "pur713-def-star-exchange"
kind = "definition"
title = "Direct-image exchange, finite coefficients"
order = 3039
uses = ["pur713-def-pullback-comparison"]
+++
The finite-coefficient direct-image exchange for $\square$ is the natural transformation

$$
\operatorname{Ex}_{*,\square,\mathcal O_E/\pi_E^n}:
Lg^*_{\mathcal O_E/\pi_E^n}Rf_{*,\mathcal O_E/\pi_E^n}
\longrightarrow Rf'_{*,\mathcal O_E/\pi_E^n}Lg'^*_{\mathcal O_E/\pi_E^n}
$$

of functors $D(X_{\Proet},\mathcal O_E/\pi_E^n)\to D(Y'_{\Proet},\mathcal O_E/\pi_E^n)$ whose component at $K$ is the adjoint, under Lemma “Finite-coefficient derived inverse-image adjunction” (`pur713-lem-star-adjunction`) for $f'$, of

$$
Lf'^*_{\mathcal O_E/\pi_E^n}Lg^*_{\mathcal O_E/\pi_E^n}Rf_{*,\mathcal O_E/\pi_E^n}K
\xrightarrow{c_{\square,\mathcal O_E/\pi_E^n}}
Lg'^*_{\mathcal O_E/\pi_E^n}Lf^*_{\mathcal O_E/\pi_E^n}Rf_{*,\mathcal O_E/\pi_E^n}K
\xrightarrow{Lg'^*_{\mathcal O_E/\pi_E^n}\varepsilon_{f,K}}Lg'^*_{\mathcal O_E/\pi_E^n}K,
$$

where $\varepsilon_f$ is the counit of Lemma “Finite-coefficient derived inverse-image adjunction” (`pur713-lem-star-adjunction`) for $f$ and $c_{\square,\mathcal O_E/\pi_E^n}$ is Definition [pur713-def-pullback-comparison]. No invertibility is asserted.
