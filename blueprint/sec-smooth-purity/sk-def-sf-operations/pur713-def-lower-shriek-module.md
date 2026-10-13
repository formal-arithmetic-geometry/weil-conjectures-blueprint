+++
id = "pur713-def-lower-shriek-module"
kind = "definition"
title = "Module-object compact-support direct image"
order = 1845
tags = ["latex:bpdefinition"]
uses = ["pur713-def-derived-push-module", "pur713-def-open-shriek-module", "pur713-input-coefficient-structure", "pur713-input-open-projection", "pur713-lem-open-exact-module"]
+++
Let $f:X\to Y$ be a separated morphism of finite type with chosen compactification $c_f=(j_f,p_f)$ (Definition “Chosen compactifications” (`pur456-pbc-chosen-compactification`, see [sk-thm-sf-comp-composition])). Under Inputs [pur713-input-coefficient-structure] and [pur713-input-open-projection], for $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, define

$$
Rf_{!,T}:=Rp_{f,*,T}\circ\mathrm D(j_{f,!,T}):
D(X_{\Proet},T)\longrightarrow D(Y_{\Proet},T),
$$

with Definitions [pur713-def-derived-push-module] and [pur713-def-open-shriek-module]; $\mathrm D(j_{f,!,T})$ is defined by Lemma [pur713-lem-open-exact-module]. It is the composite of derived functors chosen in the governing reference, §8.2, not the total right derived functor of the underived composite. For an arbitrary compactification $d=(j,p)$ of $f$, write $R_{d,T}:=Rp_{*,T}\circ\mathrm D(j_{!,T})$; this is used only in comparison statements.
