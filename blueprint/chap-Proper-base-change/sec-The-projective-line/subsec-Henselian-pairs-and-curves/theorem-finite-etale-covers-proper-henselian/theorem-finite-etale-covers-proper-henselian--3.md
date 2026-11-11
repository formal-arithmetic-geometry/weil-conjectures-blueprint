+++
id = "theorem-finite-etale-covers-proper-henselian--3"
kind = "theorem"
title = "Finite torsors"
order = 357002
aliases = ["bp-r108-3"]
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_one_constantSheaf_of_henselianRing"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "theorem-finite-etale-covers-proper-henselian--2"]
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

Indeed, these groups classify $M$-torsors, and the equivalence of
clause [theorem-finite-etale-covers-proper-henselian--2] transports finite étale covers, their group
actions, and the equations expressing simple transitivity.
