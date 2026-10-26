+++
id = "lem-weil-pbc-w-local-partition"
kind = "lemma"
title = "Clopen partitions on a w-local affine scheme"
order = 903
lean = ["WLocalSpace.spectralSpace_closedPoints", "WLocalSpace.t1Space_closedPoints", "WLocalSpace.CompactSpace_closedPoints", "SpectralSpace.totallySeparatedSpace", "WLocalSpace.isHomeomorph_connectedComponents_closedPoints"]
uses = ["def-weil-pbc-w-local", "det-pe-wlocal-components"]
+++
For a w-local [def-weil-pbc-w-local] affine scheme $X$, its closed point set $X^c$ is a
profinite space, and restriction identifies clopen partitions of $X$ with
clopen partitions of $X^c$. An open subset containing a part of $X^c$
contains the corresponding components of $X$.
