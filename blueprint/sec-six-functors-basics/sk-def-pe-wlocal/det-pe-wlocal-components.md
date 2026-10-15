+++
id = "det-pe-wlocal-components"
kind = "lemma"
title = "Components of a w-local space"
uses = ["def-weil-pbc-w-local"]
+++
Let $T$ be a spectral space whose set $T^c$ of closed points is closed.

1. $T^c$, with the subspace topology, is profinite.
2. If every point of $T$ specializes to exactly one closed point, then the map
   $r\colon T\to T^c$ sending a point to its closed specialization is a continuous
   retraction; the connected components of $T$ are the fibres
   $r^{-1}(c)=\{\text{generalizations of }c\}$, $c\in T^c$; and the composite
   $T^c\hookrightarrow T\to\pi_0(T)$ is a homeomorphism; in particular $\pi_0(T)$ is profinite.
3. Conversely, if every connected component of $T$ contains exactly one closed point, then
   every point of $T$ specializes to exactly one closed point. Hence the definition of
   w-local in [sk-def-pe-wlocal] agrees with [def-weil-pbc-w-local].
4. For $T=\operatorname{Spec}R$ w-local and $\mathfrak m\in T^c$, the component of
   $\mathfrak m$ is the image of $\operatorname{Spec}R_{\mathfrak m}\to\operatorname{Spec}R$.
