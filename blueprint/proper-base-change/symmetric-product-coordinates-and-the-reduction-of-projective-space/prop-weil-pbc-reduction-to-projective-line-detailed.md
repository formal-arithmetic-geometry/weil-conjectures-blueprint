+++
id = "prop-weil-pbc-reduction-to-projective-line-detailed"
kind = "theorem"
title = "Reduction to the projective line"
order = 1177
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_of_isProper_of_isBaseChangeIso_projectiveLine"]
uses = ["lem-weil-pbc-target-locality", "thm-weil-pbc-chow", "lem-weil-pbc-projective-embedding", "lem-weil-pbc-reduction-projective-space", "prop-weil-pbc-finite-morphisms", "prop-weil-pbc-composition-stability", "prop-weil-pbc-cancellation", "def-weil-pbc-property"]
+++
Assume that $\mathbf P^1_S\to S$ satisfies $\mathrm{PBC}$ in the sense of
[def-weil-pbc-property] for every scheme $S$. Then every proper morphism of
schemes that is locally of finite presentation satisfies $\mathrm{PBC}$.

## Proof

By [lem-weil-pbc-target-locality] the assertion is local on the target, so we
work over an affine $Y$, where [thm-weil-pbc-chow] supplies $\pi$, $i_Y$, and
the two closed embeddings $i_Y$ and $i_X$ of
[lem-weil-pbc-projective-embedding]. At every use of composition or
cancellation below, first convert all $\mathrm{PBC}$ inputs to $\mathrm{IA}$,
apply the lemma, and convert back. The projective-space projections $\mathbf
P^n_S\to S$ have $\mathrm{PBC}$ by
[lem-weil-pbc-reduction-projective-space]. The Chow map factors as $\pi=q_X\circ
i_X$, where $i_X$ is finite and hence has $\mathrm{PBC}$ by
[prop-weil-pbc-finite-morphisms], and $q_X:\mathbf P^n_X\to X$ has
$\mathrm{PBC}$; composition by [prop-weil-pbc-composition-stability] gives
$\mathrm{PBC}$ for $\pi$. Likewise $f\pi=q_Y\circ i_Y$ has $\mathrm{PBC}$.
Since $\pi$ is proper and surjective, [prop-weil-pbc-cancellation] applied to
$\pi$ and $f$ gives $\mathrm{PBC}$ for $f$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, prop:weil-pbc-property-iff-acyclicity
