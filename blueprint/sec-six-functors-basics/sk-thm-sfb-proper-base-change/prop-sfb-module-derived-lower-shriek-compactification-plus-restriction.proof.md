+++
kind  = "proof"
of    = "prop-sfb-module-derived-lower-shriek-compactification-plus-restriction"
uses = ["def-sfb-module-open-lower-shriek", "det-def-sfb-derived-categories"]
+++
Treat the two factors separately. The extension by zero $i_!$ is exact
([def-sfb-module-open-lower-shriek]), so it preserves bounded below complexes and
$\iota\circ D^+(i_!)\cong D(i_!)\circ\iota$. The right derived functor on bounded
below derived categories is compatible with the unbounded one,
$\iota\circ R^+g_*\cong Rg_*\circ\iota$, since a bounded below injective resolution is
K-injective and both functors are computed on it
([det-def-sfb-derived-categories]). Pasting the two isomorphisms gives
$\iota\circ R^+g_*\circ D^+(i_!)\cong Rg_*\circ\iota\circ D^+(i_!)\cong
Rg_*\circ D(i_!)\circ\iota$.
