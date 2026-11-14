+++
id = "definition-exceptional-base-change-map"
kind = "definition"
title = "Exceptional base change map"
order = 727
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperShriekBaseChange"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-affines-form-basis", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
