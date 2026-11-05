+++
id = "proposition-composition-base-change-rf-shriek--4"
kind = "proposition"
title = "Base-change isomorphism"
order = 516005
aliases = ["bp-r157-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicIntegers", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekBaseChangeMap"]
uses = ["proposition-construction-independence-rf-shriek", "prose-05-31", "definition-pro-etale-base-change-map", "definition-derived-base-change-map"]
+++
Let $v:Y'\to Y$ and $f:X\to Y$ be $k$-morphisms in the shared context,
and let $u:X'\to X$, $f':X'\to Y'$ form a cartesian square with $f$ and $v$.
For $\Lambda=\Qbarl$, $E$ or $\Oe$, the compact-support base change map is an
isomorphism
$$
\Ex_!:v^*Rf_!\xrightarrow{\sim}Rf'_!u^*
$$
on $\Dbc(X_{\mathrm{pro}\acute{e}t},\Lambda)$. It is formed as in (5.8),
then transported from the pulled-back compactification to the chosen
compactification of $f'$.

For a finite commutative ring $\Lambda$, the étale version holds on the
unbounded category $D(X_{\mathrm{\acute{e}t}},\Lambda)$ for a cartesian square
of arbitrary schemes, assuming that $f$ and $f'$ admit compactifications and
$f'$ is quasi-compact. Here a compactification means an open immersion
followed by a proper morphism, without a quasi-compactness condition on the
open immersion. In this version the pullbacks are written $Lv^*$ and
$Lu^*$, and the conclusion is that the specified map
$Lv^*Rf_!\to Rf'_!Lu^*$ is an isomorphism.
