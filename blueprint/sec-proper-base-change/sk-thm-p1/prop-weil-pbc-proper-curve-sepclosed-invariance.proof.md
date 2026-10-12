+++
kind  = "proof"
of    = "prop-weil-pbc-proper-curve-sepclosed-invariance"
+++
First assume both fields algebraically closed. Apply constructible/primary
reduction. The closed immersion $C_{\mathrm{red}}\to C$ is a universal
homeomorphism, so the explicit site equivalence first replaces $C$ by its
reduction. Then apply dense-open localization, the prime-to-$\ell$ trace
splitting, the
finite-pushforward comparison, and the normalized smooth constant calculation
in that order. Every step commutes with field extension, giving the result.
For separably closed $k\subseteq k'$, apply Lemma
[lemma-weil-pbc-curve-separably-closed-passage] to the algebraically
closed result just proved. Its commutative rectangle identifies the
resulting isomorphism with the specified restriction map.

Pass to compatible algebraic closures: the isomorphism of
[prop-weil-pbc-algebraically-closed-extension] holds for the two algebraically
closed extensions, and the two purely inseparable extensions identify the
sites by invariance under universal homeomorphisms, so the separably closed
case is obtained by composing the isomorphisms.
