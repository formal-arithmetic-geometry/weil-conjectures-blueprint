+++
id = "pur9-input-ambient-comparison"
kind = "remark"
title = "Compactification comparisons on the ambient categories"
order = 2038
tags = ["latex:bpinput"]
uses = ["pur713-def-shriek-exchange", "pur713-def-shriek-exchange-chosen", "pur713-input-comparison"]
+++
Input [pur713-input-comparison] holds, and its comparisons are compatible with the exchange maps: for every Cartesian square $\square$ as in -def-sf-exchangesZZ, every compactification $d$ of $f$ with base change $d'$, and $\operatorname{Ex}_{!,\square,d}$ the exchange of Definition [pur713-def-shriek-exchange] formed with $d$ in place of $c_f$,

$$
(\theta_{d'}Lg'^*_{\mathcal O_E/\varpi^n})\circ\operatorname{Ex}_{!,\square,d}=\operatorname{Ex}^\circ_{!,\square,\mathcal O_E/\varpi^n}\circ(Lg^*_{\mathcal O_E/\varpi^n}\theta_d),
$$

with $\operatorname{Ex}^\circ$ of Definition [pur713-def-shriek-exchange-chosen]. On the étale-origin subcategory $\mathscr E^+(X_{\Proet},\mathcal O_E/\varpi^n)$ of Definition “The bounded-below étale-origin subcategory” (`pur456-def-etale-origin`, see [sk-prop-sf-comp-coherence]), $\theta_d$ agrees with $\theta^{\Proet}_{d,c_f}$ of Definition “Pro-étale compactification comparison” (`pur456-def-proet-independent`, see [sk-prop-sf-comp-coherence]). *Status:* Lemma “Pro-étale compactification comparison is a natural isomorphism” (`pur456-lem-proet-independent`, see [sk-prop-sf-comp-coherence]) constructs such maps only on $\mathscr E^+(X_{\Proet},\mathcal O_E/\varpi^n)$, under Inputs “The bounded-below site-comparison theorem” (`pur7710-input-site-unit`, see [sk-prop-sf-comp-coherence]) and “The qcqs direct-image comparison theorem” (`pur7710-input-qcqs-comparison`, see [sk-prop-sf-comp-coherence]); the extension to the whole ambient category and the exchange and projection equations are not established here.
