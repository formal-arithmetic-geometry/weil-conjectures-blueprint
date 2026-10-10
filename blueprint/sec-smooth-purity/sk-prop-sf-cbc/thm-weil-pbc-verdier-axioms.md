+++
id = "thm-weil-pbc-verdier-axioms"
kind = "theorem"
title = "Verdier axioms and stagewise triangulation"
order = 1540
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

## Proof

TR1: every morphism has a cone triangle by
[def-weil-pbc-common-stage-cones]; the identity triangle is the cone
triangle of an identity (cone zero), and distinguishedness is closed under
isomorphism by the definition. TR2: by
[prop-weil-pbc-common-stage-calculus] a distinguished triangle and its
signed rotation may be represented over one common finite field, so the
finite-stage TR2 axiom makes the signed rotation distinguished (the shift in
the signed rotation being the $\sigma$-comparison of the definition). TR3:
given a commutative square between the first arrows of two distinguished
triangles, represent the two triangles over one common finite field (using
the transport isomorphisms of
[def-weil-pbc-finite-stage-pair-category]) and apply the finite-stage TR3
axiom; the resulting vertical arrow transports back to $\mathcal P_T$. TR4:
the same common-stage representation of two composable morphisms, together
with the cone independence of [prop-weil-pbc-cone-independence], and the
finite-stage TR4 axiom produce the octahedral diagram whose remaining cone
triangle is distinguished. Hence $\mathcal P_T$ is an ordinary triangulated
category; $j_E$ is exact because cone triangles of $j_E(f)$ are the
corresponding common-stage cone triangles, and the identifications
$j_FT_{F/E}\simeq j_E$ are exact natural isomorphisms by
[prop-weil-pbc-cone-independence].
