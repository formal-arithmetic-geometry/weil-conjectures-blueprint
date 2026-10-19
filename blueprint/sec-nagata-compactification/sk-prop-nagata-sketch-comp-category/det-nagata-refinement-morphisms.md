+++
id = "det-nagata-refinement-morphisms"
kind = "lemma"
title = "Morphisms out of a dense compactification"
lean = ["AlgebraicGeometry.Compactification.refinement_morphisms"]
uses = ["det-nagata-definition-refinement", "def-nagata-dense-compactification"]
+++
Let $f:X\to S$ be a quasi-compact morphism, let
$c'=(X\xrightarrow{j'}\overline X'\xrightarrow{p'}S)$ be a dense
compactification and $c=(X\xrightarrow{j}\overline X\xrightarrow{p}S)$ a
compactification of $f$. Let $h:\overline X'\to\overline X$ be an
$S$-morphism with $h\circ j'=j$. Then:

1. $h$ is proper;
1. $h^{-1}(j(X))=j'(X)$, so $h$ is a refinement $c'\to c$
   ([det-nagata-definition-refinement]);
1. $h$ is the unique $S$-morphism $\overline X'\to\overline X$ with
   $h\circ j'=j$.
