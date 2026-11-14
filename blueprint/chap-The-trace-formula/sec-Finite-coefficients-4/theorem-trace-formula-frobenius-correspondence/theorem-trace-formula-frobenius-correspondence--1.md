+++
id = "theorem-trace-formula-frobenius-correspondence--1"
kind = "theorem"
title = "Trace formula for a Frobenius correspondence (1)"
name_showing = false
order = 1007001
aliases = ["bp-r307-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.trace_frobeniusCompactOperator_eq_sum"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "definition-categorical-trace--2", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--4", "definition-frobenius-correspondences-their-operators--5", "definition-frobenius-correspondences-their-operators--6", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, put
$X=X_0\times_{\mathbf F_q}k$, let $A$ be any finite commutative
$\ell$-primary ring and $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
$\psi:\Phi_X^*K\to K$ be any Frobenius correspondence on $K$. For every
$m\geq1$, in $A$,

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K))
=\sum_{x\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x}).
$$
