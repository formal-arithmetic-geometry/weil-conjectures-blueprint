+++
id = "thm-zl-real-mixed-by-curves"
kind = "theorem"
title = "Mixedness of real sheaves by reduction to the proved curve case"
order = 4289
lean = ["AlgebraicGeometry.WeilSheaf.IsReal.isMixed"]
uses = ["def-weil-punctual-weights", "def-wf-iota-real", "i-topology", "lem-a1-mixed-direct-summand", "lem-zl-curve-testing-irreducibility", "lem-zl-finite-pushforward", "lem-zl-geometric-constituents-any-base", "sk-lem-coefficient-heart", "thm-rp-real-lisse-purity-affine", "lem-zl-quasi-finite", "sk-r-real-linear", "sk-prop-sf-open-closed-triangle"]
+++
Every constructible $\iota$-real $\Qlb$-Weil sheaf (an object of
$\Cons(X,\Qlb)$ [sk-lem-coefficient-heart] with a Weil structure) on a separated
finite-type scheme over a finite field is $\iota$-mixed, with a
finite filtration in the sense of [def-weil-punctual-weights].
