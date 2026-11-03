+++
id = "lem-fin-noetherian-chow-modification"
kind = "lemma"
title = "A projective modification of a proper scheme"
lean = ["AlgebraicGeometry.exists_projective_modification"]
order = 2378
uses = ["cor-chow-lemma-proper", "def-pc-projective-morphism", "def-weil-pbc-scheme-conventions", "thm-chow-lemma"]
+++
Let $S$ be a Noetherian scheme and $f:X\to S$ a proper morphism.
There are a scheme $Y$, a proper surjective morphism $\pi:Y\to X$, a
dense open $U\subset X$ such that $\pi^{-1}(U)\to U$ is an isomorphism, a
finite set $N$ and a closed immersion $e:Y\to\mathbf P^N_S$ with $e$
followed by $\mathbf P^N_S\to S$ equal to $f\circ\pi$. In particular
$Y\to S$ is projective ([def-pc-projective-morphism]).
