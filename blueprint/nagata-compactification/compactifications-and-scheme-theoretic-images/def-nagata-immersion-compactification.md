+++
id = "def-nagata-immersion-compactification"
kind = "definition"
title = "Compactification constructed from an immersion"
order = 156
lean = ["AlgebraicGeometry.Compactification.ofIsImmersion"]
uses = ["def-nagata-compactification", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
Let $g\colon X\to Y$ be a quasi-compact immersion over $S$, with
$Y\to S$ proper. Define $\mathsf C(g)$ to be the factorization

$$
X\xrightarrow{g^{\mathrm{im}}}
\operatorname{SIm}(g)\hookrightarrow Y\longrightarrow S.
$$
