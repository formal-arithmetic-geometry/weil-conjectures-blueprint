+++
id = "cor-exc-base-change-reduces-to-proper"
kind = "theorem"
title = "Base change for a general morphism reduces to the proper part"
order = 2309
tags = ["latex:corollary"]
uses = ["def-sf-fullcd-used-class", "def-weil-ambient-exceptional-adjoint", "def-weil-compactifications-refinements", "def-weil-pbc-derived-categories", "def-weil-pbc-inverse-image", "thm-sf-ambient-adjoint-class"]
+++
Let $f:X\to Y$ be separated finite type with a
compactification
$X\xrightarrow{j_0}\overline X\xrightarrow{p}Y$, and let $g:Y'\to Y$
be arbitrary. If the base-change comparison
$L\overline g^*Rp^{\times}\to R(p')^{\times}Lg^*$ is an isomorphism for
the proper morphism $p$, then the base-change comparison
$Lg'^*Rf^{\times}\to Rf'^{\times}Lg^*$ is an isomorphism for $f$.
Consequently the comparison for a general separated finite-type morphism
is reduced to its proper part, the open part being free. Here
$Rf^{\times}$, $Rp^{\times}$ are the ambient right adjoints of
[def-weil-ambient-exceptional-adjoint]. On the blueprint's coefficient
class [def-sf-fullcd-used-class], for finite-type schemes over
$k=\overline{\mathbf F}_q$ and $A=A_{E,n}$, the ambient datum is not
needed: there $Rf^{\times}$ and $Rp^{\times}$ are the right adjoints
relative to the bounded-below objects of étale origin of
[thm-sf-ambient-adjoint-class], and the reduction holds for the
comparisons at every bounded-below object without hypothesis. The
unrestricted ambient datum is false in general.
