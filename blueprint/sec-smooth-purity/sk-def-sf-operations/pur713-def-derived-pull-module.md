+++
id = "pur713-def-derived-pull-module"
kind = "definition"
title = "Module-object derived inverse image"
order = 1832
tags = ["latex:bpdefinition"]
uses = ["pur713-def-module-pull", "pur713-input-coefficient-structure", "pur713-input-kflat-transport"]
+++
Assume Inputs [pur713-input-coefficient-structure] and [pur713-input-kflat-transport]. For $f:X\to Y$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the derived inverse image

$$
Lf^*_T:=L(f^*_T):D(Y_{\Proet},T)\longrightarrow D(X_{\Proet},T)
$$

is the total left derived functor of the entire module-object inverse image $f^*_T$ of Definition [pur713-def-module-pull], computed on K-flat resolutions in $\mathsf{Mod}(Y_{\Proet},T)$. It is not defined by separately deriving the two factors of $f^*_T$, and it is not defined from the derived inverse image of abelian sheaves. That $f^*_T$ sends quasi-isomorphisms between K-flat complexes to quasi-isomorphisms uses Input [pur713-input-kflat-transport] and the corresponding property of extension of scalars (governing reference, §8.2).
