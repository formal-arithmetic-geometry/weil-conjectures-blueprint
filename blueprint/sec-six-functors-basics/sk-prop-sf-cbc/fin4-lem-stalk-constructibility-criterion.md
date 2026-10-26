+++
id = "fin4-lem-stalk-constructibility-criterion"
kind = "lemma"
title = "Constructibility from the cardinalities of finite stalks"
lean = ["AlgebraicGeometry.Scheme.isConstructibleSheaf_iff_isConstructible_card"]
order = 2698
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-flat-lfp-open", "lem-weil-pbc-noetherian-finite-components", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $X$ be a Noetherian
scheme and let $F$ be an
abelian etale sheaf on $X$
with finite geometric stalks.
For $n\geq1$ put $C_n=\{x\in X:|F_{\bar x}|=n\}$.
Then $F$ is constructible
if and only if every $C_n$ is a constructible subset of $X$.
For an abelian sheaf, constructibility here means a finite locally
closed partition with finite locally constant restrictions.
