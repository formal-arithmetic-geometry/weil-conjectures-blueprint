+++
id = "lemma-internal-adjunction-two-exchange-formulas--1"
kind = "lemma"
title = "Internal adjunction and two exchange formulas (1)"
name_showing = false
order = 830001
aliases = ["bp-r248-1"]
lean = ["AlgebraicGeometry.Etale.derivedHomRightDerivedLowerShriekIsoOfFinite", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierExchange"]
uses = ["proposition-composition-open-restriction-compactifications-f", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--15", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $f:X\to Y$ be a morphism, $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and
$L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. The map
(10.1) and the two maps derived from it
and defined above are isomorphisms

$$
\begin{aligned}
\cHom_Y(Rf_!K,L)&\simeq
Rf_*\cHom_X(K,f^!L),
\end{aligned}
\tag{10.2}
$$
