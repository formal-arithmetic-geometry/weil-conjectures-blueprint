+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-near-closure"
uses = ["sk-lem-nagata-sketch-boundary", "sk-lem-nagata-sketch-elimination", "sk-lem-nagata-sketch-blowups"]
+++
Inside $V$, separate $F$ from the closed complement of the maximal open on
which $q$ is an isomorphism. Since $V$ is spectral, both closed subsets can be
enlarged to disjoint constructible closed subsets. Apply
[sk-lem-nagata-sketch-boundary] so that their closures in $T$ are disjoint.
On the complement $T_0$ of the second closure, the restriction of $q$ is an
isomorphism over an open $V_0$ containing $F$. Apply
[sk-lem-nagata-sketch-elimination] on $T_0$. Its strict transform is both
open and proper over the modification, so it is an isomorphism there after
the initial schematic-density modification. Extend this blow-up from $T_0$ to
$T$, preserving $V$, by the extension part of [sk-lem-nagata-sketch-blowups].
This provides an isomorphism on an open containing the closure of $F$. The
precise argument, including the choice of constructible enlargements, is
Stacks 0F3W.
