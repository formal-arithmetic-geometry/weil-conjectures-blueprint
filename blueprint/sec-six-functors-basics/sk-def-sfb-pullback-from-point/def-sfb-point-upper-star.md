+++
id = "def-sfb-point-upper-star"
kind = "definition"
title = "The inverse image $p^*$ from the point"
order = 1538
uses = ["lem-sfb-point-lan-exists", "sk-def-sfb-finite-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.pointUpperStar"]
+++
The *inverse image from the point* is the functor
$$
p^*:=\mathrm{sheafify}\circ\operatorname{Lan}_{u^{\mathrm{op}}}\colon
\Sh(*_{\mathrm{proét}},\Ab)\longrightarrow\Sh((\Spec\Z)_{\mathrm{proét}},\Ab).
$$
It takes the left Kan extension of the underlying presheaf along $u^{\mathrm{op}}$
and then sheafifies.
