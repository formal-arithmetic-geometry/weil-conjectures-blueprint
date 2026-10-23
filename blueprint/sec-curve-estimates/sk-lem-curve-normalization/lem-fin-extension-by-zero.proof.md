+++
kind  = "proof"
of    = "lem-fin-extension-by-zero"
uses = ["lemma-constructible-iso-invariance", "lemma-openclosed-vanishing-lowershriek", "prop-constructible-open-closed", "def-constructible-stratification"]
+++
Let $i:Z\to X$ be the closed immersion of the reduced closed complement of $j(U)$, so that $(j,i)$ is a complementary pair of an open and a closed immersion. Since $j$ is quasi-compact, the open–closed criterion [prop-constructible-open-closed] applies: $j_!F$ is constructible if and only if $j^{-1}j_!F$ and $i^{-1}j_!F$ are. The unit $F\to j^{-1}j_!F$ is an isomorphism, so $j^{-1}j_!F$ is constructible, constructibility being invariant under isomorphism [lemma-constructible-iso-invariance]. The restriction $i^{-1}j_!F$ vanishes because $Z$ is disjoint from the image of $j$ [lemma-openclosed-vanishing-lowershriek], and the zero sheaf is constructible (with the one-stratum stratification of $Z$). Hence $j_!F$ is constructible.
