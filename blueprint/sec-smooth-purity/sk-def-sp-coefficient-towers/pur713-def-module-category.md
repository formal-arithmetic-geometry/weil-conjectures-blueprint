+++
id = "pur713-def-module-category"
kind = "definition"
title = "Non-finite-coefficient derived category"
order = 2479
uses = ["pur713-def-coefficient-rings", "sk-def-sf-setting", "sk-thm-sf-comp-composition"]
+++
For $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the ambient category is the ordinary derived category of the abelian category of module objects (Input “Abelian structure of module objects” (`pur713-input-module-abelian`, in [sk-def-sf-setting])) over the coefficient ring $\mathcal R_{X,T}$ of Definition [pur713-def-coefficient-rings]:

$$
D(X_{\Proet},T)
:=D\bigl(\mathsf{Mod}(X_{\Proet},T)\bigr),
$$

with $D(-)$ as in Definition “Finite-coefficient étale derived categories” (`pur456-pbc-finite-category`, in [sk-thm-sf-comp-composition]). The superscripts $+$ and $b$ denote the full subcategories of objects whose cohomology module objects vanish in all sufficiently negative degrees, respectively outside a finite interval. No derived-completeness condition, rationalization construction, or colimit of coefficient categories is part of this definition. Comparisons with such constructions require separate results.
