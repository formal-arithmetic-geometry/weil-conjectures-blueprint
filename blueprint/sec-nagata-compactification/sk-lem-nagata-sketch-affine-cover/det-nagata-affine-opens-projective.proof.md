+++
kind  = "proof"
of    = "det-nagata-affine-opens-projective"
uses = ["lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-relative-affine-space-open-immersion"]
+++
*Step 1: a quasi-compact immersion.* The standard chart
$\mathbf A^n_S\hookrightarrow\mathbf P^n_S$ is an open immersion
([lemma-nagata-relative-affine-space-open-immersion]), so the composite
$\kappa:U\to\mathbf P^n_S$ is an immersion. Since $U$ is of finite type over
the Noetherian scheme $S$, $U$ is Noetherian, so every morphism out of $U$ is
quasi-compact; in particular $\kappa$ is quasi-compact. The scheme
$\mathbf P^n_S$ is separated over the quasi-separated scheme $S$, hence
quasi-separated.

*Step 2: the closure.* By [lemma-nagata-immersion-open-in-scheme-image] the
scheme-theoretic image $\overline U$ of $\kappa$ is a closed subscheme of
$\mathbf P^n_S$, $\kappa$ factors through a quasi-compact open immersion
$U\to\overline U$, and this open immersion is scheme-theoretically dense.

*Step 3: projectivity.* $\overline U\to S$ is the composite of the closed
immersion $\overline U\hookrightarrow\mathbf P^n_S$ with the structure map,
hence projective. The structure map is proper
([lemma-nagata-projective-space-base-change-proper]) and closed immersions
are proper, so $\overline U\to S$ is proper. The composite
$U\to\overline U\to S$ equals $U\to\mathbf A^n_S\to S$, i.e. the given
morphism, since $\iota$ is an $S$-morphism.
