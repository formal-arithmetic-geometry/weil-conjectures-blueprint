+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-hypercover-descent"
+++
The finite-presentation requirement is part of
[def-weil-pbc-finite-split-hypercover]; it does not follow just from
truncating a simplicial object. There are finitely many nondegenerate terms,
face maps, and simplicial identities through degree $r$. Apply
[lem-weil-pbc-etale-finite-data-descent] to these data, including the
splitting isomorphisms. Matching schemes are finite limits, so their
formation commutes with base change. The last assertion of that lemma makes
each of the finitely many descended matching maps a cover at a common later
stage. The same finite-data argument descends morphisms and equalities. If a
full hypercover is needed at that stage, continue above degree $r$ by taking
the matching scheme itself as a new nondegenerate covering term in each
degree.

Construct the refinement inductively. In degree zero, quasi-compactness of
$X_\infty$ lets us choose a finite subcover by quasi-compact etale objects.
Suppose degrees $<r$ have been chosen. The $r$th matching object is a finite
limit of lower-degree objects, because the boundary diagram of the simplex
$r$-simplex has finitely many faces. It is therefore quasi-compact and
quasi-separated. Cover it by finitely many quasi-compact etale objects and
adjoin the degenerate summands prescribed by the already chosen degeneracy
maps. This gives a split hypercover through degree $r$. Iterating to $N$
gives the required finite skeleton.

Every chosen component is of finite presentation over $X_\infty$, so it is
the pullback of an etale component at some stage. There are only finitely
many components, face maps, degeneracy maps, and augmentations through
degree $N$; finite presentation descends them all to one common stage.
The simplicial identities are finitely many equalities of morphisms between
finitely presented schemes and hence hold after a further common stage.
For each $r\leq N$, the map to the matching object is an etale cover after
pullback to $X_\infty$. Etaleness descends by a Jacobian etale algebra
presentation
$B=A[x_1,\ldots,x_m]/(f_1,\ldots,f_m)$ with an invertible Jacobian minor.
Surjectivity also descends: the complement of the image is constructible and
quasi-compact; if it survived at every later stage, its inverse limit would
give a point outside the limiting image. Thus, after one more stage, all
matching maps are covers. The same finite-presentation argument descends a
morphism of skeleta. Equality of two morphisms is the factorization through
their equalizer, a finitely presented closed condition, so it too holds at a
later stage.
