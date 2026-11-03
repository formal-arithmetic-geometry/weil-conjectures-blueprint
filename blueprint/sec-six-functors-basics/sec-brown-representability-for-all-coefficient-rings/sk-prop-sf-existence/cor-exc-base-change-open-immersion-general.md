+++
id = "cor-exc-base-change-open-immersion-general"
kind = "theorem"
title = "Base change for an arbitrary morphism, against an open immersion"
order = 2586
tags = ["latex:corollary"]
uses = ["cor-exc-base-change-reduces-to-proper", "def-sf-fullcd-used-class", "def-weil-ambient-exceptional-adjoint", "prop-exc-base-change-proper", "thm-nagata-compactification", "thm-sf-ambient-adjoint-class"]
+++
Let $f:X\to Y$ be separated finite type carrying the ambient exceptional
right adjoint datum of [def-weil-ambient-exceptional-adjoint], and let
$g:Y'\hookrightarrow Y$ be an *open immersion*. Then the
base-change comparison $Lg'^*Rf^{\times}\to Rf'^{\times}Lg^*$ is an
isomorphism. In particular the base-change comparison holds for the
passage from an affine open of the base to the base, which is what an
assembly on affine charts requires. On the blueprint's coefficient class
[def-sf-fullcd-used-class], for finite-type schemes over
$k=\overline{\mathbf F}_q$ and $A=A_{E,n}$, the ambient datum is not
needed: there $Rf^{\times}$ and $Rf'^{\times}$ are the right adjoints
relative to the bounded-below objects of étale origin of
[thm-sf-ambient-adjoint-class], and the comparison at $K$ is an
isomorphism for every bounded-below $K$ of étale origin without
hypothesis. The unrestricted ambient datum is false in general.
