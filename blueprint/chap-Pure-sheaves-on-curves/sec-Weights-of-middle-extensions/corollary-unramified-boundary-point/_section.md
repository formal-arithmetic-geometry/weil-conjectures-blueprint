+++
id = "corollary-unramified-boundary-point"
kind = "corollary"
title = "An unramified boundary point"
order = 1186
lean = ["AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.isPureOfWeight_stalk_directImage_of_isLisse"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-perfect-complexes-geometric-point", "definition-weights", "definition-weil-representation", "definition-middle-extension"]
+++
Let $\mathcal F$ be a [lisse](@definition-lisse-sheaves) sheaf, [pure](@definition-weights) of weight $a$, on a smooth
geometrically connected curve with a point removed. If the inertia at the removed point acts
trivially, then the stalk at that point of the direct image of
$\mathcal F$ to the curve is [pure](@definition-weights) of weight $a$. In particular, a [lisse](@definition-lisse-sheaves) [Weil sheaf](@definition-weil-structure) on a smooth geometrically
connected curve that is [pure](@definition-weights) on a dense open is [pure](@definition-weights) on the whole
curve.
