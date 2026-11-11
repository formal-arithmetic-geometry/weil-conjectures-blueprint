+++
id = "lemma-extending-isomorphism-over-closure-closed--1"
kind = "lemma"
title = "Isomorphism near the closure after an admissible blow-up"
order = 1455001
aliases = ["bp-r453-1"]
lean = ["AlgebraicGeometry.exists_isIso_strictTransformMap_isoNearClosureBlowup"]
uses = ["definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--2", "definition-admissible-blow-up--1", "lemma-making-open-schematically-dense--1", "definition-strict-transform--1", "lemma-products-composites-u-admissible-blow--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1"]
+++
Let $T$ be qcqs, let $q:P\to T$ be proper, let $V\subseteq T$ be a
quasi-compact open, and let $F\subseteq V$ be closed in $V$. Let
$N\subseteq T$ be an open containing $F$ such that $q$ is an
isomorphism over $N$.

Then there is a $V$-admissible blow-up $b:T'\to T$ with the following
property: if $q':P'\to T'$ is the strict transform of $q$, there is an
open $N'\subseteq T'$ such that

$$
\overline{b^{-1}(F)}\subseteq N',\qquad
q'|_{N'}:(q')^{-1}(N')\xrightarrow{\sim}N'.
$$
