+++
id = "pur713-def-coefficient-map"
kind = "definition"
title = "Coefficient morphisms along a scheme morphism"
order = 1823
tags = ["latex:bpdefinition"]
uses = ["pur713-input-point-pullback"]
+++
Let $f:X\to Y$ be a morphism of schemes and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$. The equality $\pi_Y\circ f=\pi_X$ of structure morphisms to $\operatorname{Spec}\mathbf Z$ and the composition isomorphism $f^{-1}_{\mathbf Z}\pi^{-1}_{Y,\mathbf Z}\cong(\pi_Yf)^{-1}_{\mathbf Z}=\pi^{-1}_{X,\mathbf Z}$ of Input “Composition of fixed-coefficient images” (`pur713-input-fixed-composition`) give a natural isomorphism $f^{-1}_{\mathbf Z}\circ p_Y^*\cong p_X^*$ of functors $\mathsf{Sh}(*_{\Proet},\mathsf{Ab})\to\mathsf{Sh}(X_{\Proet},\mathsf{Ab})$ (Input [pur713-input-point-pullback]). Define

$$
\alpha_{f,T}:f^{-1}_{\mathbf Z}\mathcal R_{Y,T}=f^{-1}_{\mathbf Z}p_Y^*\underline T\longrightarrow p_X^*\underline T=\mathcal R_{X,T}
$$

as its component at $\underline T$, and

$$
\eta_{f,T}:\mathcal R_{Y,T}\longrightarrow f_{*,\mathbf Z}\mathcal R_{X,T}
$$

as its mate under $f^{-1}_{\mathbf Z}\dashv f_{*,\mathbf Z}$ (Input “Adjunction and exactness of fixed-coefficient images” (`pur713-input-fixed-adjunction`)): the unit $\mathcal R_{Y,T}\to f_{*,\mathbf Z}f^{-1}_{\mathbf Z}\mathcal R_{Y,T}$ followed by $f_{*,\mathbf Z}(\alpha_{f,T})$. Source: governing reference, §3.3.
