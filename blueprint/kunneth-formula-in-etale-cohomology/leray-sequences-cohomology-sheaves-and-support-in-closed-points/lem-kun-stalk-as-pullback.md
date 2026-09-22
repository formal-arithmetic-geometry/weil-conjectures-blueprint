+++
id = "lem-kun-stalk-as-pullback"
kind = "lemma"
title = "A stalk is inverse image to a geometric point"
order = 6056
lean = ["AlgebraicGeometry.Etale.stalk_eq_pullback"]
uses = ["def-weil-pbc-pointed-etale-neighbourhoods"]
+++
If $\bar t:\Spec(\Omega)\to T$ is a geometric point, the stalk of a sheaf
(or derived object) at $\bar t$ is its inverse image along $\bar t$.

## Proof

Inverse image along $\bar t:\Spec(\Omega)\to T$ restricts a sheaf to the
site of $\Spec(\Omega)$; the sections over $\Spec(\Omega)$ of that
restriction are the colimit over the pointed étale neighbourhoods, which is
the stalk. For derived objects, exactness of the stalk functor passes the
statement to complexes.

Unresolved dependencies: def:weil-pbc-geometric-stalks, def:weil-pbc-inverse-image, def:weil-pbc-etale-site, prop:weil-pbc-geometric-stalks-exact
