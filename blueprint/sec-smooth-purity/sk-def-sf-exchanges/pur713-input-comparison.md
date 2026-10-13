+++
id = "pur713-input-comparison"
kind = "remark"
title = "Comparison of compactifications, finite coefficients"
order = 1898
tags = ["latex:bpinput"]
uses = ["pur713-def-shriek-projection"]
+++
For every separated morphism of finite type $f:X\to Y$ of $k$-schemes of finite type and every compactification $d$ of $f$, there is a specified natural isomorphism

$$
\theta_{d,\mathcal O_E/\varpi^n}:R_d\xrightarrow{\sim}Rf_{!,\mathcal O_E/\varpi^n}
$$

of functors $D(X_{\Proet},\mathcal O_E/\varpi^n)\to D(Y_{\Proet},\mathcal O_E/\varpi^n)$, with $R_d$ of Definition “Compact-support direct image for an auxiliary compactification” (`pur713-def-lower-shriek-auxiliary`) and $Rf_{!,\mathcal O_E/\varpi^n}$ of Definition “Finite-coefficient compact-support direct image” (`pur713-def-lower-shriek`), such that $\theta_{c_f,\mathcal O_E/\varpi^n}=1$ and, for all $K\in D(X_{\Proet},\mathcal O_E/\varpi^n)$ and $L\in D(Y_{\Proet},\mathcal O_E/\varpi^n)$,

$$
\theta_{d,\mathcal O_E/\varpi^n,K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L}\circ\operatorname{PF}_{d,K,L,\mathcal O_E/\varpi^n}
=\operatorname{PF}_{f,K,L,\mathcal O_E/\varpi^n}\circ
(\theta_{d,\mathcal O_E/\varpi^n,K}\otimes^L_{\mathcal O_E/\varpi^n}1_L),
$$

with the projection transformations of Definition [pur713-def-shriek-projection]. *Status:* not established. Lemma “Pro-étale compactification comparison is a natural isomorphism” (`pur456-lem-proet-independent`, see [sk-prop-sf-comp-coherence]) gives such comparisons only on the étale-origin subcategories, and the governing reference attaches $Rf_{!,\mathcal O_E/\varpi^n}$ to the chosen compactification without asserting independence. Wherever this input is used, it is named.
