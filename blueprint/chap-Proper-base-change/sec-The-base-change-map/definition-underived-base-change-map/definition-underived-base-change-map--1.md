+++
id = "definition-underived-base-change-map--1"
kind = "definition"
title = "Underived base change map (1)"
name_showing = false
order = 315001
aliases = ["bp-r093-1"]
lean = ["AlgebraicGeometry.Etale.baseChangeMap", "AlgebraicGeometry.Etale.upperStar_map_baseChangeMap_app_counit"]
+++
Let $F$ be a sheaf on $X_{\acute{e}t}$. The *underived base change map*

$$
g^*f_*F\longrightarrow f'_*g'^*F
\tag{4.2}
$$

is the adjoint, under $f'^*\dashv f'_*$, of

$$
f'^*g^*f_*F
\simeq g'^*f^*f_*F
\xrightarrow{g'^*\varepsilon_f}g'^*F,
$$

where $\varepsilon_f:f^*f_*\to\mathrm{id}$ is the counit.
