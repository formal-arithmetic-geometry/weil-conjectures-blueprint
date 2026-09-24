+++
id = "thm-a1-affine-curve-upper"
kind = "theorem"
title = "Affine compact-support upper bound"
order = 4297
uses = ["cor-fd-origin-hc1-bound", "def-fd-nonexceptional", "def-weil-open-closed-recollement", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-constant-weil-twist", "lem-a1-affine-hc0", "lem-a1-curve-hc2-bound", "lem-a1-exceptional-constituents", "lem-a1-extension-bounds", "lem-a1-finite-boundary-cohomology", "lem-a1-finite-map-curve", "lem-a1-geometric-constituent-reduction", "lem-a1-reduction-composition", "lem-a1-reduction-lisse-pure", "lem-a1-subquotient-extension-bounds", "lem-a1-unramified-at-infinity", "lem-a1-weight-bound-constant-extension"]
+++
Let $C_0$ be a smooth geometrically connected affine curve and let
$\mathcal F$ be a lisse Weil sheaf that is punctually $\iota$-pure of
weight $w$. Then every
compactly supported cohomology group
$H_c^i(C,\mathcal F)$ has weights at most $w+i$.

## Proof

The bounds in degrees zero and two are
[lem-a1-affine-hc0], [lem-a1-curve-hc2-bound].
There is no cohomology outside degrees zero through two:
compactify the curve and use its dimension-one cohomological range
for the extension by zero.

For degree one choose the finite map of
[lem-a1-finite-map-curve]. By
[lem-a1-reduction-composition], the cohomology to be bounded is
$H_c^1(\mathbf A^1,\mathcal K)$, where
$\mathcal K=g_*j_!\mathcal F$.
On the open
$W_0=\mathbf A^1\setminus(B\cup g(C'_0\setminus C_0))$
the restriction of the transported complex is lisse and pure of weight
$w$, by [lem-a1-reduction-lisse-pure].
For the inclusion $a:W_0\hookrightarrow\mathbf A^1$,
[def-weil-open-closed-recollement] and the finite-boundary
vanishing [lem-a1-finite-boundary-cohomology] give

$$
H_c^1(W,a^*\mathcal K)\twoheadrightarrow
H_c^1(\mathbf A^1,\mathcal K).
$$

It suffices to bound the source.

After a finite constant extension,
[lem-a1-geometric-constituent-reduction] provides a filtration
with geometrically irreducible pure graded pieces of weight $w$.
The long exact sequences and
[lem-a1-extension-bounds], [lem-a1-subquotient-extension-bounds] reduce
the bound to each
such piece $\mathcal N$.
Apply [lem-a1-unramified-at-infinity] to it.
That lemma gives a new affine-line open with a geometrically
irreducible pure sheaf $\mathcal M$, unramified at infinity, and a
surjection from $H_c^1$ of this sheaf onto the group for
$\mathcal N$.

If the geometric restriction of $\mathcal M$ is constant, it has
rank one and is a constant Weil twist as in
[def-wf-constant-weil-twist]; its bound is
[lem-a1-exceptional-constituents].
If it is geometrically an Artin–Schreier sheaf
$\mathcal L_{\psi(ax)}$, extend the constant field to define $a$
and that geometric isomorphism. The quotient rank-one character
is geometrically trivial, hence a constant Weil twist; the same
exceptional-constituent lemma applies.
In every other case the input is Fourier-nonexceptional by
[def-fd-nonexceptional], and all hypotheses of
[cor-fd-origin-hc1-bound] hold.
That corollary directly bounds $H_c^1$ of the extension by zero
by $w+1$.

The successive surjections and filtration long exact sequences
preserve this bound by
[lem-a1-extension-bounds], [lem-a1-subquotient-extension-bounds].
Finally finite constant extensions preserve and reflect weight
bounds, as verified in [lem-a1-weight-bound-constant-extension].
This proves the degree-one assertion over the original field and
completes the proof.
