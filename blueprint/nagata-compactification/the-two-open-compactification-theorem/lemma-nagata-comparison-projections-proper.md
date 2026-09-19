+++
id = "lemma-nagata-comparison-projections-proper"
kind = "lemma"
title = "Properness of the comparison projections"
order = 436
lean = ["AlgebraicGeometry.TwoOpenSide.isProper_comparisonFst"]
uses = ["def-nagata-two-open-comparison-space", "lemma-nagata-prepared-boundaries", "lemma-nagata-scheme-image-universal"]
+++
Both projections $p_i\colon X_{12}\to X_i$ are proper.

## Proof

Apply [lemma-nagata-scheme-image-universal] to
$V_{12}\to X_1\times_SX_2$. It gives the canonical closed immersion
$\iota_{12}\colon X_{12}\hookrightarrow X_1\times_SX_2$ occurring in
[def-nagata-two-open-comparison-space]. For
$\{i,j\}=\{1,2\}$, the morphism $X_j\to S$ is proper by
[lemma-nagata-prepared-boundaries]; hence the projection
$\pi_i\colon X_1\times_SX_2\to X_i$ is its proper base change. The
equality $p_i=\pi_i\circ\iota_{12}$ expresses $p_i$ as a composite of
proper morphisms, so $p_i$ is proper.
