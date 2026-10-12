+++
kind  = "proof"
of    = "lem-fin-extension-by-zero"
uses = ["def-constructible-constant", "def-constructible-finite", "def-constructible-finite-locally-constant", "def-constructible-locally-constant", "def-constructible-stratification", "def-kun-separably-closed", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-locally-constant", "lemma-openclosed-vanishing-lowershriek", "prop-constructible-open-closed"]
+++
By [def-weil-pbc-constructible-complexes] $U$ has a finite
partition $U=\bigsqcup_\alpha U_\alpha$ into locally closed
constructible subschemes with $F|_{U_\alpha}$ lisse. The pieces
$U_\alpha$ are locally closed constructible subschemes of $X$ (locally
closed in the open subscheme $U$), and $X$ is the disjoint union of
$X\setminus U$ and the $U_\alpha$. By the stalk description of
[def-weil-pbc-extension-by-zero] the restriction of $j_!F$ to
$U_\alpha$ is the lisse $F|_{U_\alpha}$ and its restriction to
$X\setminus U$ is the zero sheaf, which is lisse; this is the finite
partition with lisse restrictions of
[def-weil-pbc-constructible-complexes].
