+++
id = "proposition-pro-etale-site-separably-closed--3"
kind = "proposition"
title = "The pro-étale site of a separably closed field (3)"
name_showing = false
order = 173005
aliases = ["bp-r050-3"]
lean = ["AlgebraicGeometry.ProEtale.constantSheafIsoContinuousSheaf", "AlgebraicGeometry.ProEtale.constantSheafIsoContinuousMapAddSheaf", "Profinite.continuousMapRingSheaf"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1"]
+++
Let $X$ be a scheme and $A$ a discrete abelian group. The constant
pro-étale sheaf with value $A$ is canonically isomorphic to the sheaf
$U\mapsto C(U,A)$ of continuous functions, by the map sending a
constant section to the corresponding constant function. In particular,
this identifies the underlying abelian sheaf of a discrete coefficient
ring with its sheaf of locally constant functions.

For any topological ring $R$, the functor

$$
\underline R(S)=C(S,R)
$$

on profinite sets is a sheaf of rings for the coherent topology, with
pointwise ring operations and restriction by precomposition. This
applies in particular to profinite and locally profinite rings.
