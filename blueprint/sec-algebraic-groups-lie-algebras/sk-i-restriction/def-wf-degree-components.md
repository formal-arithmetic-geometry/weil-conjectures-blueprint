+++
id = "def-wf-degree-components"
kind = "definition"
title = "Degree components and algebraic-monodromy elements"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.degreeComponent", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.degreeComponent_eq_range"]
order = 3740
uses = ["def-wf-arithmetic-monodromy-extension", "def-wf-geometric-monodromy-group", "def-wf-weil-group"]
+++
For $m\in\mathbf Z$, put

$$
G^{[m]}=H_{\mathrm{geom}}\times\{m\}.
$$

An element of $G^{[m]}$ is called an
*algebraic-monodromy element of degree $m$*. The integer degree is
the component index in [def-wf-arithmetic-monodromy-extension]; it is
not a regular function on a finite-type algebraic group.
