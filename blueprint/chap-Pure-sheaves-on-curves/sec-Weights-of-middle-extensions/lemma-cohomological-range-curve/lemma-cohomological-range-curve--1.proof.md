+++
kind = "proof"
of = "lemma-cohomological-range-curve--1"
order = 1189002
uses = ["corollary-degreewise-duality-over-fields", "lemma-degree-zero-top-cohomology", "lemma-finite-quasi-finite-direct-images", "proposition-composition-base-change-rf-shriek", "prose-10-20"]
+++
For $r<0$, choose a compactification of $X_0$. Extension by zero is
exact, and the derived direct image of a sheaf has no negative
cohomology. This is
`AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_neg`.

Suppose $r>2$. First let $X_0$ be smooth of relative dimension one
and let $F$ be lisse. By degreewise Poincaré duality
[corollary-degreewise-duality-over-fields], $H^r_c(X,F)$ is dual to
$H^{2-r}(X,F^\vee(1))$, which is zero because $2-r<0$. This is the
lisse vanishing in [lemma-degree-zero-top-cohomology], formalized as
`AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isLisse`.

For a constructible Weil sheaf on $\Aone_{k_0}$, choose a dense open
$U_0$ on which it is lisse. The reduced closed complement $Z_0$ is
finite over $k_0$, so its compactly supported cohomology vanishes
outside degree zero by [lemma-finite-quasi-finite-direct-images].
The open–closed exact sequence of [prose-10-20] gives

$$
H^r_c(U,F|_U)\longrightarrow H^r_c(\Aone_k,F)
\longrightarrow H^r_c(Z,F|_Z).
$$

The outer terms vanish, hence so does the middle one. Lean uses
`AlgebraicGeometry.WeilSheaf.exists_dense_isLisse_upperStar` for the
open and
`AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_openClosed`
for this exact-sequence argument.

Now suppose $X_0$ is affine of dimension at most one. Noether
normalization gives a finite morphism $f:X_0\to\Aone_{k_0}$
(`AlgebraicGeometry.AffineSpace.exists_isFinite_of_ringKrullDim_le_one`).
By exactness for finite direct images and composition of $Rf_!$
([lemma-finite-quasi-finite-direct-images] and
[proposition-composition-base-change-rf-shriek]),

$$
H^r_c(X,F)\simeq H^r_c(\Aone_k,f_*F)=0.
$$

This is
`AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isAffine_of_two_lt`.

Finally, use Noetherian induction on closed subsets of $X_0$.
For a nonempty closed subscheme $T_0$, choose a nonempty affine open
$V_0\subset T_0$. Vanishing holds on $V_0$ by the affine case and
on its reduced closed complement by induction; the same open–closed
exact sequence gives vanishing on $T_0$. The empty case is already
covered by the affine case. Taking $T_0=X_0$ proves the assertion.
The affine smooth case follows because a scheme smooth of relative
dimension one over a field has dimension at most one.
