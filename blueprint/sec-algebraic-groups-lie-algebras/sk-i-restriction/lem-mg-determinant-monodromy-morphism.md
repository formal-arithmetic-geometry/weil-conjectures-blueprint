+++
id = "lem-mg-determinant-monodromy-morphism"
kind = "lemma"
title = "The determinant morphism of arithmetic monodromy"
order = 2865
uses = ["def-mg-determinant-line", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "lem-mg-degree-component-functoriality"]
+++
For a rank-$r$ Weil representation $\rho$, taking the
determinant line induces a
degree-preserving, componentwise regular homomorphism

$$
\Delta_\rho:\hyperref[def-wf-arithmetic-monodromy-extension]{G_{\mathrm{arith}}(\rho)}\longrightarrow
G_{\mathrm{arith}}(\det\rho),
\qquad (h,m)\longmapsto(\det h,m),
$$

whose image is dense on every degree
component. This is the determinant instance of the functoriality in
[lem-mg-degree-component-functoriality], and it sends central elements
to central elements.
