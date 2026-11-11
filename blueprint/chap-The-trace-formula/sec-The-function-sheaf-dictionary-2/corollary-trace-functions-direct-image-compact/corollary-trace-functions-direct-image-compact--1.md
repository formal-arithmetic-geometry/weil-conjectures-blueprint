+++
id = "corollary-trace-functions-direct-image-compact--1"
kind = "corollary"
title = "Trace functions and direct image with compact support (1)"
name_showing = false
order = 1025001
aliases = ["bp-r313-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction"]
uses = ["definition-trace-function", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-weil-structure--2", "definition-correspondence--3", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $f_0:X_0\to Y_0$ be a morphism of separated $\mathbf F_q$-schemes
of finite type, with geometric base change $f:X\to Y$, and let
$(K,\phi)$ be a Weil complex on $X$ with $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ for an
admissible $\Lambda$. Give $Rf_!K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$ the Weil
structure induced by $\phi$ (after Definition [definition-weil-structure]).
Then for every $m\geq1$ and $y\in Y_0(\mathbf F_{q^m})$,

$$
t_{Rf_!K,m}(y)=\sum_{\substack{x\in X_0(\mathbf F_{q^m})\\ f_0(x)=y}}
t_{K,m}(x).
$$
