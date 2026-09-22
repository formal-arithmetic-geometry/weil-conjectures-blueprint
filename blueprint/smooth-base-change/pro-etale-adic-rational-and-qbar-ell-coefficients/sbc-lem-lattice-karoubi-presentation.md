+++
id = "sbc-lem-lattice-karoubi-presentation"
kind = "lemma"
title = "The Karoubi presentation of an integral lattice"
order = 5243
lean = ["AlgebraicGeometry.Proetale.IntegralLattice.karoubiEquiv"]
uses = ["sbc-def-admissible-lattices"]
+++
In the situation of [sbc-def-admissible-lattices], the datum of an integral
lattice for $K_E\in\Dbc(T,E)$ is equivalent to the datum of a pair $(L,e)$,
where $L\in\Dbc(T_{\Proet},\mathcal O_E)$ and $e$ is an idempotent
endomorphism of $L[\varpi^{-1}]$ with $e^2=e$, together with an isomorphism
$(L[\varpi^{-1}],e)\cong K_E$ in the Karoubi envelope of the rationalized
category.

## Proof

The rationalized category $\Dbc(T,E)$ is idempotent complete and the
canonical functor into its Karoubi envelope is an exact equivalence. Under
this equivalence an isomorphism $(L[\varpi^{-1}],e)\cong K_E$ in the
envelope is the same datum as an isomorphism $L[\varpi^{-1}]\cong K_E$ in
$\Dbc(T,E)$ together with an idempotent $e$ on $L[\varpi^{-1}]$ whose image
is carried to $K_E$; an integral lattice in the sense of
[sbc-def-admissible-lattices] is exactly the datum of such an $L$ and such
an isomorphism, the idempotent being absorbed into the isomorphism because
the equivalence is an equivalence of categories.

Unresolved dependencies: def:weil-pbc-rational-category, def:weil-karoubi-envelope, thm:weil-pbc-finite-stage-karoubian
