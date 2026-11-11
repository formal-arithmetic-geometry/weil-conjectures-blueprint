+++
id = "lemma-schematic-closure-uniqueness--1"
kind = "lemma"
title = "Schematic density in the image"
order = 1409001
aliases = ["bp-r435-1"]
lean = ["AlgebraicGeometry.Scheme.Hom.ker_toImage", "AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.IsImmersion.instIsOpenImmersionToImageOfQuasiCompact"]
+++
Let $i:U\to T$ be a quasi-compact morphism, and write
$U\xrightarrow{j}\overline U\xrightarrow{k}T$ for its factorization through
its scheme-theoretic image $\overline U$. Then

$$
\ker(\mathcal O_{\overline U}\to j_*\mathcal O_U)=0,
$$

so $j$ is scheme-theoretically dominant.

The morphism $k$ is a closed immersion by construction. If $i$ is
an immersion, $j$ is an open immersion, and hence identifies $U$
with a scheme-theoretically dense open subscheme of $\overline U$. These
statements require no quasi-separatedness assumption on $T$.
