+++
id = "theorem-contracting-correspondences-local-terms--1"
kind = "theorem"
title = "Contracting correspondences and local terms (1)"
name_showing = false
order = 1711001
aliases = ["bp-r531-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.restrict_traceClass_eq_pushforward_of_isContractingAt"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-correspondence--2", "definition-correspondence--3", "definition-trace-class-local-terms--1", "definition-pushforward-correspondence--2", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence, and let
$Z\hookrightarrow X$ have ideal $I$. Let $F_0$ be a connected component
of $\Fix(c)$ that is open and closed and whose image meets $Z$. Choose
an open neighbourhood $W\subset C$ of $F_0$ on which

$$
I_2=c_2^{-1}(I)\mathcal O_W\subset
I_1=c_1^{-1}(I)\mathcal O_W,
\qquad I_2^n\subset I_1^{n+1}\quad\text{for some }n\geq1.
$$

Let $K\in D^b_{\mathrm{ctf}}(X,A)$, let $u:c_2^*K\to c_1^!K$ be a cohomological
correspondence, and let $u_Z$ be the restriction
(E.21) to $Z$ of $u|_W$, for the
correspondence $c|_W$, with $c_Z:C_Z=(W\cap c_1^{-1}Z)_{\mathrm{red}}\to
Z_{\mathrm{red}}\times Z_{\mathrm{red}}$. Then $h_{F_0}$ is an
isomorphism after reduction, and

$$
\operatorname{Tr}_c(u)|_{F_0}
=(h_{F_0})_*\bigl(\operatorname{Tr}_{c_Z}(u_Z)|_{F_{0,Z}}\bigr),
$$

where $(h_{F_0})_*:H^0(F_{0,Z},\omega_{F_{0,Z}})\to H^0(F_0,\omega_{F_0})$
is the induced isomorphism.
