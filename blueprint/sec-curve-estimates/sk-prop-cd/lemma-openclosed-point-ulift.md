+++
id = "lemma-openclosed-point-ulift"
kind = "lemma"
title = "Raising a point a universe"
order = 990
lean = ["AlgebraicGeometry.Scheme.isConservativeFamilyOfPoints_ulift_pointSmallEtale", "CategoryTheory.GrothendieckTopology.Point.ulift"]
uses = ["def-kun-separably-closed"]
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

## Proof

The universe-raising functor $\mathrm{Type}\,w\to\mathrm{Type}\,\max(w,w')$ is
fully faithful and is a bijection on elements: the elements of the raised set
$\uparrow\!p(U)$ are exactly the elements of $p(U)$. Hence the category of
elements of the composite fibre functor is isomorphic to that of $p$, so it is
again cofiltered and initially small, and the joint surjectivity of $p$ on a
covering sieve transfers verbatim. So the composite is a point. A stalk is a
colimit over the opposite of the category of elements, which has not changed,
and the raising functor preserves these $w$-small colimits; so the stalks of
the raised point are the old ones followed by the raising functor, and they
detect exactly the same isomorphisms.

For the second statement, conservativity of a family of points is checked
against a covering-sieve criterion: a family is conservative as soon as every
sieve $S$ on an object $V$ whose associated subobject of the sheaf represented
by $V$ has full stalk at every point of the family is a covering sieve. That
criterion mentions no fibre universe, so it holds for the raised family as
soon as it holds for the original one. For $\et X$ the original family
consists, for each $s\in X$, of the geometric point
$\operatorname{Spec}\overline{\kappa(s)}\to X$ at an algebraic closure of
$\kappa(s)$, which is separably closed [def-kun-separably-closed]. These
geometric points are jointly surjective onto $X$, since the one indexed by $s$
has image $s$. A jointly surjective family of geometric points with separably
closed fields is conservative on the small étale site: for $V$ étale over $X$
and $v\in V$ over $s$, the finite separable extension $\kappa(v)/\kappa(s)$
embeds into $\overline{\kappa(s)}$, so $v$ is visible from the geometric point
at $s$, and a sieve whose subobject has full stalk at that point contains an
étale neighbourhood of $v$; the sieve therefore contains a family jointly
surjective onto $V$, which is a covering.
