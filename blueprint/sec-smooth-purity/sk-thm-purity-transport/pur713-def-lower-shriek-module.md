+++
id = "pur713-def-lower-shriek-module"
kind = "definition"
title = "Module-object compact-support direct image"
order = 2351
uses = ["pur713-def-derived-push-module", "pur713-def-open-shriek-module", "sk-def-sf-operations", "sk-thm-sf-comp-composition"]
+++
Let $f:X\to Y$ be a separated morphism of finite type with chosen compactification $c_f=(j_f,p_f)$ (Definition “Chosen compactifications” (`pur456-pbc-chosen-compactification`, in [sk-thm-sf-comp-composition])). Under Inputs “Coefficient maps are ring-object morphisms” (`pur713-input-coefficient-structure`, in [sk-def-sf-operations]) and “Open-extension projection formula for abelian sheaves” (`pur713-input-open-projection`, in [sk-def-sf-operations]), for $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, define

$$
Rf_{!,T}:=Rp_{f,*,T}\circ\mathrm D(j_{f,!,T}):
D(X_{\Proet},T)\longrightarrow D(Y_{\Proet},T),
$$

with Definitions [pur713-def-derived-push-module] and [pur713-def-open-shriek-module]; $\mathrm D(j_{f,!,T})$ is defined by Lemma “Exactness of module-object extension by zero” (`pur713-lem-open-exact-module`, in [sk-def-sf-operations]). It is the composite of derived functors chosen in the governing reference, §8.2, not the total right derived functor of the underived composite. For an arbitrary compactification $d=(j,p)$ of $f$, write $R_{d,T}:=Rp_{*,T}\circ\mathrm D(j_{!,T})$; this is used only in comparison statements.
