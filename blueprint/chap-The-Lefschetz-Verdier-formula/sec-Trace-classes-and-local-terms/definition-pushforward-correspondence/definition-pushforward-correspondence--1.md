+++
id = "definition-pushforward-correspondence--1"
kind = "definition"
title = "Pushforward of a correspondence (1)"
name_showing = false
order = 924001
aliases = ["bp-r280-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.coeff", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforward", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforwardCoeff", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforwardCoeffCounit", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforwardCoeffUnit"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-construction-independence-rf-shriek--9", "proposition-composition-base-change-rf-shriek--7", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-correspondence--2", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper morphisms, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ be a correspondence with $c'_ig=fc_i$ for
$i=1,2$. Put $K'=Rf_*K\in D^b_{\mathrm{ctf}}(Y,A)$. For a cohomological
correspondence $u$ on $(X,K)$, the *pushforward*
$u':c_2'^*K'\to c_1'^!K'$ of $u$ is the composite
$u'=\beta\,Rg_*u\,\alpha$, where $\alpha$ is built from the unit and counit
of $(\,)^*\dashv R(\,)_*$,

$$
\alpha:c_2'^*Rf_*K\xrightarrow{\eta_g}
Rg_*c_2^*f^*Rf_*K\xrightarrow{\varepsilon_f}Rg_*c_2^*K,
$$

and $\beta:Rg_*c_1^!K\to c_1'^!Rf_*K$ is built from the counit of
$R(\,)_!\dashv(\,)^!$: it is adjoint to

$$
Rc'_{1!}Rg_*c_1^!K\simeq Rf_*Rc_{1!}c_1^!K
\xrightarrow{Rf_*\varepsilon_{c_1}}Rf_*K.
$$
