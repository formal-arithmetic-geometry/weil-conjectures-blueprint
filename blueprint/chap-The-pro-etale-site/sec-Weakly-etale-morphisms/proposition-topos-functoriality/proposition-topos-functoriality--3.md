+++
id = "proposition-topos-functoriality--3"
kind = "proposition"
title = "The topos and its functoriality (3)"
name_showing = false
order = 39003
aliases = ["bp-r006-3"]
lean = ["AlgebraicGeometry.ProEtale.setPullbackComp"]
uses = ["proposition-topos-functoriality--2"]
+++
For morphisms $f:X\to Y$ and $g:Y\to Z$ of schemes in a universe $u$,
the inverse images on sheaves of sets in universe $u+1$ have a canonical
isomorphism

$$
(g\circ f)^{-1}\simeq f^{-1}\circ g^{-1}.
$$

It is the isomorphism of left adjoints corresponding, under the
adjunctions of [proposition-topos-functoriality--2], to the canonical
isomorphism $g_*\circ f_*\simeq(g\circ f)_*$.
