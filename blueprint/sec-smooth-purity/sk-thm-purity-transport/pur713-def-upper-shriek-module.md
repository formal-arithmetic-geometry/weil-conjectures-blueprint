+++
id = "pur713-def-upper-shriek-module"
kind = "definition"
title = "Module-object exceptional inverse image"
order = 2352
uses = ["sk-def-sf-operations"]
+++
For $f:X\to Y$, separated of finite type between separated $k$-schemes of finite type, with chosen compactification $c_f=(j_f,p_f)$, and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, under Inputs “Coefficient maps are ring-object morphisms” (`pur713-input-coefficient-structure`, in [sk-def-sf-operations]), “Constructibility preservation at non-finite coefficients” (`pur713-input-cons-preservation-module`, in [sk-def-sf-operations]) and “Module-object proper-adjoint input” (`pur713-input-proper-adjoint-module`, in [sk-def-sf-operations]), define

$$
Rf^!_T:=\mathrm D(j^*_{f,T})\circ Rp^!_{f,T}:
D^b_c(Y_{\Proet},T)\longrightarrow D^b_c(X_{\Proet},T),
$$

where $\mathrm D(j^*_{f,T})$ is the restriction to bounded constructible objects of the levelwise functor of Lemma “Exactness of module-object restriction to an open” (`pur713-lem-open-pull-exact-module`, in [sk-def-sf-operations]). It is a composite of two specified functors on the bounded constructible categories, as in the governing reference, §9; it is not defined on $D(Y_{\Proet},T)$, and there is no underived module-object exceptional inverse image. For an arbitrary compactification $d=(j,p)$, write $R^!_{d,T}:=\mathrm D(j^*_T)\circ Rp^!_T$ on $D^b_c(Y_{\Proet},T)$.
