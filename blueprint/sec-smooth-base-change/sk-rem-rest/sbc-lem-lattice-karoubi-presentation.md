+++
id = "sbc-lem-lattice-karoubi-presentation"
kind = "lemma"
title = "The Karoubi presentation of an integral lattice"
order = 1462
uses = ["def-weil-karoubi-envelope", "def-weil-pbc-rational-category", "sbc-def-admissible-lattices", "thm-weil-pbc-finite-stage-karoubian"]
+++
In the situation of [sbc-def-admissible-lattices], the datum of an
integral lattice for
$K_E\in\Dbc(T,E)$ is equivalent to the datum of a pair $(L,e)$, where
$L\in\Dbc(T_{\Proet},\mathcal O_E)$ and $e$ is an idempotent
endomorphism of $L[\varpi^{-1}]$ with $e^2=e$, together with an
isomorphism $(L[\varpi^{-1}],e)\cong K_E$ in the Karoubi envelope of
the rationalized category of [def-weil-pbc-rational-category].

## Proof

By [thm-weil-pbc-finite-stage-karoubian] the rationalized category
$\Dbc(T,E)$ of [def-weil-pbc-rational-category] is idempotent
complete and the canonical functor into its Karoubi envelope of
[def-weil-karoubi-envelope] is an exact equivalence. Under this
equivalence an isomorphism $(L[\varpi^{-1}],e)\cong K_E$ in the
envelope is the same datum as an isomorphism
$L[\varpi^{-1}]\cong K_E$ in $\Dbc(T,E)$ together with an idempotent
$e$ on $L[\varpi^{-1}]$ whose image is carried to $K_E$; an integral
lattice in the sense of [sbc-def-admissible-lattices] is exactly
the datum of such an $L$ and such an isomorphism, the idempotent being
absorbed into the isomorphism because the equivalence is an equivalence
of categories.
