+++
id = "definition-trace-class-local-terms--1"
kind = "definition"
title = "Trace class and local terms (1)"
name_showing = false
order = 917001
aliases = ["bp-r277-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.mate", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--15", "proposition-six-operations-dctf--16", "definition-correspondence--2", "definition-correspondence--3", "lemma-external-duality-trace-morphism--2", "definition-trace-morphism--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $u:c_2^*K\to c_1^!K$ be a cohomological correspondence on $(X,K)$.
By adjunction, $u$ is a section $A_C\to\mathcal H_c(K)$.
Its composite with the trace morphism of
Definition [definition-trace-morphism], transposed by $i_c^*\dashv Ri_{c*}$,
is the *trace class*

$$
\operatorname{Tr}_c(u):A_{\Fix(c)}\longrightarrow\omega_{\Fix(c)}.
$$
