+++
id = "def-weil-pbc-property"
kind = "definition"
title = "Proper base-change property"
order = 1638
lean = ["AlgebraicGeometry.Etale.IsBaseChangeIso"]
uses = ["def-weil-pbc-derived-exchange"]
+++
For a proper morphism $f:X\to Y$, define $\mathsf{PBC}(f)$ to mean that for
every morphism $g:Y'\to Y$, every associated Cartesian square $\square$, and
every torsion sheaf $F$ on $X_{\mathrm{et}}$, the map
$\operatorname{Ex}_{\square,F}$ is an isomorphism in the derived category.
The assertion includes the specified map of Definition
[def-weil-pbc-derived-exchange], not an unnamed isomorphism.
