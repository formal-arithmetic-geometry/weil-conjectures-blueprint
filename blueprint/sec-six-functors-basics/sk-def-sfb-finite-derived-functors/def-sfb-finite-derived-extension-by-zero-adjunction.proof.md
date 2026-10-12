+++
kind  = "proof"
of    = "def-sfb-finite-derived-extension-by-zero-adjunction"
uses = ["def-sfb-finite-derived-pullback-iso"]
+++
The derived adjunction of [sk-def-sfb-derived-categories] gives $L(j_!)\dashv R(j^*)$, with
$L(j_!)$ computed on K-flat and $R(j^*)$ on K-injective resolutions. As both functors are
exact, $L(j_!)\cong D(j_!)$ and $R(j^*)\cong D(j^*)$ (the argument of
[def-sfb-finite-derived-pullback-iso]). Transporting the adjunction along these
isomorphisms gives $D(j_!)\dashv D(j^*)$.
