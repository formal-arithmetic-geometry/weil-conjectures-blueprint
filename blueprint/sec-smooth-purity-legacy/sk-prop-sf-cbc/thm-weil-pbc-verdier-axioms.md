+++
id = "thm-weil-pbc-verdier-axioms"
kind = "theorem"
title = "Verdier axioms and stagewise triangulation"
order = 1889
uses = ["def-weil-pbc-common-stage-cones", "def-weil-pbc-finite-stage-pair-category", "prop-weil-pbc-common-stage-calculus", "prop-weil-pbc-cone-independence"]
+++
The shift and distinguished triangles of [def-weil-pbc-common-stage-cones]
satisfy the four Verdier axioms:

1. every morphism has a distinguished cone triangle, the identity triangle
   is distinguished, and distinguishedness is closed under isomorphism;
2. a triangle is distinguished if and only if its signed rotation is
   distinguished;
3. every commutative square between the first arrows of two distinguished
   triangles extends to a morphism of triangles;
4. cone triangles for composable maps can be placed in an octahedral diagram
   whose required faces commute and whose remaining cone triangle is
   distinguished.

Consequently $\mathcal P_T$ is an ordinary triangulated category. Every
finite-stage inclusion $j_E:\mathcal C_E(T)\to\mathcal P_T$ is exact, and
the identifications $j_FT_{F/E}\simeq j_E$ are exact natural isomorphisms.
