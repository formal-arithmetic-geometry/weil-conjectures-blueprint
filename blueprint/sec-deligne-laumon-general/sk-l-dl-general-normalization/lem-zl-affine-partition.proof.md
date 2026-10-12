+++
kind = "proof"
of = "lem-zl-affine-partition"
uses = ["def-weil-pbc-scheme-conventions"]
+++
Choose a finite affine open cover $U_1,\ldots,U_m$.
Set $S_i=U_i\setminus\bigcup_{j<i}U_j$, with its reduced
closed subscheme structure inside $U_i$.
Each $S_i$ is affine, since it is closed in an affine scheme,
and is locally closed in the sense of
[def-weil-pbc-scheme-conventions]. Every point belongs
to the piece indexed by the first $U_i$ containing it.
Hence these finitely many pieces are disjoint and cover $X$.
