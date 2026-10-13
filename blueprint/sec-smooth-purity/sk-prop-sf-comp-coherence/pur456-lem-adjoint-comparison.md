+++
id = "pur456-lem-adjoint-comparison"
kind = "lemma"
title = "The comparison of specified module-object right adjoints"
order = 1869
tags = ["latex:bplemma"]
uses = ["pur713-def-upper-shriek-module", "pur713-input-proper-adjoint-module", "pur713-lem-shriek-adjunction-module"]
+++
Let $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, let $d$ be a compactification of $f:X\to Y$, and assume Input [pur713-input-proper-adjoint-module], so that $R^!_{d,T}$, $Rf^!_T$ of Definition [pur713-def-upper-shriek-module] and the adjunctions $R_{d,T}\dashv R^!_{d,T}$, $Rf_{!,T}\dashv Rf^!_T$ of Lemma [pur713-lem-shriek-adjunction-module] are given, with units $\eta_d,\eta_f$ and counits $\varepsilon_d,\varepsilon_f$. Suppose given a natural isomorphism $\theta_{d,T}:R_{d,T}\to Rf_{!,T}$ of functors on $D^b_c(X_{\Proet},T)$. Then there is a unique natural transformation $\theta^!_{d,T}:Rf^!_T\to R^!_{d,T}$ of functors on $D^b_c(Y_{\Proet},T)$ such that, for all $K\in D^b_c(X_{\Proet},T)$, $L\in D^b_c(Y_{\Proet},T)$ and $v:K\to Rf^!_TL$,

$$
\varepsilon_{d,L}\circ R_{d,T}\bigl(\theta^!_{d,T,L}\circ v\bigr)
=\varepsilon_{f,L}\circ Rf_{!,T}(v)\circ\theta_{d,T,K};
$$

it is an isomorphism, and its component at $L$ is

$$
Rf^!_TL\xrightarrow{\eta_{d,Rf^!_TL}}R^!_{d,T}R_{d,T}Rf^!_TL
\xrightarrow{R^!_{d,T}(\theta_{d,T,Rf^!_TL})}R^!_{d,T}Rf_{!,T}Rf^!_TL
\xrightarrow{R^!_{d,T}(\varepsilon_{f,L})}R^!_{d,T}L.
$$
