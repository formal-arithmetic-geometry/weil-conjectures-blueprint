+++
id = "sbc-lem-higher-direct-image-presheaf"
kind = "lemma"
title = "Higher direct image as a sheafified cohomology presheaf"
order = 1428
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology"]
+++
Let $h:Y\to X$ be a morphism of schemes and $F\in\Ab(Y_{\Et})$. Then
$R^qh_*F$ is the sheaf associated with the presheaf

$$
(U\to X)\longmapsto H^q\bigl(U\times_XY,F|_{U\times_XY}\bigr)
$$

on $X_{\Et}$; more generally for $K\in D(Y_{\Et})$ the cohomology sheaf
$R^qh_*K$ is associated with $U\mapsto H^q(U\times_XY,K|_{U\times_XY})$.
