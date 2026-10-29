+++
id = "def-sfb-mate-push-hom"
kind = "definition"
title = "The mate comparison in a square of adjunctions"
order = 1340
uses = ["def-sfb-conjugate-pull-iso"]
lean = ["CategoryTheory.Adjunction.pushHomOfComapIso"]
+++
In the situation of [def-sfb-conjugate-pull-iso] (only the adjunctions
$E_1\dashv\mathrm{Res}_1$ and $E_2\dashv\mathrm{Res}_2$ are needed), the *mate* of
$e^{-1}\colon L_1\circ\mathrm{Res}_1\to\mathrm{Res}_2\circ L_2$ is the natural transformation

$$
E_2\circ L_1\longrightarrow L_2\circ E_1\colon\mathcal A\longrightarrow\mathcal B',
$$

the composite
$E_2L_1\xrightarrow{E_2L_1\eta_1}E_2L_1\mathrm{Res}_1E_1\xrightarrow{E_2e^{-1}E_1}
E_2\mathrm{Res}_2L_2E_1\xrightarrow{\varepsilon_2L_2E_1}L_2E_1$, with $\eta_1$ the unit of
$E_1\dashv\mathrm{Res}_1$ and $\varepsilon_2$ the counit of $E_2\dashv\mathrm{Res}_2$. It is not
an isomorphism in general.
