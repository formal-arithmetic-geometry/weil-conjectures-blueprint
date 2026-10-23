+++
id = "pur7710-def-etale-shriek-exchange"
kind = "definition"
title = "Étale compact-support exchange"
order = 3044
uses = ["pur713-def-base-changed-compactification", "sk-thm-sf-comp-composition"]
+++
Let $f:X\to Y$ be a separated morphism of finite type between $k$-schemes of finite type, $g:Y'\to Y$ a morphism of $k$-schemes of finite type, and write $f':X'=X\times_YY'\to Y'$ and $g':X'\to X$ for the projections. Let $c_f=(j:X\hookrightarrow\overline X,\ p:\overline X\to Y)$ be the chosen compactification of $f$, let $\overline X'=\overline X\times_YY'$ with projections $\overline g:\overline X'\to\overline X$ and $p':\overline X'\to Y'$, and let $c'=(j',p')$ be the base-changed compactification of $f'$ (Definition [pur713-def-base-changed-compactification]). Define the natural transformation

$$
\operatorname{Ex}_{!,\Et,\mathcal O_E/\pi_E^n}:
Lg^*_{\Et,\mathcal O_E/\pi_E^n}Rf_{!,\Et,\mathcal O_E/\pi_E^n}
\longrightarrow I_{c',\mathcal O_E/\pi_E^n}Lg'^*_{\Et,\mathcal O_E/\pi_E^n}
$$

of functors from $D^+(X_{\Et},\mathcal O_E/\pi_E^n)$ to $D^+(Y'_{\Et},\mathcal O_E/\pi_E^n)$ as the composite

$$
\begin{aligned}
Lg^*_{\Et,\mathcal O_E/\pi_E^n}Rp_{*,\Et,\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\Et,\mathcal O_E/\pi_E^n})
&\longrightarrow Rp'_{*,\Et,\mathcal O_E/\pi_E^n}L\overline g^*_{\Et,\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\Et,\mathcal O_E/\pi_E^n})\\
&\xrightarrow{Rp'_{*,\Et,\mathcal O_E/\pi_E^n}(e^{-1}_{j,\overline g})} Rp'_{*,\Et,\mathcal O_E/\pi_E^n}\mathrm D(j'_{!,\Et,\mathcal O_E/\pi_E^n})Lg'^*_{\Et,\mathcal O_E/\pi_E^n}.
\end{aligned}
$$

The first arrow is the adjunction exchange of Lemma “The derived proper-base-change comparison” (`pur456-pbc-derived`, in [sk-thm-sf-comp-composition]) for the Cartesian square of $p$ and $g$, evaluated on $\mathrm D(j_{!,\Et,\mathcal O_E/\pi_E^n})$ of an object of $D^+(X_{\Et},\mathcal O_E/\pi_E^n)$, which lies in $D^+(\overline X_{\Et},\mathcal O_E/\pi_E^n)$ by Lemma “\'{E}tale extension by zero preserves bounded-below objects” (`pur456-pbc-open-plus`, in [sk-thm-sf-comp-composition]). The second arrow applies the direct image to the inverse of the map $e_{j,\overline g}$ of Definition “The étale open-exchange morphism” (`pur7710-def-etale-open-exchange`, in [sk-thm-sf-comp-composition]), which exists by Lemma “Open base change on the étale site” (`pur7710-lem-etale-open-base-change`, in [sk-thm-sf-comp-composition]).
