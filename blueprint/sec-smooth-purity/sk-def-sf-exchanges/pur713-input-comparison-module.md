+++
id = "pur713-input-comparison-module"
kind = "remark"
title = "Comparison of compactifications, module objects"
order = 1900
tags = ["latex:bpinput"]
uses = ["pur456-lem-adjoint-comparison", "pur713-def-lower-shriek-module", "pur713-def-shriek-projection-module", "pur713-input-comparison"]
+++
For $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, every $f$ as in Input [pur713-input-comparison] and every compactification $d$ of $f$, there is a specified natural isomorphism $\theta_{d,T}:R_{d,T}\xrightarrow{\sim}Rf_{!,T}$ of functors $D(X_{\Proet},T)\to D(Y_{\Proet},T)$, with $R_{d,T}$ and $Rf_{!,T}$ of Definition [pur713-def-lower-shriek-module], such that $\theta_{c_f,T}=1$ and, for all $K\in D(X_{\Proet},T)$ and $L\in D(Y_{\Proet},T)$,
$\theta_{d,T,K\otimes^L_{\mathcal R_{X,T}}Lf^*_TL}\circ\operatorname{PF}_{d,K,L,T}=\operatorname{PF}_{f,K,L,T}\circ(\theta_{d,T,K}\otimes^L_{\mathcal R_{Y,T}}1_L)$,
with the projection transformations of Definition [pur713-def-shriek-projection-module]. Lemma [pur456-lem-adjoint-comparison] uses only the restriction of $\theta_{d,T}$ to $D^b_c(X_{\Proet},T)$. *Status:* not established at any non-finite coefficient stage; the governing reference attaches $Rf_{!,T}$ to the chosen compactification and lists independence of the compactification among its open directions (§12).
