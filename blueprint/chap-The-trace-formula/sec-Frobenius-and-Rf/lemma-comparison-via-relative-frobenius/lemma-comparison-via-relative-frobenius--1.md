+++
id = "lemma-comparison-via-relative-frobenius--1"
kind = "lemma"
title = "Comparison via relative Frobenius (1)"
name_showing = false
order = 1000002
aliases = ["bp-r305-1"]
lean = ["AlgebraicGeometry.isFinite_relativeFrobenius", "AlgebraicGeometry.isUniversalHomeomorphism_relativeFrobenius", "AlgebraicGeometry.isFinite_and_isUniversalHomeomorphism_relativeFrobenius", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusComparison", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusComparison_add", "AlgebraicGeometry.relativeFrobenius_fst", "AlgebraicGeometry.relativeFrobenius_snd"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-six-operations-dctf--5", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
The relative Frobenius $r_m$ is a finite universal homeomorphism,
$p_mr_m=\Phi_X^m$ and $f'_mr_m=f$, and there are natural isomorphisms

$$
\begin{aligned}
\theta_{f,m}:(\Phi_Y^m)^*Rf_!K
&\simeq Rf'_{m!}p_m^*K
\xrightarrow{Rf'_{m!}\eta_{r_m}}
Rf'_{m!}Rr_{m*}r_m^*p_m^*K\\
&\simeq Rf_!(\Phi_X^m)^*K,
\end{aligned}
$$

compatible with iteration in $m$.
