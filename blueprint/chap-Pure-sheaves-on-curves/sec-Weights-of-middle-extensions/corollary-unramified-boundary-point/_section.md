+++
id = "corollary-unramified-boundary-point"
kind = "corollary"
title = "An unramified boundary point"
order = 1186
lean = ["AlgebraicGeometry.BoundaryDatum.isPunctuallyPure_of_isPunctuallyPure_restrict", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.isPureOfWeight_stalk_directImage_of_isLisse"]
uses = ["lemma-stability", "definition-weil-representation"]
+++
Let $\mathcal F$ be a lisse sheaf, pure of weight $a$, on a smooth
geometrically connected curve with a point removed. If the inertia at the removed point acts
trivially, then the stalk at that point of the direct image of
$\mathcal F$ to the curve is pure of weight $a$. In particular, a lisse Weil sheaf on a smooth geometrically
connected curve that is pure on a dense open is pure on the whole
curve.
