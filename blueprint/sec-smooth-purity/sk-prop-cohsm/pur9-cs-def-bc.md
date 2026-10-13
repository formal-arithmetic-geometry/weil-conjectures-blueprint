+++
id = "pur9-cs-def-bc"
kind = "definition"
title = "Base-change map for the standing exceptional inverse image"
order = 2343
tags = ["latex:bpdefinition"]
uses = ["pur713-def-base-changed-compactification", "pur713-def-shriek-exchange-chosen", "pur713-input-comparison", "pur713-input-proper-adjoint", "pur7710-input-constructible-sheaves", "pur7710-input-site-exchange", "pur7710-lem-constructible-equivalence", "pur7710-lem-origin-cbc", "pur9-input-ambient-comparison", "pur9-input-preservation"]
+++
Assume Inputs [pur713-input-proper-adjoint], [pur9-input-ambient-comparison], [pur9-input-preservation], “The qcqs direct-image comparison theorem” (`pur7710-input-qcqs-comparison`, see [sk-prop-sf-comp-coherence]), [pur7710-input-site-exchange] and [pur7710-input-constructible-sheaves]. Let $f:X\to Y$ be separated of finite type, $v:Y'\to Y$ a morphism, $X'=X\times_YY'$, $f':X'\to Y'$ and $u:X'\to X$ the projections, and $c'$ the base change of $c_f$ (Definition [pur713-def-base-changed-compactification]). For $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\varpi^n)$ put $M=Rf^!_{\mathcal O_E/\varpi^n}K$; then $M\in D^b_c(X_{\Proet},\mathcal O_E/\varpi^n)\subseteq\mathscr E^+(X_{\Proet},\mathcal O_E/\varpi^n)$ by Input [pur9-input-preservation] and Lemma [pur7710-lem-constructible-equivalence], so the exchange $\operatorname{Ex}^\circ_{!,\square,\mathcal O_E/\varpi^n,M}$ of Definition [pur713-def-shriek-exchange-chosen] is invertible by Lemma [pur7710-lem-origin-cbc]. Define

$$
b_{v,K}:Lu^*_{\mathcal O_E/\varpi^n}Rf^!_{\mathcal O_E/\varpi^n}K\longrightarrow Rf'^!_{\mathcal O_E/\varpi^n}Lv^*_{\mathcal O_E/\varpi^n}K
$$

in $D(X'_{\Proet},\mathcal O_E/\varpi^n)$ as the morphism corresponding under the standing adjunction for $f'$ to

$$
Rf'_{!,\mathcal O_E/\varpi^n}Lu^*_{\mathcal O_E/\varpi^n}M\xrightarrow{(\operatorname{Ex}^\circ_{!,\square,\mathcal O_E/\varpi^n,M})^{-1}}Lv^*_{\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}M\xrightarrow{Lv^*_{\mathcal O_E/\varpi^n}\varepsilon_{f,K}}Lv^*_{\mathcal O_E/\varpi^n}K,
$$

with $\operatorname{Ex}^\circ$ formed with $\theta_{c'}$ of Input [pur713-input-comparison] and $\varepsilon_f$ the counit of the standing adjunction for $f$.
