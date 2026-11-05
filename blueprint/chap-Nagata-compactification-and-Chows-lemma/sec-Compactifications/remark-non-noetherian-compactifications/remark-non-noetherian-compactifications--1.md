+++
id = "remark-non-noetherian-compactifications--1"
kind = "remark"
title = "Dense refinements without a Noetherian hypothesis"
name_showing = false
order = 1414001
aliases = ["bp-r438-1"]
lean = ["AlgebraicGeometry.Compactification.denseRefinement", "AlgebraicGeometry.Compactification.isDense_denseRefinement"]
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
The pro-étale exactness argument in the preceding remark is bypassed
by Lean's construction of dense refinements.

Let $f:X\to S$ be quasi-compact and let
$X\xrightarrow{j}\overline X\xrightarrow{p}S$ be a compactification.
Write $Z$ for the scheme-theoretic image of $j$, with
$i:Z\hookrightarrow\overline X$ its closed immersion. The factorization

$$
X\xrightarrow{j_Z}Z\xrightarrow{p\circ i}S
$$

is a dense compactification of $f$: $j_Z$ is an open immersion and is
scheme-theoretically dense. This construction does not require $S$ or
$\overline X$ to be Noetherian or quasi-compact and quasi-separated,
nor does it require $\overline X\setminus Z$ to be quasi-compact.

*Proof.* Since $f=p\circ j$ is quasi-compact and $p$ is proper, $j$ is
quasi-compact. Take its scheme-theoretic image $Z$. The image
factorization gives $j=i\circ j_Z$, and $j_Z$ is an open immersion
because $j$ is a quasi-compact immersion. The scheme-theoretic image
facts used in [lemma-schematic-closure-uniqueness] hold here without a
quasi-separatedness hypothesis on $\overline X$.

The morphism $i$ is a closed immersion, so $p\circ i$ is proper.
Together with $f=(p\circ i)\circ j_Z$, this constructs the refined
compactification. Finally, the factor map $j_Z$ to the scheme-theoretic
image is scheme-theoretically dominant. This is precisely the density
condition in [definition-compactification-refinement].
