+++
id = "def-sfb-point-lower-star"
kind = "definition"
title = "The direct image $p_*$ to the point"
order = 1041
uses = ["lem-sfb-profinite-to-proetale-continuous"]
lean = ["AlgebraicGeometry.ProEtale.pointLowerStar"]
+++
The *direct image to the point* is the functor
$$
p_*\colon\Sh((\Spec\Z)_{\mathrm{proét}},\Ab)\longrightarrow\Sh(*_{\mathrm{proét}},\Ab),
\qquad(p_*G)(S)=G(\Spec LC(S,\Z)),
$$
given by restriction along $u$.
