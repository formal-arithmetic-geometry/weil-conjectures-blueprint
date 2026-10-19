+++
id = "pur713-def-open-exchange"
kind = "definition"
title = "Open-extension base-change map, finite coefficients"
order = 2356
uses = ["pur713-def-base-changed-compactification"]
+++
In Definition [pur713-def-base-changed-compactification], for $K\in D(X_{\Proet},\mathcal O_E/\pi_E^n)$, define

$$
b'_{j,\bar g,\mathcal O_E/\pi_E^n,K}:\mathrm D(j'_{!,\mathcal O_E/\pi_E^n})Lg'^*_{\mathcal O_E/\pi_E^n}K\longrightarrow L\bar g^*_{\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K
$$

as the adjoint, under Lemma “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`) for $j'$, of the composite

$$
\begin{aligned}
Lg'^*_{\mathcal O_E/\pi_E^n}K&\xrightarrow{Lg'^*_{\mathcal O_E/\pi_E^n}(\mathrm{unit})}Lg'^*_{\mathcal O_E/\pi_E^n}\mathrm D(j^*_{\mathcal O_E/\pi_E^n})\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K
\cong Lg'^*_{\mathcal O_E/\pi_E^n}Lj^*_{\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K\\
&\xrightarrow{\mu_{j,g'}}L(jg')^*_{\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K
\xrightarrow{\mu^{-1}_{\bar g,j'}}Lj'^*_{\mathcal O_E/\pi_E^n}L\bar g^*_{\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K
\cong\mathrm D(j'^*_{\mathcal O_E/\pi_E^n})L\bar g^*_{\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K,
\end{aligned}
$$

where the unnamed isomorphisms are those of Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`), $\mu$ is Definition “Composition comparison for finite-coefficient derived inverse image” (`pur713-def-pull-composition`) at the coefficient $\mathcal O_E/\pi_E^n$, and $L(jg')^*_{\mathcal O_E/\pi_E^n}=L(\bar gj')^*_{\mathcal O_E/\pi_E^n}$. It is a natural transformation of functors $D(X_{\Proet},\mathcal O_E/\pi_E^n)\to D(\overline X'_{\Proet},\mathcal O_E/\pi_E^n)$.
