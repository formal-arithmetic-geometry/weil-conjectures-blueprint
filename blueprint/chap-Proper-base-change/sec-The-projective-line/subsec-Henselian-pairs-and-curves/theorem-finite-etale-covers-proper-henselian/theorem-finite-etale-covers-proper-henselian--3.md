+++
id = "theorem-finite-etale-covers-proper-henselian--3"
kind = "remark"
title = "Finite torsors"
order = 357002
aliases = ["bp-r108-3"]
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_one_constantSheaf_of_henselianRing"]
uses = []
+++
Let $(B,J)$ be a henselian pair, let $Y$ be proper over $B$, and let
$i:Y_0\to Y$ be the closed fibre over $B/J$. For every finite abelian
group $M$, restriction on étale cohomology is a bijection

$$
H^1(Y,\underline M)\xrightarrow{\sim}H^1(Y_0,\underline M).
\tag{4.8}
$$

Here the target of the restriction map is first
$H^1(Y_0,i^*\underline M)$, which we identify with
$H^1(Y_0,\underline M)$ using the canonical isomorphism
$i^*\underline M\simeq\underline M$.

*Proof.* Apply [theorem-finite-etale-covers-proper-henselian--2]. We use the
general fact that an equivalence on finite étale schemes induced by
base change gives a bijection on $H^1$ with finite constant
coefficients.

Indeed, $H^1$ classifies torsors, and a torsor under the finite constant
group $M$ is represented by a finite étale scheme. Full faithfulness
lifts isomorphisms between restricted torsors and their inverses;
faithfulness shows that the lifted maps commute with the $M$-actions
and are inverse. This proves injectivity on isomorphism classes of
torsors.

For surjectivity, lift the finite étale scheme representing a torsor
on $Y_0$ by essential surjectivity. Fullness lifts each action map,
and faithfulness gives the identity and addition equations. The map
from the disjoint union of copies of the lifted scheme $P$, indexed
by $M$, to $P\times_YP$ becomes an isomorphism after restriction.
An equivalence reflects isomorphisms, so the lifted action is simply
transitive. We must also check that $P\to Y$ is surjective. Its image
is open and closed because the map is finite étale. The inclusion of
this image is finite étale and becomes an isomorphism over $Y_0$;
reflection of isomorphisms shows that the image is all of $Y$.
Thus the lifted scheme with its action represents a torsor.

Finally, the classification of torsors by $H^1$ is compatible with
inverse image and with isomorphisms of the coefficient sheaf. It
identifies this bijection on torsor classes with restriction
$H^1(Y,\underline M)\to H^1(Y_0,i^*\underline M)$.
The canonical isomorphism $i^*\underline M\simeq\underline M$ gives
the displayed comparison.
