+++
id = "det-pe-wlocal-components"
kind = "lemma"
title = "Components of a w-local space"
lean = ["WLocalSpace.spectralSpace_closedPoints", "WLocalSpace.t1Space_closedPoints", "WLocalSpace.CompactSpace_closedPoints", "SpectralSpace.totallySeparatedSpace", "WLocalSpace.isHomeomorph_connectedComponents_closedPoints", "WLocalSpace.closedPoints_eq_of_mk_eq"]
order = 892
uses = ["def-weil-pbc-w-local"]
+++
Let $T$ be a w-local spectral space [def-weil-pbc-w-local], with set $T^c$ of closed
points.

1. $T^c$, with the subspace topology, is spectral, $T_1$ and compact; hence it is
   profinite.
2. The composite $T^c\hookrightarrow T\to\pi_0(T)$ is a homeomorphism; in particular
   $\pi_0(T)$ is profinite, and two closed points lying in the same connected component are
   equal.
3. The connected component of $c\in T^c$ is the set of generalizations of $c$; thus the
   connected components of $T$ are the fibres of the map $T\to T^c$ sending a point to its
   unique closed specialization.
4. For $T=\operatorname{Spec}R$ and $\mathfrak m\in T^c$, the component of $\mathfrak m$
   is the image of $\operatorname{Spec}R_{\mathfrak m}\to\operatorname{Spec}R$.
