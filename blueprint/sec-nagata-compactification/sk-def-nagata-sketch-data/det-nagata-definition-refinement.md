+++
id = "det-nagata-definition-refinement"
kind = "definition"
title = "Refinement of compactifications"
uses = ["def-nagata-compactification", "def-nagata-dense-compactification"]
+++
Let $f:X\to S$ be a morphism and let
$c=(X\xrightarrow{j}\overline X\xrightarrow{p}S)$ and
$c'=(X\xrightarrow{j'}\overline X'\xrightarrow{p'}S)$ be compactifications of
$f$ in the sense of [def-nagata-compactification], with $j,j'$ quasi-compact
open immersions. A *refinement* $h:c'\to c$ is a morphism of schemes
$h:\overline X'\to\overline X$ such that

1. $p\circ h=p'$ ($h$ is an $S$-morphism);
1. $h\circ j'=j$ ($h$ is compatible with the identifications of $X$ with the
   opens $j'(X)\subseteq\overline X'$ and $j(X)\subseteq\overline X$);
1. $h^{-1}(j(X))=j'(X)$ as open subschemes of $\overline X'$.

By the second condition, $h$ restricts on $j'(X)$ to the isomorphism
$j\circ(j')^{-1}:j'(X)\xrightarrow{\sim}j(X)$, so the third condition says
that $h$ maps the boundary $\overline X'\setminus j'(X)$ into the boundary
$\overline X\setminus j(X)$. Refinements compose: if $h:c'\to c$ and
$h':c''\to c'$ are refinements, then $p\circ h\circ h'=p''$,
$h\circ h'\circ j''=h\circ j'=j$, and
$(h\circ h')^{-1}(j(X))=h'^{-1}(j'(X))=j''(X)$; the identity of
$\overline X$ is a refinement $c\to c$. Compactifications of $f$ with their
refinements thus form a category, and the *dense* compactifications
([def-nagata-dense-compactification]) form a full subcategory.
