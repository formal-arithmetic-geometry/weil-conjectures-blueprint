+++
id = "pur713-def-derived-push-module"
kind = "definition"
title = "Module-object derived direct image"
order = 1835
tags = ["latex:bpdefinition"]
uses = ["pur713-def-module-push", "pur713-input-coefficient-structure", "pur713-input-module-abelian", "pur713-lem-restriction-exact"]
+++
For $f:X\to Y$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, under Input [pur713-input-coefficient-structure], the derived direct image

$$
Rf_{*,T}:=R(f_{*,T}):D(X_{\Proet},T)\longrightarrow D(Y_{\Proet},T)
$$

is the total right derived functor of the entire module-object direct image of Definition [pur713-def-module-push], computed on K-injective resolutions in the Grothendieck abelian category $\mathsf{Mod}(X_{\Proet},T)$ (Input [pur713-input-module-abelian]). Its identification with $\mathrm D(\operatorname{Res}_{\eta_{f,T}})\circ R((f_{*,\mathbf Z})_{\mathcal R_{X,T}})$ is a comparison theorem of the governing reference, §8.2, using Lemma [pur713-lem-restriction-exact]; it is not the definition.
