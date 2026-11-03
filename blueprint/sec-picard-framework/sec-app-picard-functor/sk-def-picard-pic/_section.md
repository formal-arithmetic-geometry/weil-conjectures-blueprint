+++
id = "sk-def-picard-pic"
kind = "definition"
title = "Relative Picard functor"
order = 876
lean = ["AlgebraicGeometry.picardFunctor", "AlgebraicGeometry.picardFunctorNormalized"]
uses = ["sk-lem-abelian-seesaw", "sec-nagata-compactification"]
tags = ["sketch"]
+++
For a morphism of schemes $f:C\to S$, let

$$
\operatorname{Pic}_{C/S}
=\bigl(T\longmapsto
\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)\bigr)^{\mathrm{fppf}}.
$$

Here $C_T=C\times_ST$, and the superscript denotes sheafification on
the big fppf site of $S$. Equivalently, one may sheafify
$T\mapsto\operatorname{Pic}(C_T)$, since an invertible sheaf on $T$
becomes trivial on a Zariski cover. When this functor is represented by
a scheme, we call the representing scheme the Picard scheme.
