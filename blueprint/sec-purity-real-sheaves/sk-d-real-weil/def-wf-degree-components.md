+++
id = "def-wf-degree-components"
kind = "definition"
title = "Degree components and algebraic-monodromy elements"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.degreeComponent", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.degreeComponent_eq_range"]
order = 3942
uses = ["d-monodromy", "def-wf-arithmetic-monodromy-extension"]
+++
For a represented degree datum ([d-monodromy]) with geometric monodromy
group $H$ and $m\in\mathbf Z$, put

$$
G^{[m]}=H\times\{m\}\subseteq G_{\mathrm{arith}}(\rho).
$$

An element of $G^{[m]}$ is called an
*algebraic-monodromy element of degree $m$*. The integer degree is
the component index in [def-wf-arithmetic-monodromy-extension]; it is
not a regular function on a finite-type algebraic group.
