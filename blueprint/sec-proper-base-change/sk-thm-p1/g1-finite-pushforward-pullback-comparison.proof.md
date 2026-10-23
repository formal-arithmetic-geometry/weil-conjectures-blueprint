+++
kind = "proof"
of = "g1-finite-pushforward-pullback-comparison"
uses = ["lem-weil-pbc-cohomology-pullback-functorial", "lem-weil-pbc-edge-map-base-change", "lemma-weil-pbc-finite-exchange"]
+++
The finite edge maps for $f$ and for its base change $f'$ are bijective, and finite exchange is an isomorphism, so it induces a bijection on cohomology [lemma-weil-pbc-finite-exchange]. The base change identity for edge maps [lem-weil-pbc-edge-map-base-change] identifies the pullback along $a$ on $H^q(Y,f_*F)$ with the pullback along $b$ on $H^q(X,F)$ through these bijections.

For bijections $l$ and $r$ satisfying $v\circ l=r\circ w$, bijectivity of $w$ is equivalent to that of $v$. Surjectivity is equivalent too: lift through $l$ in one direction and cancel the injective $r$ in the other.

Regarding an abelian sheaf as a sheaf of $\mathbb Z$-modules and forgetting again gives back the original sheaf up to natural isomorphism, compatibly with pullback. Naturality of the cohomology pullback [lem-weil-pbc-cohomology-pullback-functorial] gives commuting squares whose other maps are the cohomology bijections of these isomorphisms; apply the same elementary argument.
