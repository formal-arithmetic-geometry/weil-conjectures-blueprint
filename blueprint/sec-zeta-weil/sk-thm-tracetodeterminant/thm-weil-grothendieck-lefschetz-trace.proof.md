+++
kind  = "proof"
of    = "thm-weil-grothendieck-lefschetz-trace"
+++
*Step 1: the identity.* The local data of the interface are the
local Frobenius operators $F_x^{(n)}$ and the stalk complexes
$K_{\bar x}=L\bar x^*\operatorname{For}(K_E)$ of
[def-weil-local-frobenius-trace], computed with the derived
pullback of [def-weil-derived-pullback-tensor-hom] and traced
alternately over the cohomology sheaves of
[def-weil-derived-cohomology-sheaves]; the
global side is the compact-support cohomology of
[def-weil-ordinary-compact-cohomology] with the geometric-Frobenius
operator of [def-weil-global-geometric-frobenius]. The identity
is the trace formula of the trace-formula chapter: at the finite coefficient stage
it is [thm-trf-grothendieck-lefschetz-finite-ring] (whose finite
ring, finite field, and trace-class hypotheses are the ones recorded in
the interface), the $E$-valued form is [thm-trf-trace-formula-e],
and the $\Qlb$-form over the common-stage coefficients of
[def-weil-algebraically-closed-coefficients] is
[thm-trf-grothendieck-lefschetz-qbar]; the local terms are the
fixed-point and local-term computations of
[thm-trf-frobenius-fixed-points] and
[thm-trf-frobenius-local-term] through the
[thm-trf-lefschetz-verdier] comparison on the projective line, in the
trace-formula chapter's reduction to curves (affine line, Weil
$!$-pushforward along the relative Frobenius, localization),
with the trace classes of
[def-trf-karoubi-trace] and the independence of
[prop-trf-karoubi-independence]. This step inherits the inputs of
the finite-ring trace formula, the construction of the Verdier local trace
and its compatibility with extension by zero to the projective line, both
of which are proved in the trace-formula chapter.
The properness hypothesis in the Lefschetz–Verdier comparison cannot be
dropped for an arbitrary correspondence on a non-proper scheme.
The displayed identity,
understood after the mapping of the $E$-valued traces along
$E\hookrightarrow\Qlb$, is exactly the one of
[thm-trf-grothendieck-lefschetz-qbar] transcribed to the
interface's notation, and the induced Frobenius operators on the
geometric stalks are those of the local Frobenius construction
[def-trf-frobenius-operators].

*Step 2: the point-count specialization.* For
$K_E=E_Y$, $K=(\Qlb)_Y$, and proper $Y_0$, the
interface's constant-sheaf clause is [cor-trf-point-counting],
whose second form replaces compact-support by ordinary cohomology via
the proper coincidence of [prop-weil-proper-compact-coincidence];
the point-count convention is the one of
[def-weil-point-counts-zeta].

*Step 3: the determinant form.* In the smooth-proper
geometrically connected case the same trace formula is the input of
the trace-to-determinant identity [thm-zl-lefschetz-weil-identity]
of the zeta chapter, which converts the per-iterate point counts into the
determinant factorization of the zeta series.
