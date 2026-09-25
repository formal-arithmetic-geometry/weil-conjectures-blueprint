+++
id = "d-real-boundary"
kind = "definition"
title = "Boundary extension and inertia"
order = 2827
uses = ["d-real-setup", "def-wf-constant-weil-twist", "def-wf-weil-group", "lem-wf-weil-group-constant-extension", "lem-wf-weil-group-exact-sequence", "rem-ptr-wf-weil-group-1"]
+++
Let $j:U_0\hookrightarrow C_0$ be a nonempty open in a
curve, with finite complement $S_0$, and let
$\mathcal F$ be lisse Weil on $U_0$.
Write $J=j_*\mathcal F$ for ordinary sheaf direct image, defined by
sections over the inverse image of an etale neighborhood; use this
construction at finite coefficient levels for adic coefficients.
For $s\in S_0$, let $K_s$ be the fraction field of the henselization of
$\mathcal O_{C_0,s}$, and put

$$
I_s=\ker\bigl(\Gal(\overline K_s/K_s)\to
\Gal(\overline{k(s)}/k(s))\bigr).
$$

Henselization is the universal local henselian extension with unchanged
residue field; a henselian ring lifts simple roots of monic polynomials.
If $V_s$ is the local generic stalk, a residue Frobenius lift acts
unambiguously on the invariants $V_s^{I_s}$.

Uses: [def-wf-constant-weil-twist], [d-real-setup], [def-wf-weil-group], [lem-wf-weil-group-constant-extension], [lem-wf-weil-group-exact-sequence], [rem-ptr-wf-weil-group-1]
