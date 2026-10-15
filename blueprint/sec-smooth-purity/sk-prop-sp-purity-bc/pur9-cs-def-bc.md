+++
id = "pur9-cs-def-bc"
kind = "definition"
title = "Base-change map for the standing exceptional inverse image"
order = 2360
uses = ["pur713-def-base-changed-compactification", "pur713-def-shriek-exchange-chosen", "sk-def-sf-exchanges", "sk-def-sf-operations", "sk-prop-sf-cbc", "sk-prop-sf-comp-coherence", "sk-prop-sf-comparison"]
+++
Assume Inputs “Finite-coefficient proper-adjoint input” (`pur713-input-proper-adjoint`, in [sk-def-sf-operations]), “Compactification comparisons on the ambient categories” (`pur9-input-ambient-comparison`), “Preservation of finite-Tor constructible objects” (`pur9-input-preservation`), “The qcqs direct-image comparison theorem” (`pur7710-input-qcqs-comparison`, in [sk-prop-sf-comp-coherence]), “Compatibility of site comparison with the specified exchange” (`pur7710-input-site-exchange`, in [sk-prop-sf-cbc]) and “Constructible sheaves across the two sites” (`pur7710-input-constructible-sheaves`, in [sk-prop-sf-comparison]). Let $f:X\to Y$ be separated of finite type, $v:Y'\to Y$ a morphism, $X'=X\times_YY'$, $f':X'\to Y'$ and $u:X'\to X$ the projections, and $c'$ the base change of $c_f$ (Definition [pur713-def-base-changed-compactification]). For $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\varpi^n)$ put $M=Rf^!_{\mathcal O_E/\varpi^n}K$; then $M\in D^b_c(X_{\Proet},\mathcal O_E/\varpi^n)\subseteq\mathscr E^+(X_{\Proet},\mathcal O_E/\varpi^n)$ by Input “Preservation of finite-Tor constructible objects” (`pur9-input-preservation`) and Lemma “Equivalence on bounded constructible complexes” (`pur7710-lem-constructible-equivalence`, in [sk-prop-sf-comparison]), so the exchange $\operatorname{Ex}^\circ_{!,\square,\mathcal O_E/\varpi^n,M}$ of Definition [pur713-def-shriek-exchange-chosen] is invertible by Lemma “Compact-support base change on the étale-origin class” (`pur7710-lem-origin-cbc`, in [sk-prop-sf-cbc]). Define

$$
b_{v,K}:Lu^*_{\mathcal O_E/\varpi^n}Rf^!_{\mathcal O_E/\varpi^n}K\longrightarrow Rf'^!_{\mathcal O_E/\varpi^n}Lv^*_{\mathcal O_E/\varpi^n}K
$$

in $D(X'_{\Proet},\mathcal O_E/\varpi^n)$ as the morphism corresponding under the standing adjunction for $f'$ to

$$
Rf'_{!,\mathcal O_E/\varpi^n}Lu^*_{\mathcal O_E/\varpi^n}M\xrightarrow{(\operatorname{Ex}^\circ_{!,\square,\mathcal O_E/\varpi^n,M})^{-1}}Lv^*_{\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}M\xrightarrow{Lv^*_{\mathcal O_E/\varpi^n}\varepsilon_{f,K}}Lv^*_{\mathcal O_E/\varpi^n}K,
$$

with $\operatorname{Ex}^\circ$ formed with $\theta_{c'}$ of Input “Comparison of compactifications, finite coefficients” (`pur713-input-comparison`, in [sk-def-sf-exchanges]) and $\varepsilon_f$ the counit of the standing adjunction for $f$.
