+++
id = "definition-exceptional-base-change-map--1"
kind = "definition"
title = "Exceptional base change map (1)"
name_showing = false
order = 727001
aliases = ["bp-r218-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.upperShriekBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.upperShriekBaseChange"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-construction-independence-rf-shriek--9", "proposition-composition-base-change-rf-shriek--8", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--3", "proposition-six-operations-dctf--4", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
For $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$, the *exceptional base change map*
$g'^*f^!K\to f'^!g^*K$ is the adjoint transpose, for
$Rf'_!\dashv f'^!$, of the composite

$$
Rf'_!g'^*f^!K\xrightarrow{\sim}g^*Rf_!f^!K
\xrightarrow{\ g^*\varepsilon_f(K)\ }g^*K,
$$

whose first arrow is the inverse of the base change isomorphism of
Proposition [proposition-composition-base-change-rf-shriek](2).
