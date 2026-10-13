+++
id = "pur7710-input-site-exchange"
kind = "remark"
title = "Compatibility of site comparison with the specified exchange"
order = 1875
tags = ["latex:bpinput"]
uses = ["pur713-def-shriek-exchange", "pur7710-def-etale-shriek-exchange"]
+++
For the Cartesian square and the compactifications in Definition [pur7710-def-etale-shriek-exchange], the following equality of natural transformations holds, with $\beta$ of Definition “Inverse image across the two sites” (`pur7710-def-site-pullback-comparison`, see [sk-prop-sf-comp-coherence]), $\kappa$ of Definition “Comparison of compactification candidates across sites” (`pur456-def-candidate-site-comparison`, see [sk-prop-sf-comp-coherence]) and the pro-étale exchange $\operatorname{Ex}_{!,\square,\mathcal O_E/\varpi^n}$ of Definition [pur713-def-shriek-exchange]:

$$
\begin{aligned}
&(R_{c'}\beta_{g'})
\circ(\operatorname{Ex}_{!,\square,\mathcal O_E/\varpi^n}L\nu^*_{X,\mathcal O_E/\varpi^n})
\circ(Lg^*_{\mathcal O_E/\varpi^n}\kappa_{f,\mathcal O_E/\varpi^n})\\
&\quad=(\kappa_{c',\mathcal O_E/\varpi^n}Lg'^*_{\Et,\mathcal O_E/\varpi^n})
\circ(L\nu^*_{Y',\mathcal O_E/\varpi^n}\operatorname{Ex}_{!,\Et,\mathcal O_E/\varpi^n})
\circ(\beta_g Rf_{!,\Et,\mathcal O_E/\varpi^n}).
\end{aligned}
$$

Both sides run from $Lg^*_{\mathcal O_E/\varpi^n}L\nu^*_{Y,\mathcal O_E/\varpi^n}Rf_{!,\Et,\mathcal O_E/\varpi^n}$ to $R_{c'}L\nu^*_{X',\mathcal O_E/\varpi^n}Lg'^*_{\Et,\mathcal O_E/\varpi^n}$, as functors on $D^+(X_{\Et},\mathcal O_E/\varpi^n)$. *Status:* every map in the equality is built from units, counits, the comparisons $\beta$ and $\omega$, and their mates, so the equality is expected to follow from Lemmas “Composition law for the inverse-image site comparison” (`pur7710-lem-site-pullback-coherence`, see [sk-prop-sf-comp-coherence]) and “Composition law for the open-extension site comparison” (`pur456-lem-open-site-comparison`, see [sk-prop-sf-comp-coherence]) by a mate computation; that computation has not been carried out here, so the equality is recorded as an input. An unspecified isomorphism between these functors does not establish it, and it has not been checked against formalization declarations.
