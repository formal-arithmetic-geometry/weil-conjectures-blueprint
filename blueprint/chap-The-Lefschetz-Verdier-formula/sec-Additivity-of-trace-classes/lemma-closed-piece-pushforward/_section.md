+++
id = "lemma-closed-piece-pushforward"
kind = "lemma"
title = "The closed piece as a pushforward"
order = 940
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_unit_comp_restrictedClosedPieceCoeff"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-correspondence", "definition-pushforward-correspondence", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
In the situation of
Lemma [lemma-lift-correspondence-invariant-decomposition], put
$M=i^*K\in D^b_{\mathrm{ctf}}(Z,A)$, and let $u_{|Z}$ be the cohomological
correspondence on $(Z,M)$ for $c_Z$ whose exceptional adjoint is
$Rc_{1Z!}c_{2Z}^*M\simeq i^*\Theta K\xrightarrow{i^*\widehat u}M$. Then
$u_Z$ is the pushforward of $u_{|Z}$ along the proper maps $i$ and $i'$
(Definition [definition-pushforward-correspondence]).
