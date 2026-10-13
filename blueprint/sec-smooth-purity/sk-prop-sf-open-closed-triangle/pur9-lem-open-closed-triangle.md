+++
id = "pur9-lem-open-closed-triangle"
kind = "lemma"
title = "The open–closed triangle"
order = 2177
tags = ["latex:bplemma"]
uses = ["pur9-input-closed-immersion", "pur9-input-open-closed"]
+++
Assume Inputs [pur9-input-closed-immersion] and [pur9-input-open-closed]. For every $M\in D(X_{\Proet},\mathcal O_E/\varpi^n)$ there is a distinguished triangle

$$
\mathrm D(j_{!,\mathcal O_E/\varpi^n})\mathrm D(j^*_{\mathcal O_E/\varpi^n})M\xrightarrow{\ \varepsilon^j_M\ }M\xrightarrow{\ \eta^i_M\ }Ri_{*,\mathcal O_E/\varpi^n}Li^*_{\mathcal O_E/\varpi^n}M\xrightarrow{\ \delta_M\ }\mathrm D(j_{!,\mathcal O_E/\varpi^n})\mathrm D(j^*_{\mathcal O_E/\varpi^n})M[1],
$$

where $\varepsilon^j$ is the counit of Lemma “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`), $\eta^i$ the unit of Lemma “Finite-coefficient derived inverse-image adjunction” (`pur713-lem-star-adjunction`) for $i$, and $\delta$ is a natural transformation; the triangle is natural in $M$.
