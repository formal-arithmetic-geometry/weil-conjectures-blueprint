+++
id = "definition-trace-morphism--1"
kind = "definition"
title = "Trace morphism (1)"
name_showing = false
order = 914001
aliases = ["bp-r276-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceMap", "AlgebraicGeometry.ProEtale.CondensedRing.evaluationKernel"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--15", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-verdier-dual-evaluation--2", "definition-correspondence--1", "definition-correspondence--2", "definition-correspondence--3", "lemma-external-duality-trace-morphism--2", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
In the setting of Lemma [lemma-external-duality-trace-morphism], let
$e_K:P_X\to R\Delta_{X*}\omega_X$ be adjoint to the evaluation
$\Delta_X^*P_X=K\otimes^{\mathbf L} \mathbb D_XK\to\omega_X$. The
*trace morphism* is the composite

$$
\mathcal H_c(K)\simeq c^!P_X\xrightarrow{c^!e_K}c^!R\Delta_{X*}\omega_X
\xrightarrow{\sim}Ri_{c*}d_c^!\omega_X
\simeq Ri_{c*}\omega_{\Fix(c)}
$$

of the second isomorphism of the lemma, $c^!e_K$, exceptional base
change for the proper map $\Delta_X$, and the composition of
exceptional inverse images $d_c^!a_X^!=a_{\Fix(c)}^!$.
