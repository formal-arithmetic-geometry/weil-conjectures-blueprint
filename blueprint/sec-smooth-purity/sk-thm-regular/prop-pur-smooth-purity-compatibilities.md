+++
id = "prop-pur-smooth-purity-compatibilities"
kind = "theorem"
title = "Compatibilities of smooth purity"
order = 2114
tags = ["latex:proposition"]
uses = ["def-coefficient-twists-detailed", "def-exchange-projection", "def-pur-conventions", "def-pur-smooth-purity-map", "def-sbc-smooth-morphisms", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-exceptional-adjoint-admissibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-pur-regular-immersion-purity-compatibilities", "thm-pur-cohomological-smoothness", "thm-pur-finite-coefficient-smooth-purity", "thm-pur-regular-immersion-purity"]
+++
In the situation of [thm-pur-finite-coefficient-smooth-purity],
the smooth purity map is compatible with the
adjunction
$Rf_!\dashv Rf^!$, with the
[def-weil-derived-cohomology-sheaves] cohomology sheaves and
truncations, and with the
Tate-twist structure.

## Proof

All the constituents of [def-pur-smooth-purity-map] are canonical
derived tensor and internal-Hom transformations: the tensor formula
[thm-pur-cohomological-smoothness] is compatible
with the adjunction and with the cohomology sheaves by its definition
(the canonical isomorphism is the mate of the projection formula
[def-exchange-projection], and the derived tensor and internal-Hom
are those of [def-weil-derived-pullback-tensor-hom] and
[def-weil-derived-tensor]), the twist isomorphisms
[def-coefficient-twists-detailed] are compatible with the twists, and
[thm-pur-regular-immersion-purity] is compatible with the same
structures on the immersion side (the classes are the boundaries of the
Kummer products, whose cup-compatibility is
[prop-pur-regular-immersion-purity-compatibilities]);
composing the compatibilities along
[def-pur-smooth-purity-map] gives the assertion.
