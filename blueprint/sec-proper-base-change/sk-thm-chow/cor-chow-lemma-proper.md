+++
id = "cor-chow-lemma-proper"
kind = "theorem"
title = "Chow's lemma for proper morphisms"
order = 1062
lean = ["AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpace"]
tags = ["latex:corollary"]
uses = ["def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lem-chow-agree-on-dense-open", "lem-chow-closed-model", "lem-chow-glue", "lem-chow-graph", "lem-chow-preimage", "lem-chow-scheme-theoretic-closure", "lem-chow-segre", "lem-chow-tuple-immersion", "lem-weil-pbc-closed-immersion-products", "lem-weil-pbc-proper-composition", "lem-weil-pbc-proper-immersion-closed", "lem-weil-pbc-proper-to-separated", "lemma-nagata-dense-affine-cover-exists", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-projective-target-local", "lemma-nagata-scheme-image-ideal-qc", "thm-chow-lemma"]
+++
Let $S$ be a noetherian scheme and let $f\colon X\to S$ be a proper morphism.
Then the immersion $i\colon X'\to\mathbf P^N_S$ of [thm-chow-lemma] is a
*closed* immersion. Thus there are a finite set $N$, a proper surjective
morphism $\pi\colon X'\to X$ which is an isomorphism over a dense open
subscheme of $X$, and a closed immersion $i\colon X'\to\mathbf P^N_S$ with
$i$ followed by $\mathbf P^N_S\to S$ equal to $f\circ\pi$. In particular every
proper $S$-scheme is dominated by a projective $S$-scheme through a proper
surjective morphism.
