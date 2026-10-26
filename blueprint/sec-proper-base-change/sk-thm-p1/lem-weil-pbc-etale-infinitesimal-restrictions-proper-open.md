+++
id = "lem-weil-pbc-etale-infinitesimal-restrictions-proper-open"
kind = "lemma"
title = "An open containing the closed fiber of a proper scheme over a complete base is everything"
uses = ["def-pc-base-change"]
lean = ["AlgebraicGeometry.proper_closed_fiber_open_eq_top"]
order = 1706
+++
Let $A$ be a commutative ring which is $I$-adically complete for an ideal $I\subseteq A$. Let $f:Y\to\operatorname{Spec}A$ and $g:X\to Y$ be morphisms of schemes with $f\circ g$ proper. Let $W\subseteq X$ be an open subset containing $g^{-1}$ of the image of the projection $Y\times_{\operatorname{Spec}A}\operatorname{Spec}(A/I)\to Y$ [def-pc-base-change]. Then $W=X$.
