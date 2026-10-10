+++
kind  = "proof"
of    = "lemma-nagata-one-valuation-avoids-boundary"
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-valuation-factor-closed"]
+++
Otherwise the closed point would map into $\overline Z_{1,2}$ under $g_1$
and into $\overline Z_{2,1}$ under $g_2$. By
[lemma-nagata-valuation-pair-factors-comparison], the pair factors
through $X_{12}$, and its closed point then lies in
$X_{12}\cap(\overline Z_{1,2}\times_S\overline Z_{2,1})$, contradicting
the assumed key boundary disjointness. If the closed point avoids
one of the two boundaries, its inverse image of the corresponding open
complement is an open subset of $\operatorname{Spec}(A)$ containing the
closed point. By
[lemma-nagata-valuation-open-closed-point] this open is all of
$\operatorname{Spec}(A)$. The associated $g_i$ therefore factors
through $X_i\setminus\overline Z_{i,j}$.
