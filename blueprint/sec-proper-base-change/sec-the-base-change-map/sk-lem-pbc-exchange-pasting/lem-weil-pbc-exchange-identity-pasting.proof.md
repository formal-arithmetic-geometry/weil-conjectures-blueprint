+++
kind  = "proof"
of    = "lem-weil-pbc-exchange-identity-pasting"
+++
Both equations are checked with the uniqueness part of
[lemma-weil-pbc-derived-exchange-replacement]: a natural transformation
$g^{-1}Rf_*\to Rf'_*g'^{-1}$ is the derived exchange morphism
[def-weil-pbc-derived-exchange] as soon as its composite with $g^{-1}\eta_K$ is
the underived exchange morphism $\Ex^0_{\square,K}$ followed by the canonical
map $f'_*g'^{-1}K\to Rf'_*g'^{-1}K$; and since every object of $\Dplus$ is
isomorphic to a bounded below complex of injectives, on which the canonical
maps $\eta$ are isomorphisms, it suffices to check this on such complexes $I$.

*Identity square.* For the identity square ($g=\mathrm{id}_Y$,
$g'=\mathrm{id}_X$, $f'=f$) the square isomorphism $\theta_\square$ is the
composite of the unit isomorphisms $\mathrm{id}^{-1}\cong\mathrm{id}$, by the
compatibility with identities recorded in [def-weil-pbc-cartesian-square].
Its mate $\Ex^0_\square:\mathrm{id}^{-1}f_*\to f_*\mathrm{id}^{-1}$ is therefore
the identity of $f_*$ modulo these unit isomorphisms (the triangle identity
of $f^{-1}\dashv f_*$). The transformation $\mathrm{id}^{-1}Rf_*\cong
Rf_*\cong Rf_*\mathrm{id}^{-1}$ made of the unit isomorphisms satisfies the
characterizing identity, by naturality of $\mathrm{id}^{-1}\cong\mathrm{id}$
with respect to $\eta_K$; so it is $\Ex_\square$.

*Pasting.* For horizontally or vertically pasted squares, consider the
composite $\Phi$ of the two derived exchange morphisms with the associativity
isomorphisms. On a bounded below complex $I$ of injectives, all derived direct
images that occur are computed by underived direct images: $f_*I$ is again a
complex of injectives because $f_*$ is right adjoint to the exact functor
$f^{-1}$, and the characterizing identities for the two inner squares (the
second one applied to $f_*I$, resp. to $g'^{-1}I$) identify $\Phi_I\circ\eta_I$
with the canonical map following the composite of the two underived exchange
morphisms and the associativity isomorphisms. That underived composite is
$\Ex^0$ of the outer rectangle: each $\Ex^0$ is the mate of a square
isomorphism, the square isomorphism of the outer rectangle is the composite of
the two inner ones modulo composition isomorphisms
[def-weil-pbc-cartesian-square], and forming mates is compatible with pasting
(the triangle identities cancel the adjacent unit–counit pairs). Hence $\Phi$
satisfies the characterizing identity of the outer rectangle and equals its
derived exchange morphism.
