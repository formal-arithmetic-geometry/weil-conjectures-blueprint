+++
id = "sbc-lem-bc-failure-field"
kind = "lemma"
title = "A failure is detected on the generic fibre"
lean = ["AlgebraicGeometry.Etale.FieldFailure.isAffineHom_a", "AlgebraicGeometry.Etale.nonempty_fieldFailure_of_not_universalBaseChangeProperty", "AlgebraicGeometry.Etale.survivesBaseChange_comp_iff_of_surjective", "AlgebraicGeometry.Etale.survivesBaseChange_of_isLimit", "AlgebraicGeometry.Etale.survivesBaseChange_or_of_isClosedImmersion", "AlgebraicGeometry.Etale.not_survivesBaseChange_of_isEmpty"]
order = 2062
uses = ["sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-bc-injectivity", "sbc-lem-bc-minimal-counterexample", "sbc-lem-higher-direct-image-limit", "sbc-lem-thickening-etale-site"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property] assume for
some $q\geq1$ that $\mathrm{BC}(f,n,q')$ holds universally for all
$q'\leq q-1$, but $\mathrm{BC}(f,n,q)$ does not hold universally. Then there exist a commutative diagram

$$
\begin{array}{ccccc}
X & \longleftarrow & X' & \longleftarrow & Y\\
f\big\downarrow & & \big\downarrow f' & & \big\downarrow e\\
S & \longleftarrow & S' & \longleftarrow & \operatorname{Spec}K
\end{array}
$$

where $X'=X\times_SS'$, $Y=X'\times_{S'}\operatorname{Spec}K$, $S'$ is
an affine scheme, $K$ is a
field, and $\mathcal F$ is an abelian sheaf on
$\operatorname{Spec}K$ annihilated by $n$ such that

$$
f'^{-1}R^qg_*\mathcal F\longrightarrow R^qh_*e^{-1}\mathcal F
$$

is not an isomorphism. If $S$ is separated, then moreover
$S'\to S$ is an affine morphism.
