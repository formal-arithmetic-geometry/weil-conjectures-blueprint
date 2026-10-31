+++
id = "def-wf-monodromy-data"
kind = "definition"
title = "Monodromy data"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum"]
order = 3948
uses = ["d-monodromy", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "lem-wf-degree-components-grading"]
+++
For a represented degree datum $\rho$ ([d-monodromy]), the tuple
consisting of $\rho$, the geometric monodromy group $H$, the locally
finite-type extension $G_{\mathrm{arith}}(\rho)$, and the degree
components $G^{[m]}$ is called the *monodromy data* of $\rho$. The term
*arithmetic monodromy group* below always means this degree-graded
extension, with grading as in [lem-wf-degree-components-grading].

Its image in $\operatorname{GL}_n$ has as Zariski closures the
translates $HF^m$ of the degree components.
