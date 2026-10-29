+++
id = "lem-sc-brauer-injectivity"
kind = "lemma"
title = "Brauer classes are determined by the generic fibre"
order = 1442
uses = ["def-br", "lem-sc-point-z-cohomology", "lem-sp-grothendieck-edge-maps", "thm-sc-hilbert-90"]
lean = ["AlgebraicGeometry.Scheme.injective_cohomologyMap_gmSheaf_two"]
+++
Let $X$ be an integral regular noetherian scheme (for example a
connected smooth scheme over a field) with generic point
$j:\eta=\operatorname{Spec}k(X)\to X$. Then the restriction to the
generic point induces an injection (Grothendieck)

$$
\operatorname{Br}(X):=H^2(X_{\Et},\mathbf G_m)\longrightarrow
H^2(k(X)_{\Et},\mathbf G_m)=\operatorname{Br}(k(X)).
$$

In particular this holds for every smooth connected curve $C$ over a
field, proper or not, where $H^2(C_{\Et},\mathbf G_m)$ is the Brauer
group $\operatorname{Br}(C)$ of [def-br].
