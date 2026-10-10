+++
kind  = "proof"
of    = "lemma-weil-pbc-chow-embedding-over-x"
+++
We prove the general statement first. The identification
$\mathbf P^n_X=X\times_Y\mathbf P^n_Y$ is the defining fibre-product identity
([lemma-nagata-projective-space-base-change-pullback]), so the condition
$fa=q_Y\circ b$ (with $q_Y:\mathbf P^n_Y\to Y$) gives a unique morphism
$(a,b):T\to\mathbf P^n_X$ over $X$ whose composite with the base change
$\mathbf P^n_X\to\mathbf P^n_Y$ of $f$ is $b$. That base change is
separated, because $f$ is separated and separatedness is stable under base
change. A morphism whose composite with a separated morphism is a closed
immersion is itself a closed immersion
([lem-weil-pbc-closed-immersion-from-composite]); as $b$ is a closed
immersion, so is $(a,b)$.

For the first assertion, $f$ is proper, hence separated, and the Chow
modification ([lemma-weil-pbc-chow-factorization]) satisfies
$f\pi=q_Y\circ\iota_Y$ with $\iota_Y$ a closed immersion. Applying the
general statement with $T=X'$, $a=\pi$ and $b=\iota_Y$ shows that
$\iota_X=(\pi,\iota_Y)$ is a closed immersion over $X$.
