+++
kind  = "proof"
of    = "prop-constructible-pullback"
uses = ["def-constructible-finite", "def-constructible-locally-constant", "def-constructible-stratification", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-finite", "lemma-constructible-pullback-locally-constant", "lemma-constructible-pullback-stratification"]
+++
Let $(\iota_k\colon Z_k\to X)_k$ be a stratification of $X$ with all
$\iota_k^*\mathcal F$ finite locally constant, and let
$(\iota'_k\colon Z_k\times_XY\to Y)_k$ be its pullback
([lemma-constructible-pullback-stratification]), with projections
$g_k\colon Z_k\times_XY\to Z_k$. Since $\iota_k\circ g_k=g\circ\iota'_k$
and pullback is functorial up to natural isomorphism,
$\iota_k'^*g^*\mathcal F\cong g_k^*\iota_k^*\mathcal F$, which is finite
locally constant by
[lemma-constructible-pullback-locally-constant], [lemma-constructible-pullback-finite]
and [lemma-constructible-iso-invariance].

If $\mathcal F$ is finite locally constant, then $g^*\mathcal F$ is locally
constant by [lemma-constructible-pullback-locally-constant] and has finite
stalks by [lemma-constructible-pullback-finite], so it is finite locally
constant.
