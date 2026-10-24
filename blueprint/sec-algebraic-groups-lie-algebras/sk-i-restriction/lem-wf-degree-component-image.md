+++
id = "lem-wf-degree-component-image"
kind = "lemma"
title = "Matrix image of a degree component"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.image_degreeComponent_eq_closure"]
order = 3738
uses = ["d-monodromy", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components"]
+++
In the situation of [def-wf-degree-components], for every
$m\in\mathbf Z$ the image of $G^{[m]}$ under the matrix map
$(h,m)\mapsto hF^m$ of
[def-wf-arithmetic-monodromy-extension] is the Zariski closure
$\overline{\rho(\deg^{-1}(m))}^{\,\mathrm{Zar}}$ inside
$\operatorname{GL}_n$, that is, the translate $HF^m$ of the geometric
monodromy group $H$ of [d-monodromy].
