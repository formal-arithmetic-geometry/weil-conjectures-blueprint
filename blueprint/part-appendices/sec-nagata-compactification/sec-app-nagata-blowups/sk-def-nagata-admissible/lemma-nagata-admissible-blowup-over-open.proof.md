+++
kind  = "proof"
of    = "lemma-nagata-admissible-blowup-over-open"
uses = ["lemma-nagata-affine-blowup-complement", "lemma-nagata-ideal-unit-off-support"]
+++
By [def-nagata-admissible-blowup] the support $V(\mathcal I)$ is disjoint
from $U$, so $U$ is an open subset of $X\setminus V(\mathcal I)$. By
[thm-nagata-global-blowup-complement] the restriction of $\pi$ over
$X\setminus V(\mathcal I)$ is an isomorphism; restricting further over the
open $U$ gives that $\pi^{-1}(U)\to U$ is an isomorphism.
