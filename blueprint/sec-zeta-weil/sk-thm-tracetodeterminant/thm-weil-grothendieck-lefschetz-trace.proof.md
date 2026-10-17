+++
kind  = "proof"
of    = "thm-weil-grothendieck-lefschetz-trace"
uses = ["det-thm-tf-uniform-formula-weil", "sk-thm-sfb-qlbar-two-colimit", "sk-prop-scalar-six", "def-weil-local-frobenius-trace", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-cohomology-sheaves", "def-weil-ordinary-compact-cohomology", "def-weil-global-geometric-frobenius", "def-trf-frobenius-operators", "cor-trf-point-counting", "prop-weil-proper-compact-coincidence", "def-weil-point-counts-zeta", "thm-zl-lefschetz-weil-identity"]
+++
*Step 1: the identity.* The local data of the interface are the
local Frobenius operators $F_x^{(n)}$ and the stalk complexes
$K_{\bar x}=L\bar x^*K$ of
[def-weil-local-frobenius-trace], computed with the derived
pullback of [def-weil-derived-pullback-tensor-hom] and traced
alternately over the cohomology sheaves of
[def-weil-derived-cohomology-sheaves]; the
global side is the compact-support cohomology of
[def-weil-ordinary-compact-cohomology] with the geometric-Frobenius
operator of [def-weil-global-geometric-frobenius]. With these
identifications, and the induced Frobenius operators on the geometric
stalks of [def-trf-frobenius-operators], the displayed identity is the
Grothendieck–Lefschetz trace formula [det-thm-tf-uniform-formula-weil] in its
form (2) for $\Lambda=\Qlb$ and $m=n$: the complexes are perfect, so the
alternating sums of traces over cohomology are the traces of
[det-thm-tf-uniform-formula-weil] (1), and all sums over degrees are finite.
That theorem is proved in the trace-formula chapter from the finite-ring
trace formula, the Lefschetz–Verdier comparison on the projective line and
the local-term computations. The properness hypothesis in the
Lefschetz–Verdier comparison cannot be dropped for an arbitrary
correspondence on a non-proper scheme.

For the $E$-model clause: if $K\cong(K_E)_{\Qlb}$ compatibly with the Weil
structures, the stalks and the compactly supported cohomology of $K$ are
obtained from those of $K_E$ by the flat extension of scalars, compatibly
with the Frobenius operators ([sk-prop-scalar-six]), and traces commute
with extension of scalars; such a model exists by
[sk-thm-sfb-qlbar-two-colimit] (3), and the Weil structure descends to
some finite $E$ by (2) applied with $r=0$, after enlarging $E$.

*Step 2: the point-count specialization.* For
$K=(\Qlb)_Y$ and proper $Y_0$, the
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
