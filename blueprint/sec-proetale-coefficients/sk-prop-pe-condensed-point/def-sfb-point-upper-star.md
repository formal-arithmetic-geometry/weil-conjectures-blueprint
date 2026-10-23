+++
id = "def-sfb-point-upper-star"
kind = "definition"
title = "The inverse image $p^*$ from the point"
order = 1077
uses = ["lem-sfb-point-lan-exists", "det-pe-topos-functoriality-site"]
lean = ["AlgebraicGeometry.ProEtale.pointUpperStar"]
+++
The *inverse image from the point* is the functor
$$
p^*:=\mathrm{sheafify}\circ\operatorname{Lan}_{u^{\mathrm{op}}}\colon
\Sh(*_{\mathrm{proét}},\Ab)\longrightarrow\Sh((\Spec\Z)_{\mathrm{proét}},\Ab).
$$
It takes the left Kan extension of the underlying presheaf along $u^{\mathrm{op}}$
and then sheafifies.
