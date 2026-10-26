+++
id = "def-sfb-finite-lower-star-comp"
kind = "definition"
title = "Composition isomorphism for pushforwards"
order = 880
uses = ["def-sfb-finite-lower-star"]
lean = ["AlgebraicGeometry.ProEtale.lowerStarComp"]
+++
For morphisms $h_1\colon T\to S$ and $h_2\colon S\to R$, the *composition isomorphism*
of the pushforwards of [def-sfb-finite-lower-star] is

$$
(h_2)_*\circ(h_1)_*\xrightarrow{\ \sim\ }(h_2\circ h_1)_*,
$$

given on sections over $V\in R_{\mathrm{proét}}$ by restriction along the canonical
isomorphism $(V\times_RS)\times_ST\cong V\times_RT$.
