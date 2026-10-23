+++
id = "det-def-sfb-sheaf-tensor-closed"
kind = "lemma"
title = "The tensor product of sheaves is closed and right exact"
lean = ["CategoryTheory.GrothendieckTopology.monoidalClosed_sheaf_of_essentiallySmall", "CategoryTheory.Monoidal.Reflective.monoidalClosed", "CategoryTheory.GrothendieckTopology.preservesColimitsOfSize_tensorLeft_sheaf_of_essentiallySmall", "CategoryTheory.GrothendieckTopology.preservesColimitsOfSize_tensorRight_sheaf_of_essentiallySmall"]
order = 1193
uses = ["det-def-sfb-sheaf-tensor-structure", "det-def-sfb-sheaf-tensor-hom-sheaf", "det-def-sfb-sheaf-tensor-presheaf"]
+++
In the situation of [det-def-sfb-sheaf-tensor-structure], for sheaves $\mathcal F,\mathcal G$ put
$\mathcal{H}om(\mathcal F,\mathcal G):=[\mathcal F,\mathcal G]$, the presheaf internal hom of
[det-def-sfb-sheaf-tensor-presheaf], which is a sheaf by [det-def-sfb-sheaf-tensor-hom-sheaf].
Then there are bijections
$$
\Hom_{\Sh}(\mathcal F\otimes\mathcal G,\mathcal H)\cong\Hom_{\Sh}\bigl(\mathcal G,\mathcal{H}om(\mathcal F,\mathcal H)\bigr),
$$
natural in all three variables. Hence $(\Sh(C,\mathcal A),\otimes)$ is closed symmetric monoidal,
and $\mathcal F\otimes-$ and $-\otimes\mathcal F$ preserve all colimits; in particular they are
additive and right exact.
