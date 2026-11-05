+++
kind = "proof"
of = "theorem-weights-rf-shriek--1"
order = 1084001
uses = ["theorem-direct-image-mixed-sheaf", "lemma-weights-exact-sequence", "proposition-weights-under-usual-operations", "proposition-construction-independence-rf-shriek"]
+++
For a Weil sheaf $G$ mixed of weights at most $v$, Theorem
[theorem-direct-image-mixed-sheaf] bounds $R^af_!G$ by $v+a$ for
$a\geq0$. The negative cohomology sheaves of $Rf_!G$ vanish, so
$Rf_!G\in D_{\leq v}(Y_0)$.

Lean passes from this sheaf statement to complexes by induction on the
length of a bounded cohomological range. The zero complex gives the base
case. If $b$ is the highest remaining degree, use the truncation triangle

$$
\tau_{<b}K\longrightarrow K\longrightarrow\mathcal H^b(K)[-b]
\longrightarrow(\tau_{<b}K)[1].
$$

The induction hypothesis bounds $Rf_!\tau_{<b}K$ by $w$.
Since $\mathcal H^b(K)$ is mixed of weights at most $w+b$, the sheaf
case and the shift formula of [proposition-weights-under-usual-operations]
bound $Rf_!(\mathcal H^b(K)[-b])$ by $w$. The functor $Rf_!$
preserves distinguished triangles and commutes with shifts. Apply
[lemma-weights-exact-sequence] to the cohomology sequences of the image
triangle to obtain the bound for $Rf_!K$.

These steps are
`AlgebraicGeometry.WeilSheaf.isMixedOfWeightsAtMost_derivedLowerShriek_toComplex`,
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.map_of_forall_toComplex`,
and `AlgebraicGeometry.HasDirectImageWeightBound.isMixedOfWeightsAtMost_derivedLowerShriek`.
