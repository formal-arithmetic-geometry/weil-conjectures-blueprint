+++
id = "lemma-nagata-scheme-theoretic-closure-minimal"
kind = "lemma"
title = "Minimality of the scheme-theoretic closure"
order = 154
lean = ["AlgebraicGeometry.IsClosedImmersion.lift"]
uses = ["def-nagata-scheme-theoretic-closure", "lemma-nagata-scheme-image-universal"]
+++
The scheme-theoretic closure is the smallest closed subscheme of $Y$
through which $a$ factors: it factors through every such closed subscheme,
and the comparison is unique over $Y$.

## Proof

This is [lemma-nagata-scheme-image-universal] applied to the immersion
$a$, together with
[def-nagata-scheme-theoretic-closure].
