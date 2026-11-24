+++
id = "proposition-six-operations-change-coefficients"
kind = "proposition"
title = "The six operations and change of coefficients"
order = 646
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension"]
+++
Let $\Lambda\to\Lambda'$ be one of the maps of coefficient rings listed
above. Extension of scalars sends [$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves) into
[$D^b_{\mathrm{ctf}}(X,\Lambda')$](@definition-constructible-sheaves). For morphisms $f:X\to Y$ of schemes of finite type
over $k$ (separated in the case of [$Rf_!$](@proposition-construction-independence-rf-shriek) and [$f^!$](@theorem-existence-exceptional-inverse-image)), the
change-of-coefficients maps of
Definition [definition-change-of-coefficients-maps] and
(7.1) for $f^*$, $Rf_*$, [$Rf_!$](@proposition-construction-independence-rf-shriek),
[$f^!$](@theorem-existence-exceptional-inverse-image), $\otimes^{\mathbf L}$ and $\cHom$ are isomorphisms on objects of
[$D^b_{\mathrm{ctf}}(-,\Lambda)$](@definition-constructible-sheaves). For a composite $\Lambda\to\Lambda'\to\Lambda''$ of two
such maps, each of these isomorphisms is the composite of the isomorphisms
for $\Lambda\to\Lambda'$ and $\Lambda'\to\Lambda''$. These isomorphisms
are compatible with the composition isomorphisms $(gf)^*\simeq f^*g^*$,
$R(gf)_*\simeq Rg_*Rf_*$, $\href{@proposition-construction-independence-rf-shriek}{R(gf)_!}\simeq \href{@proposition-construction-independence-rf-shriek}{Rg_!}\href{@proposition-construction-independence-rf-shriek}{Rf_!}$ and
$\href{@theorem-existence-exceptional-inverse-image}{(gf)^!}\simeq \href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{g^!}$ for composable morphisms $f$ and $g$. Under these
isomorphisms, the extensions of scalars of the units and counits of the
adjunctions $f^*\dashv Rf_*$, $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ and
$-\otimes^{\mathbf L}K\dashv\cHom(K,-)$ (the last counit being evaluation)
over $\Lambda$ are the corresponding units and counits over $\Lambda'$.
