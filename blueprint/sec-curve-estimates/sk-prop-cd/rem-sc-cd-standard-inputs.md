+++
id = "rem-sc-cd-standard-inputs"
kind = "remark"
title = "The standard inputs used above"
order = 1009
uses = ["lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Four standard facts are used in the proofs above; we record them here so
that no step of the argument is left implicit.

1. A finite morphism has exact direct image with no higher direct
images, and its direct image preserves injective sheaves because its
inverse image is exact and left adjoint to it; this is
[lemma-weil-pbc-finite-direct-image-exact].
1. A separably closed residue field and a polynomial with a simple root
there admit a unique lift of that root, by the Hensel lifting lemma
for a strict henselian local ring; the simplicity is supplied by the
discriminant, a nonzero element of the coefficient field and hence a
unit in the strict local ring.
1. Vanishing of all geometric stalks of an etale sheaf forces the sheaf
to vanish; this is
[lemma-weil-pbc-geometric-stalk-conservative].
1. For a finite-type algebra over a field, the transcendence degree of
the residue field at a point bounds its local dimension, and a
proper closed subset of an irreducible finite-type scheme has
strictly smaller dimension.
