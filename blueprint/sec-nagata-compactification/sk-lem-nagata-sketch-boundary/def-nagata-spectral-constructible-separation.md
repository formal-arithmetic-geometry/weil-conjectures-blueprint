+++
id = "def-nagata-spectral-constructible-separation"
kind = "definition"
title = "Constructible separation data in a spectral space"
lean = ["PrespectralSpace.constructibleSeparation"]
order = 348
uses = ["lemma-nagata-spectral-constructible-separation-exists"]
+++
Let $V$ be a quasi-compact topological space whose quasi-compact open
subsets form a basis of the topology (for instance a spectral space), and let
$T,T'\subseteq V$ be disjoint closed subsets.
Select quasi-compact opens $(W,W')$ from
[lemma-nagata-spectral-constructible-separation-exists] and define

$$
T_c=V\setminus W,
\qquad
T'_c=V\setminus W'.
$$
