+++
id = "pur9-input-site-projection"
kind = "remark"
title = "Compatibility of site comparison with the projection maps"
order = 2223
tags = ["latex:bpinput"]
uses = ["pur713-def-shriek-projection", "pur7710-input-site-exchange", "pur9-def-etale-unbounded-candidate", "pur9-input-site-monoidal"]
+++
For $f,c$ as above, $G\in D^+(X_{\Et},\mathcal O_E/\varpi^n)$ and $H\in D(Y_{\Et},\mathcal O_E/\varpi^n)$ with $G\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\Et,\mathcal O_E/\varpi^n}H\in D^+(X_{\Et},\mathcal O_E/\varpi^n)$ and $Rf_{!,\Et,\mathcal O_E/\varpi^n}G\otimes^L_{\mathcal O_E/\varpi^n}H\in D^+(Y_{\Et},\mathcal O_E/\varpi^n)$, the two composites

$$
\begin{aligned}
&\kappa_{f,G\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\Et,\mathcal O_E/\varpi^n}H}\circ L\nu^*_{Y,\mathcal O_E/\varpi^n}(\operatorname{PF}^{\Et}_{f,G,H}),\\
&Rf_{!,\mathcal O_E/\varpi^n}(m_X^{-1})\circ Rf_{!,\mathcal O_E/\varpi^n}(1\otimes\beta_{f,H})\circ\operatorname{PF}_{f,L\nu^*_{X,\mathcal O_E/\varpi^n}G,L\nu^*_{Y,\mathcal O_E/\varpi^n}H,\mathcal O_E/\varpi^n}\circ(\kappa_{f,G}\otimes1)\circ m_Y
\end{aligned}
$$

from $L\nu^*_{Y,\mathcal O_E/\varpi^n}(Rf_{!,\Et,\mathcal O_E/\varpi^n}G\otimes^L_{\mathcal O_E/\varpi^n}H)$ to $Rf_{!,\mathcal O_E/\varpi^n}L\nu^*_{X,\mathcal O_E/\varpi^n}(G\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\Et,\mathcal O_E/\varpi^n}H)$ are equal; all functors are at the coefficient $\mathcal O_E/\varpi^n$, $\kappa$ is Definition “Comparison of compactification candidates across sites” (`pur456-def-candidate-site-comparison`, see [sk-prop-sf-comp-coherence]), $\beta$ Definition “Inverse image across the two sites” (`pur7710-def-site-pullback-comparison`, see [sk-prop-sf-comp-coherence]), $m$ Input [pur9-input-site-monoidal], $\operatorname{PF}$ the finite-coefficient map of Definition [pur713-def-shriek-projection], and $Rf_{!,\Et,\mathcal O_E/\varpi^n}=Rf^{\mathrm{un}}_{!,\Et,\mathcal O_E/\varpi^n}$ on $D^+$ by Definition [pur9-def-etale-unbounded-candidate]. *Status:* both composites are built from units, counits, $\beta$, $\omega$, $\lambda$ and monoidal comparisons, so the equality is expected from mate calculus, as for Input [pur7710-input-site-exchange]; that derivation is not carried out here, and the equality is recorded as an input.
