+++
kind  = "proof"
of    = "lemma-nagata-closed-immersion-stage-exists"
+++
Cover $Y_\lambda$ by finitely many affine opens and cover the inverse images
in $Z_\lambda$ by finitely many affine opens; this is finite because the
morphism is finitely presented. On one such chart write the map as
$B_\lambda\to C_\lambda$ with $C_\lambda$ finitely presented over
$B_\lambda$. After tensoring with the colimit ring, the map
$B\to C$ is surjective. Choose finitely many algebra generators of
$C_\lambda$ over $B_\lambda$. Their images in $C$ have preimages in $B$;
choose representatives of those preimages at a common later stage. The
finitely many equations expressing each generator as such a preimage hold
at one further common stage by
[lemma-nagata-filtered-colimit-finite-data]. Consequently the chart
map is surjective at that stage and at every later stage, hence a closed
immersion on the chart. Repeat for the finite affine chart list and take a
common upper bound. The chartwise closed immersions agree on overlaps (they
are base changes of the same map), so their images glue to a global closed
immersion. Base change of a finite-presentation morphism to a later stage
preserves finite presentation, and the same finite upper-bound argument
proves the assertion for every $\nu\geq\mu$.
