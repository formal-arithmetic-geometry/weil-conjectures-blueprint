+++
id = "lem-fin-finite-boundary-reconstruction"
kind = "lemma"
title = "Recovering constructibility at a finite boundary"
order = 1971
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "lem-fin-closed-immersion", "lem-fin-extension-by-zero", "lem-fin-finite-reflects-derived", "lem-fin-proper-bounded-constructible", "lemma-weil-pbc-geometric-stalk-conservative", "prop-constructible-derived-subcategory", "sbc-def-coefficient-conventions", "thm-constructible-serre"]
+++
Let $b:Y\to S$ be proper
between finite-type schemes, with the finite coefficients of
[sbc-def-coefficient-conventions].
Let $a:G\hookrightarrow Y$ be open, with closed complement
$i:Z\hookrightarrow Y$, and assume $bi:Z\to S$ is finite.
For $K\in\hyperref[def-weil-pbc-derived-categories]{D^+(Y,\Lambda)}$,
suppose $a^*K$ and the direct image
$Rb_*K$ belong to their respective
bounded constructible categories.
Then $K\in D^b_c(Y,\Lambda)$.
