+++
id = "theorem-f-shriek-finite-coefficients"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 593
lean = ["AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedUpperShriek", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.DerivedCategoryFiniteTor.rightDerivedLowerShriekAdjunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "proposition-construction-independence-rf-shriek", "proposition-composition-open-restriction-compactifications-f", "definition-compactification-refinement"]
+++
For every separated morphism $f:X\to Y$ of finite type, the right adjoint
$f^!:\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,A)})\to\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)})$ of
Theorem [theorem-existence-exceptional-inverse-image] maps [$D^b_{\mathrm{ctf}}(Y,A)$](@definition-constructible-sheaves) into [$D^b_{\mathrm{ctf}}(X,A)$](@definition-constructible-sheaves).
Consequently, its adjunction restricts to

$$
\href{@proposition-construction-independence-rf-shriek}{Rf_!}:\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}\ \rightleftarrows\ \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,A)}:\href{@theorem-existence-exceptional-inverse-image}{f^!}.
$$
