+++
id = "prop-nagata-closed-subscheme-compactifiable"
kind = "theorem"
title = "The closed-subscheme construction is a compactification"
order = 86
lean = ["AlgebraicGeometry.HasCompactification.of_isClosedImmersion"]
tags = ["latex:proposition"]
uses = ["def-nagata-closed-subscheme-compactification", "def-nagata-compactifiable", "def-nagata-compactification", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-scheme-image-restrict-open"]
+++
Let $i\colon X\hookrightarrow X'$ be a closed immersion over $S$ such that
$X'\to S$ is quasi-compact and compactifiable. Then $X\to S$ is
compactifiable: for every compactification $C'$ of $X'\to S$, the
constructed factorization $\mathsf{Closed}(i,C')$ is a compactification
of $X\to S$.
