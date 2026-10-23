+++
kind  = "proof"
of    = "prop-weil-pbc-reduction-to-projective-line"
uses = ["lem-weil-pbc-projective-embedding", "lem-weil-pbc-reduction-projective-space", "lemma-weil-pbc-cancellation", "prop-weil-pbc-composition-stability", "prop-weil-pbc-finite-morphism"]
+++
Let $f:X\to Y$ be proper. By [lemma-weil-pbc-target-locality] it suffices to treat
the restrictions of $f$ over the affine opens of $Y$, which are again proper; so
let $Y$ be affine. [lemma-weil-pbc-chow-factorization] supplies a proper
surjection $\pi:\widetilde X\to X$ and a closed immersion
$i_Y:\widetilde X\hookrightarrow\mathbf P^n_Y$ over $Y$ with $f\pi=q_Yi_Y$, where
$q_Y:\mathbf P^n_Y\to Y$ is the projection. The projections $\mathbf P^n_S\to S$
have torsion base change by [lem-weil-pbc-reduction-projective-space]. Closed
immersions are finite and so have torsion base change by
[prop-weil-pbc-finite-morphism]. Hence $f\pi=q_Y\circ i_Y$ has torsion base
change by [prop-weil-pbc-composition-stability] (1). The morphism
$i_X=(\pi,i_Y):\widetilde X\to\mathbf P^n_X$ is a closed immersion
([lem-weil-pbc-projective-embedding], $f$ being separated) and
$\pi=q_X\circ i_X$, so $\pi$ has torsion base change by the same argument. Since
$\pi$ is surjective, [lemma-weil-pbc-cancellation] (2) applied to $\pi$ and $f$
gives torsion base change for $f$.
