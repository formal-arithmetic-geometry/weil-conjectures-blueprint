+++
id = "lemma-extending-isomorphism-over-closure-closed--1"
kind = "lemma"
title = "The constructed blow-up is an isomorphism near the closure"
name_showing = false
order = 1452001
aliases = ["bp-r453-1"]
lean = ["AlgebraicGeometry.exists_isIso_strictTransformMap_isoNearClosureBlowup"]
uses = ["definition-admissible-blow-up", "definition-strict-transform"]
+++
Let $T$ be qcqs, let $q:P\to T$ be proper, let $V\subseteq T$ be a
quasi-compact open, and let $F\subseteq V$ be closed in $V$. Let
$N\subseteq T$ be an open containing $F$ such that $q$ is an
isomorphism over $N$.

Let $b:T'\to T$ be the $V$-admissible blow-up
`AlgebraicGeometry.isoNearClosureBlowup`, constructed by separation,
elimination of indeterminacy, and extension of the centre as described
below. If $q':P'\to T'$ is the strict transform of $q$, there is an open
$N'\subseteq T'$ such that

$$
\overline{b^{-1}(F)}\subseteq N',\qquad
q'|_{N'}:(q')^{-1}(N')\xrightarrow{\sim}N'.
$$
