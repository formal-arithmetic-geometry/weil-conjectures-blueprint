+++
id = "pur713-def-module-push"
kind = "definition"
title = "Module-object direct image"
order = 1827
tags = ["latex:bpdefinition"]
uses = ["pur713-def-mapmod", "pur713-def-restriction", "pur713-input-coefficient-structure"]
+++
Assume Input [pur713-input-coefficient-structure], so that $\eta_{f,T}$ is a morphism of ring objects. For $f:X\to Y$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the direct image of module objects is

$$
f_{*,T}:=\operatorname{Res}_{\eta_{f,T}}\circ(f_{*,\mathbf Z})_{\mathcal R_{X,T}}:
\mathsf{Mod}(X_{\Proet},T)\longrightarrow\mathsf{Mod}_{f_{*,\mathbf Z}\mathcal R_{X,T}}(Y_{\Proet})\longrightarrow\mathsf{Mod}(Y_{\Proet},T),
$$

with the transport of Definition [pur713-def-mapmod] and the restriction of scalars of Definition [pur713-def-restriction]. Thus the underlying sheaf of $f_{*,T}M$ is $f_{*,\mathbf Z}M$, and $\mathcal R_{Y,T}$ acts through $\eta_{f,T}$.
