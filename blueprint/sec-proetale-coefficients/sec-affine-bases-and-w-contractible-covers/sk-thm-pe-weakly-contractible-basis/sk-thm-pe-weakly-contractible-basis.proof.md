+++
kind = "proof"
of = "sk-thm-pe-weakly-contractible-basis"
+++
A cover of $U$ splits as a ring map by
Proposition [sk-prop-pe-wc-rings], and a splitting of a finite cover
amounts to a clopen partition of $U$ on whose pieces the lifts can be
glued. Apply Theorem [sk-thm-pe-wc-cover] to each affine chart. For the
splitting assertion, note that by Theorem [sk-thm-pe-indetale-refinement] a
faithfully flat weakly étale $D$-algebra can be refined to a faithfully
flat ind-étale $D$-algebra. By Proposition [sk-prop-pe-wc-rings] this
refinement splits, and hence so does the original map. Now refine a given cover of the
affine $U$ by a finite affine cover $\{V_j\to U\}$. The disjoint union
$\coprod_jV_j$ is a single faithfully flat weakly étale affine cover,
which therefore has a section $s:U\to\coprod_jV_j$. The sets
$s^{-1}(V_j)$ form a finite clopen partition of $U$, and on
$s^{-1}(V_j)$ the inclusion into $U$ factors through $V_j$.

Now let $F\to h_U$ be an epimorphism. Then $\mathrm{id}_U$ lifts after
passing to a covering of $U$. We refine this covering by the clopen
partition just constructed and glue the lifts on its disjoint pieces.
This gives a global lift of $\mathrm{id}_U$, that is, a section. The same argument,
after pulling back an arbitrary epimorphism along a map from $h_U$,
proves projectivity. See [Stacks, Tag 098F](https://stacks.math.columbia.edu/tag/098F), [Stacks, Tag 0990](https://stacks.math.columbia.edu/tag/0990).
