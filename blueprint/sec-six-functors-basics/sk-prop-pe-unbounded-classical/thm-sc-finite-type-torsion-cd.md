+++
id = "thm-sc-finite-type-torsion-cd"
kind = "theorem"
title = "Torsion cohomological dimension of a finite-type scheme"
lean = ["AlgebraicGeometry.Scheme.subsingleton_H_of_two_mul_add_lt"]
order = 1911
uses = ["def-sc-etale-torsion-cd", "def-sc-zariski-cohomology", "def-sc-zariski-site", "def-weil-pbc-scheme-conventions", "lem-sc-zariski-dimension-bound", "thm-sc-affine-torsion-cd", "thm-sp-grothendieck"]
+++
Let $K$ be a field with $\operatorname{cd}_{\rm tor}(K)\leq c$,
and let $X$ be a finite-type
$K$-scheme of dimension $d$.
Then $\operatorname{cd}_{\rm tor}(X)\leq2d+c$, in the sense of
[def-sc-etale-torsion-cd].
