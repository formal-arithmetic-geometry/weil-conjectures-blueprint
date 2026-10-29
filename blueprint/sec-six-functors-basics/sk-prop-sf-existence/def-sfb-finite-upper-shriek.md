+++
id = "def-sfb-finite-upper-shriek"
kind = "definition"
title = "Exceptional pullback $Rf^!$ (pro-étale, finite coefficients)"
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriek"]
order = 2553
uses = ["def-weil-pbc-site-comparison-morphism", "sk-def-nagata-sketch-data", "thm-sfb-finite-lower-shriek-left-adjoint"]
+++
Let $\Lambda$ be a finite ring and let $f\colon X\to Y$ admit a compactification
[sk-def-nagata-sketch-data]. The *exceptional pullback* of $f$ on pro-étale sheaves is

$$
Rf^!:=\nu_X^*\circ f^\times\circ R\nu_{Y,*}\colon D(Y_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda),
$$

where $\nu$ is the comparison morphism of [def-weil-pbc-site-comparison-morphism] and $f^\times$
is the étale exceptional inverse image of [thm-sfb-finite-lower-shriek-left-adjoint]. It is
defined on the whole unbounded derived category but used only on bounded below objects, where
it is right adjoint to $Rf_!$ on objects of étale origin ([def-sfb-finite-shriek-adjunction]).
It is not a right adjoint of the pro-étale $Rf_!$ on $D(X_{\mathrm{proét}},\Lambda)$, which in
general has none.
