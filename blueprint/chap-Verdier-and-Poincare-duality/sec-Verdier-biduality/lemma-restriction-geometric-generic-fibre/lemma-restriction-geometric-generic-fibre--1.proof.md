+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--1"
order = 838004
uses = ["theorem-generic-constructibility-base-change-rj"]
+++
First let $L$ be a constructible sheaf in degree zero. Deligne's generic
base change theorem [theorem-generic-constructibility-base-change-rj],
in its finite-ring form for noetherian base changes, gives a nonempty open
$B_0\subset B$ over which the formation of $Rj_*L$ commutes with base
change. The generic point belongs to every nonempty open of the integral
scheme $B$. Thus $t$ has image in $B_0$, and the comparison for $L$ is an
isomorphism.

For a bounded constructible complex, use its finite truncation filtration.
The complexes for which the comparison is an isomorphism form a
triangulated subcategory, and the preceding argument applies to each
cohomology sheaf. This is the dévissage
`AlgebraicGeometry.Etale.prop_of_boundedConstructible` in the Lean proof.
