+++
id = "lemma-finite-morphisms-cohomology--3"
kind = "lemma"
title = "The cohomology edge map of a finite morphism"
name_showing = false
order = 1594003
aliases = ["bp-r497-3"]
lean = ["AlgebraicGeometry.Etale.bijective_edgeMap_of_isFinite"]
uses = []
+++
Let $h:Y\to C$ be a finite morphism of schemes, let $G$ be an abelian
sheaf on $Y_{\acute{e}t}$, and let $q\geq0$. The composite

$$
H^q(C_{\acute{e}t},h_*G)
\longrightarrow H^q(Y_{\acute{e}t},h^*h_*G)
\xrightarrow{H^q(\varepsilon_G)} H^q(Y_{\acute{e}t},G),
$$

where the first map is pullback and $\varepsilon_G:h^*h_*G\to G$
is the counit, is bijective. Thus this canonical edge map identifies
$H^q(C_{\acute{e}t},h_*G)$ with $H^q(Y_{\acute{e}t},G)$.
