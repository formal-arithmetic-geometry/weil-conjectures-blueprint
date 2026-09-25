+++
id = "rem-rs-route-note"
kind = "remark"
title = "Why the curve form needs no class field theory"
order = 2810
uses = ["lem-rs-connectivity-cover", "lem-rs-connectivity-pullback", "lem-wf-no-central-torus", "rem-wf-outer-automorphism-note", "thm-wf-rank-one-finite-geometric-image-curve"]
+++
The final proposition below is assembled from the elementary chain of
the Rosengarten chapter. The reduction to a connected component is the
finite etale cover of [lem-rs-connectivity-cover], over which the
geometric monodromy group is the connected group $H^\circ$ and the
geometric monodromy representation stays geometrically semisimple by
[lem-rs-connectivity-pullback].
The only arithmetic input is the curve theorem
[thm-wf-rank-one-finite-geometric-image-curve], proved in 52 from
constant $H^1$, the ordinary Jacobian, Kummer theory, purity and
Poincare duality. No class field theory or generalized Jacobian is
used. The algebraic-group input is fully elementary:
[lem-wf-no-central-torus] uses the weight-lattice generation, the
finiteness of the set of weights, and the determinant character (with
[lem-wf-inner-correction] and
[lem-wf-disconnected-geometric-centre] for the disconnected case),
and 52's [lem-wf-finite-outer-power] proves elementarily (via
Engel's lemma, Cartan's trace criterion, and the innerness of the
derivations of a semisimple Lie algebra) that a power of the Frobenius
conjugation on a connected semisimple group is inner – the spelling
out of why the general assertion "there are only finitely many outer
automorphisms" is not available (see
[rem-wf-outer-automorphism-note] in 52). The commutator form of
the central-element argument is [rem-wf-commutator-cocycle-note]
in 52.
