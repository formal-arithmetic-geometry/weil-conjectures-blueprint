+++
kind = "proof"
of = "lemma-triviality-fibres"
order = 1476
uses = ["definition-constructible-sheaves", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form"]
+++
The proof uses only that $P_t$ is proper and integral with
$H^0(P_t,\mathcal O_{P_t})=\kappa(t)$, which holds by [Stacks, [0BUG](https://stacks.math.columbia.edu/tag/0BUG)]
because $P$ is proper and geometrically integral.

For (1), a trivial sheaf and its inverse both have the nonzero section
$1$, so only the converse needs an argument. On $\mathbf P^1$, for
instance, $\mathcal O(d)$ and $\mathcal O(-d)$ both have nonzero
sections only when $d=0$, and the general argument is the same. Let $s$ and $s'$ be nonzero
sections of $\mathcal L_t$ and $\mathcal L_t^{-1}$. Since $P_t$ is
integral, the product $ss'$ is a nonzero element of
$H^0(P_t,\mathcal O)=\kappa(t)$, hence a unit. Since $ss'$ would
vanish wherever $s$ does, the section $s$ vanishes nowhere, and it
trivializes $\mathcal L_t$.

For (2), note that by (1) the set in question is the intersection of
the loci where $\dim H^0(P_t,\mathcal L_t)$ and
$\dim H^0(P_t,\mathcal L_t^{-1})$ are positive. These loci are closed
because the functions $t\mapsto\dim H^0(P_t,\mathcal L_t^{\pm1})$ are
upper semicontinuous [Stacks, [0BDN](https://stacks.math.columbia.edu/tag/0BDN)], as $\mathcal L$ is flat over $T$
and $f$ is proper.
