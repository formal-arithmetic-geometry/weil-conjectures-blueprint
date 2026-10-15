+++
id = "pur713-def-derived-push-module"
kind = "definition"
title = "Module-object derived direct image"
order = 2349
uses = ["pur713-def-module-push", "sk-def-sf-operations", "sk-def-sf-setting"]
+++
For $f:X\to Y$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, under Input “Coefficient maps are ring-object morphisms” (`pur713-input-coefficient-structure`, in [sk-def-sf-operations]), the derived direct image

$$
Rf_{*,T}:=R(f_{*,T}):D(X_{\Proet},T)\longrightarrow D(Y_{\Proet},T)
$$

is the total right derived functor of the entire module-object direct image of Definition [pur713-def-module-push], computed on K-injective resolutions in the Grothendieck abelian category $\mathsf{Mod}(X_{\Proet},T)$ (Input “Abelian structure of module objects” (`pur713-input-module-abelian`, in [sk-def-sf-setting])). Its identification with $\mathrm D(\operatorname{Res}_{\eta_{f,T}})\circ R((f_{*,\mathbf Z})_{\mathcal R_{X,T}})$ is a comparison theorem of the governing reference, §8.2, using Lemma “Exactness of restriction of scalars” (`pur713-lem-restriction-exact`, in [sk-def-sf-operations]); it is not the definition.
