+++
kind  = "proof"
of    = "lemma-openclosed-point-ulift"
+++
The universe-raising functor $\mathrm{Type}\,w\to\mathrm{Type}\,\max(w,w')$ is
fully faithful and is a bijection on elements: the elements of the raised set
$\uparrow\!p(U)$ are exactly the elements of $p(U)$. Hence the category of
elements of the composite fibre functor is isomorphic to that of $p$, so it is
again cofiltered and initially small, and the joint surjectivity of $p$ on a
covering sieve transfers verbatim. So the composite is a point. A stalk is a
colimit over the opposite of the category of elements, which has not changed,
so the stalk of a sheaf at the raised point is computed by a colimit over an
isomorphic index category and is canonically isomorphic to its stalk at $p$;
in particular the two points detect exactly the same isomorphisms.

For the second statement, conservativity of a family of points is checked
against a covering-sieve criterion: a family is conservative as soon as every
sieve $S$ on an object $V$ whose associated subobject of the sheaf represented
by $V$ has full stalk at every point of the family is a covering sieve. That
criterion mentions no fibre universe, so it holds for the raised family as
soon as it holds for the original one. For $\et X$ the original family
consists, for each $s\in X$, of the geometric point
$\operatorname{Spec}\overline{\kappa(s)}\to X$ at an algebraic closure of
$\kappa(s)$, which is separably closed [def-pc-separably-closed]. These
geometric points are jointly surjective onto $X$, since the one indexed by $s$
has image $s$. A jointly surjective family of geometric points with separably
closed fields is conservative on the small étale site: for $V$ étale over $X$
and $v\in V$ over $s$, the finite separable extension $\kappa(v)/\kappa(s)$
embeds into $\overline{\kappa(s)}$, so $v$ is visible from the geometric point
at $s$, and a sieve whose subobject has full stalk at that point contains an
étale neighbourhood of $v$; the sieve therefore contains a family jointly
surjective onto $V$, which is a covering.
