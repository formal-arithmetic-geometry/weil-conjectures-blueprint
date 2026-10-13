+++
id = "pur713-def-module-pull"
kind = "definition"
title = "Module-object inverse image"
order = 1828
tags = ["latex:bpdefinition"]
uses = ["pur713-input-coefficient-open", "pur713-input-coefficient-structure"]
+++
Assume Input [pur713-input-coefficient-structure], so that $\alpha_{f,T}$ is a morphism of ring objects. For $f:X\to Y$ and $T$ as above, the inverse image of module objects is

$$
f^*_T:=\operatorname{Ext}_{\alpha_{f,T}}\circ(f^{-1}_{\mathbf Z})_{\mathcal R_{Y,T}}:
\mathsf{Mod}(Y_{\Proet},T)\longrightarrow\mathsf{Mod}_{f^{-1}_{\mathbf Z}\mathcal R_{Y,T}}(X_{\Proet})\longrightarrow\mathsf{Mod}(X_{\Proet},T),
$$

so that $f^*_TM=\mathcal R_{X,T}\otimes_{f^{-1}_{\mathbf Z}\mathcal R_{Y,T}}f^{-1}_{\mathbf Z}M$ is the ringed-site pullback. The general extension of scalars $\operatorname{Ext}_{\alpha_{f,T}}$ is kept in the definition although $\alpha_{f,T}$ is invertible (Input [pur713-input-coefficient-open]), so that no inverse is chosen.
