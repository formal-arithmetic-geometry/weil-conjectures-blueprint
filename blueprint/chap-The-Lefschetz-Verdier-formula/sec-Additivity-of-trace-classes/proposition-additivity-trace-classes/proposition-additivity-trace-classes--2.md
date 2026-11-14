+++
id = "proposition-additivity-trace-classes--2"
kind = "proposition"
title = "Additivity of trace classes (2)"
name_showing = false
order = 943004
aliases = ["bp-r287-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_isClosedImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_isPullback", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_ofGraph_eq_add"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-correspondence--2", "definition-correspondence--3", "definition-trace-class-local-terms--1", "definition-pushforward-correspondence--1", "definition-frobenius-correspondences-their-operators--5", "definition-frobenius-correspondences-their-operators--6", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $i:Z\to X$ be a closed immersion with open complement $U$ such
that $c_1^{-1}(Z)\subset c_2^{-1}(Z)$, let $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
$u$ be a cohomological correspondence on $(X,K)$. Then

$$
\operatorname{Tr}_c(u)=\operatorname{Tr}_c(u_U)+\operatorname{Tr}_c(u_Z),
$$

where $u_U$ and $u_Z$ are the graded pieces of the lift of
Lemma [lemma-lift-correspondence-invariant-decomposition], and $u_Z$
is the pushforward along $i$ and $C_Z\to C$ of the correspondence
$u_{|Z}$ on $(Z,i^*K)$ for $c_Z:C_Z=(c_1^{-1}(Z))_{\mathrm{red}}\to
Z\times Z$ (Lemma [lemma-closed-piece-pushforward]).
