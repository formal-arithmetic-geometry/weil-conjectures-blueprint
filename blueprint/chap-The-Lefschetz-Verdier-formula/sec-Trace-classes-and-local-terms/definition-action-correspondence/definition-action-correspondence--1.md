+++
id = "definition-action-correspondence--1"
kind = "definition"
title = "Action of a correspondence on cohomology (1)"
name_showing = false
order = 922001
aliases = ["bp-r279-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.globalOperator"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-construction-independence-rf-shriek--9", "proposition-composition-base-change-rf-shriek--7", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-correspondence--2", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $u$ be a cohomological correspondence on $(X,K)$ for a
correspondence $c$ with $c_2$ proper. The endomorphism $T_c(u)$ of
$R\Gamma_c(X,K)$ is the composite

$$
\begin{aligned}
T_c(u):R\Gamma_c(X,K)&\xrightarrow{\eta_{c_2}}
R\Gamma_c(C,c_2^*K)\xrightarrow{u}R\Gamma_c(C,c_1^!K)\\
&\simeq R\Gamma_c(X,Rc_{1!}c_1^!K)
\xrightarrow{\varepsilon_{c_1}}R\Gamma_c(X,K).
\end{aligned}
$$
