+++
id = "prop-sfb-module-derived-lower-shriek-compactification-plus-restriction"
kind = "proposition"
title = "The bounded below derived lower shriek is a restriction"
order = 1698
uses = ["def-sfb-module-derived-lower-shriek-compactification", "def-sfb-module-derived-lower-shriek-compactification-plus"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekOfCompactificationPlusCompatibility"]
+++
Let $\Lambda$ be a commutative condensed ring and $c$ a compactification of a
morphism $f\colon X\to Y$. With $\iota\colon D^+\hookrightarrow D$ the inclusions of
the bounded below derived categories, there is a natural isomorphism

$$
\iota\circ R^+f^c_!\cong Rf^c_!\circ\iota
$$

between the functors of [def-sfb-module-derived-lower-shriek-compactification-plus]
and [def-sfb-module-derived-lower-shriek-compactification].
