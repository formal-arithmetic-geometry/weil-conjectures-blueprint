+++
id = "thm-sf-relative-trace"
kind = "theorem"
title = "The relative trace, and its transitivity"
order = 2481
uses = ["cor-sf-trace", "def-compact-support-direct-image-detailed", "def-sf-datum", "fix-prop-adjunctions", "prop-compactification-coherence-detailed", "thm-sf-comp-composition"]
+++
In the setting of [def-sf-datum], let $f:X\to Y$ be proper. Then the
counit of $Rf_!\dashv Rf^!$, read through the identification
$Rf_!\cong Rf_*$ of [fix-prop-adjunctions], is a natural transformation

$$
\operatorname{tr}_f:\ Rf_*f^!\longrightarrow\operatorname{id}_Y ,
$$

and:

1. **(i)** *transitivity*: for composable proper $f,g$,
$\operatorname{tr}_{g\circ f}=\operatorname{tr}_g\circ Rg_*\operatorname{tr}_f$, the identifications being the composition law
$R(g\circ f)_!\cong Rg_!Rf_!$ of [thm-sf-comp-composition], [def-compact-support-direct-image-detailed] and
$(g\circ f)^!\cong f^!g^!$;
1. **(ii)** *the projection formula*: composed with
$\operatorname{PF}$ the trace is the pairing of $Rf_*K$ with $L$, i.e. it is
the map that integrates;
1. **(iii)** *the orientation*: for smooth $f$ under an
orientation datum it is the normalized trace of [cor-sf-trace],
compatibly with the orientation of the diagonal.

## Proof

(i) is the pasting of counits: for a pasted adjunction the counit is
the pasted counit by the triangle identities, which are part of
[fix-prop-adjunctions]; substituting the composition law recorded in
[def-compact-support-direct-image-detailed] and the isomorphism
$(g\circ f)^!\cong f^!g^!$ of [def-sf-datum](A4), coherent by
[prop-compactification-coherence-detailed], gives the displayed identity.
(ii) is the definition of $\operatorname{PF}$ read through
$Rf_!\cong Rf_*$. (iii) substitutes the orientation
$Rf^!\cong Lf^*(-)(d)[2d]$ into (ii) and compares with
[cor-sf-trace]; the compatibility with the diagonal is the composition
case of (i).
