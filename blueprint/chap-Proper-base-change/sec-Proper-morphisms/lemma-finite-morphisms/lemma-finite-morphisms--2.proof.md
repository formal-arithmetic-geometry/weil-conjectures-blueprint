+++
kind = "proof"
of = "lemma-finite-morphisms--2"
order = 384005
uses = ["lemma-finite-morphisms--1", "definition-underived-base-change-map"]
+++
The functor $u_*$ preserves finite limits, being a right adjoint. By
[lemma-finite-morphisms--1], its effect on an epimorphism at a geometric
stalk is a finite product of epimorphisms. Under the stated assumptions on
the forgetful functor, the geometric stalks with algebraically closed
residue fields jointly detect epimorphisms. Hence $u_*$ preserves
epimorphisms, and is exact.

The base change $u'$ is finite. For a geometric point $\bar w'$ of $W'$,
the cartesian square identifies the geometric fibre of $u'$ at $\bar w'$
with that of $u$ at $g\bar w'$. Apply the stalk formula to $u$ and $u'$,
and identify the stalk of an inverse image with the stalk at the image
point. Under these identifications, the base change map is the reindexing
of the same finite product of stalks of $F$.

To check the map itself, express [definition-underived-base-change-map]
using the unit for $g'^*\dashv g'_*$, the composition isomorphisms for
direct images, and the counit for $g^*\dashv g_*$. On stalks the counit is
restriction of germs, and the composition isomorphisms respect successive
restrictions. The triangle identity for the unit and counit then shows
that each product projection is the corresponding restriction map. Thus
the base change map is an isomorphism at every geometric stalk, and
conservativity gives the assertion for sheaves.
