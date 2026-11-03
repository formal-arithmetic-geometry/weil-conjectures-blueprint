+++
id = "lemma-weil-pbc-curve-normalization-constant"
kind = "lemma"
title = "Normalization and smooth constant case"
lean = ["AlgebraicGeometry.IsCurve.reducedConstantLowerShriekAssertions", "AlgebraicGeometry.IsCurve.Assertions.lowerShriek_constantModSheaf_of_finite_coefficients"]
order = 1610
uses = ["lemma-weil-pbc-curve-dense-open-reduction", "lemma-weil-pbc-normalization-exact-sequence", "lemma-weil-pbc-smooth-curve-artin-schreier", "lemma-weil-pbc-smooth-curve-kummer-localization"]
+++
Let $X$ be a reduced separated curve of finite type over an algebraically
closed field $k$, let $j:U\hookrightarrow X$ be an open immersion, and let
$\ell$ be a prime (possibly $\ell=\operatorname{char}k$). Then all applicable
assertions among the eight curve assertions $\mathcal C_1,\dots,\mathcal C_8$
(vanishing, finiteness, invariance under algebraically closed extension of
$k$, and surjectivity of $H^2$ onto opens)
hold for the sheaf $j_!\underline{\mathbf F_\ell}$ on $X$.
