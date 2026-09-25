+++
id = "prop-weil-derived-operations-well-defined"
kind = "theorem"
title = "Well-definedness of the derived operations"
order = 1836
tags = ["latex:proposition"]
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-proetale-site"]
+++
The functors of
[def-weil-derived-pullback-tensor-hom] – derived pullback,
derived tensor product, and derived internal Hom – are independent of
the chosen resolutions and give triangulated functors on the ambient
derived categories.

## Proof

The operations of [def-weil-derived-pullback-tensor-hom] are defined
by choosing K-flat resolutions for the derived tensor products and
K-injective resolutions for the derived internal Hom, with the
conventions of [def-weil-derived-tensor]. Any two K-flat
resolutions of the same complex are connected by a zig-zag of
quasi-isomorphisms between K-flat complexes, and tensoring with a K-flat
complex preserves quasi-isomorphisms, so the derived tensor product does
not depend on the chosen resolution; likewise any two K-injective
resolutions of the second variable are homotopy equivalent, so the
derived internal Hom is independent of the choice. Deriving functors
this way in both variables is compatible with shifts, cones, and
distinguished triangles in the source variables, and both operations
are exact triangulated functors in each variable on the ambient derived
categories built from the corresponding small pro-etale site. The
finite-torsion, complete, rational, and common-stage coefficient
variants of [def-weil-derived-pullback-tensor-hom] are obtained
from the levelwise instances of the same construction and hence inherit
the same properties.
