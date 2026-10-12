+++
id = "prop-exc-base-change-proper"
kind = "theorem"
title = "Base change for a proper morphism, against an open immersion"
order = 2156
tags = ["latex:proposition"]
uses = ["cor-sf-ambient-adjoint-discharge", "def-sf-fullcd-used-class", "def-weil-ambient-exceptional-adjoint", "def-weil-pbc-derived-categories", "lem-compact-support-direct-image-triangulated", "lem-exc-closed-support-triangle", "lem-exc-open-fully-faithful", "prop-exc-ambient-dual-base-change"]
+++
Let $f:X\to Y$ be proper, carrying the ambient exceptional right adjoint
datum of [def-weil-ambient-exceptional-adjoint], let
$g:Y'\hookrightarrow Y$ be an open immersion with closed complement
$i:Z\hookrightarrow Y$, and form the Cartesian squares with
$X'=f^{-1}(Y')$, $g':X'\hookrightarrow X$, $f'=f|_{X'}$ and
$i':f^{-1}(Z)\hookrightarrow X$. Then for every object $K$ the
base-change comparison

$$
\beta:\ Lg'^*Rf^{\times}K\xrightarrow{\ \sim\ }Rf'^{\times}Lg^*K
$$

is an isomorphism. On the blueprint's coefficient class
[def-sf-fullcd-used-class] the ambient datum displayed as the hypothesis
is the theorem [cor-sf-ambient-adjoint-discharge], and the argument below
is object-wise, so on that class the comparison is an isomorphism for every
$K$ of the class without hypothesis; the datum is retained for the complexes
outside it, [rem-sf-class-adjoint-residue].
