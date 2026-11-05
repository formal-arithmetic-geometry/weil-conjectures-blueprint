+++
id = "lemma-schematic-closure-uniqueness--1"
kind = "lemma"
title = "Schematic density in the image"
name_showing = false
order = 1406001
aliases = ["bp-r435-1"]
lean = ["AlgebraicGeometry.Scheme.Hom.ker_toImage"]
uses = []
+++
Let $f:X\to T$ be a quasi-compact morphism, and write
$X\xrightarrow{j}Z\xrightarrow{k}T$ for its factorization through
its scheme-theoretic image. Then
$$
\ker(\mathcal O_Z\to j_*\mathcal O_X)=0,
$$
so $j$ is scheme-theoretically dominant.

The morphism $k$ is a closed immersion by construction. If $f$ is
an immersion, $j$ is an open immersion, and hence identifies $X$
with a scheme-theoretically dense open subscheme of $Z$. These
statements require no quasi-separatedness assumption on $T$.
