+++
id = "prop-exc-base-change-proper"
kind = "theorem"
title = "Base change for a proper morphism, against an open immersion"
order = 2585
tags = ["latex:proposition"]
uses = ["def-sf-fullcd-used-class", "def-weil-ambient-exceptional-adjoint", "def-weil-pbc-derived-categories", "lem-compact-support-direct-image-triangulated", "lem-exc-closed-support-triangle", "lem-exc-open-fully-faithful", "prop-exc-ambient-dual-base-change", "thm-sf-ambient-adjoint-class"]
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
[def-sf-fullcd-used-class], for finite-type schemes over
$k=\overline{\mathbf F}_q$ and $A=A_{E,n}$, the ambient datum is not
needed: there $Rf^{\times}$, $Rf'^{\times}$ and $Rf_Z^{\times}$ are the
right adjoints relative to the bounded-below objects of étale origin of
[thm-sf-ambient-adjoint-class], and the argument below is object-wise, so
the comparison is an isomorphism for every bounded-below $K$ of étale
origin without hypothesis. The unrestricted ambient datum is false in
general and is retained only for the complexes outside that class,
[rem-sf-class-adjoint-residue].
