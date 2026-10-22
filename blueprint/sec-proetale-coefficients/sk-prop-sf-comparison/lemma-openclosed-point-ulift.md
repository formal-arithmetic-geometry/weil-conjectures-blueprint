+++
id = "lemma-openclosed-point-ulift"
kind = "lemma"
title = "Raising a point a universe"
order = 998
lean = ["AlgebraicGeometry.Scheme.isConservativeFamilyOfPoints_ulift_pointSmallEtale", "CategoryTheory.GrothendieckTopology.Point.ulift"]
uses = ["def-pc-separably-closed"]
+++
Let $(\mathcal C,J)$ be a site and let $p$ be a point of it, given by a fibre
functor $\mathcal C\to\mathrm{Type}\,w$ (with cofiltered and initially small
category of elements, and jointly surjective on covering sieves). Then
composing the fibre functor with the universe-raising functor
$\mathrm{Type}\,w\to\mathrm{Type}\,\max(w,w')$ is again a point of
$(\mathcal C,J)$, and its stalks are the old ones up to the universe-raising
functor.

Applied to $\et X$ for a scheme $X$ in a universe $u$: the family of geometric
points of $\et X$ consisting, for each point $s\in X$, of the geometric point at
an algebraic closure of $\kappa(s)$, raised from $\mathrm{Type}\,u$ to
$\mathrm{Type}\,(u+1)$, is a conservative family of points.
