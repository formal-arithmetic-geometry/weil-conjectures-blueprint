+++
id = "lem-sc-zero-generic-acyclic"
kind = "lemma"
title = "Acyclicity of a sheaf with zero generic restriction"
order = 4524
lean = ["AlgebraicGeometry.Curve.cohomology_eq_zero_of_genericRestriction_eq_zero"]
+++
Let $C$ be an integral separated curve over an algebraically closed field,
and let $F$ be a torsion étale sheaf whose restriction to the generic point
is zero. Then $H^q(C,F)=0$ for all $q>0$.

## Proof

For a finite set $S$ of closed points let $j_S:C\setminus S\to C$ and put
$F_S=\ker(F\to j_{S*}j_S^*F)$. We claim $F=\varinjlim_SF_S$.

Represent a section on a quasi-compact étale object $V\to C$. On each of the
finitely many irreducible components of $V$ its generic germ is zero. The
definition of a geometric stalk provides an étale neighborhood on which the
section is zero. The image of that neighborhood is open; the sheaf axiom
implies vanishing on the image. Thus the section vanishes off a finite
closed subset of $V$. Its image in $C$ is contained in a finite set of
closed points: a point of $V$ mapping to the generic point of $C$ lies in
the fibre $V_\eta$, which is zero-dimensional because $V\to C$ is
quasi-finite, and on the corresponding finite étale piece
$\operatorname{Spec}L\to\eta$ the sections are $F_\eta\otimes_AL=0$, the
generic stalk $F_\eta$ vanishing by hypothesis, so the section vanishes
there as well; the remaining points of its non-vanishing locus are closed
points whose image in $C$ is closed too. The section consequently belongs to
$F_S(V)$ for some $S$. This proves the claim on a basis, or on geometric
stalks by exactness of the stalk functors.

For $i_S:S\to C$, the map $F_S\to i_{S*}i_S^*F_S$ is an isomorphism: at a
point of $S$ it is the identity, and outside $S$ both stalks vanish. Finite
direct image is exact, so its cohomology is the cohomology on $S$. That is
zero in positive degrees, since $S$ is a finite disjoint union of spectra of
algebraically closed fields. Finally use the compatibility of cohomology
with filtered colimits.

Unresolved dependencies: def:sc-curves, def:weil-pbc-etale-sheaves, def:weil-pbc-etale-cohomology, prop:weil-pbc-geometric-stalks-exact, lem:weil-pbc-finite-direct-image-exact, lem:weil-pbc-zero-dimensional-cohomology, lem:weil-pbc-cohomology-filtered-colimit
