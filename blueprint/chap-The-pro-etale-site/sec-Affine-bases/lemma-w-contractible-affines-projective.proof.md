+++
kind = "proof"
of = "lemma-w-contractible-affines-projective"
order = 70
+++
To see that covers of $U$ split, note that by
Theorem [theorem-pro-etale-refinements-weakly-etale] a
faithfully flat weakly étale $D$-algebra can be refined to a faithfully
flat ind-étale $D$-algebra. This
refinement splits by Proposition [proposition-splitting-ind-etale-covers], and hence so does the original map. Given a cover of the
affine $U$, we refine it by a finite affine cover $\{V_j\to U\}$. The disjoint union
$\coprod_jV_j$ is a single faithfully flat weakly étale affine cover,
which therefore has a section $s:U\to\coprod_jV_j$. The sets
$s^{-1}(V_j)$ form a finite clopen partition of $U$, and on
$s^{-1}(V_j)$ the inclusion into $U$ factors through $V_j$.

If $F\to h_U$ is an epimorphism, then by the definition of an
epimorphism of sheaves $\mathrm{id}_U$ lifts after passing to a covering
of $U$. We refine this covering by the clopen partition just
constructed. On each piece $s^{-1}(V_j)$ we have a lift, and since the
pieces are disjoint and cover $U$, the sheaf condition glues these lifts
with no compatibility to check. The result is a global lift of
$\mathrm{id}_U$, that is, a section. The same argument,
after pulling back an arbitrary epimorphism along a map from $h_U$,
proves projectivity. See [Stacks, [098F](https://stacks.math.columbia.edu/tag/098F), [0990](https://stacks.math.columbia.edu/tag/0990)].
