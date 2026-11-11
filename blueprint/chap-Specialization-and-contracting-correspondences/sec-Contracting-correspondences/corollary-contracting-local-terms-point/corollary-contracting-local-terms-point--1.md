+++
id = "corollary-contracting-local-terms-point--1"
kind = "corollary"
title = "Contracting local terms at a point (1)"
name_showing = false
order = 1715001
aliases = ["bp-r532-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_of_isContractingAt"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-correspondence--2", "definition-correspondence--3", "definition-trace-class-local-terms--1", "definition-trace-class-local-terms--2", "definition-trace-class-local-terms--3", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $y\in X(k)$, and suppose that $c_1^{-1}(y)$ is a single reduced point
$z$, with $c_2(z)=y$. Suppose that $F_0=\{z\}$ is an isolated reduced
component of $\Fix(c)$, open and closed, and that on a neighbourhood of $F_0$
the ideal $I_y$ satisfies

$$
c_2^{-1}(I_y)\mathcal O_C\subset c_1^{-1}(I_y)\mathcal O_C,
\qquad
\bigl(c_2^{-1}(I_y)\mathcal O_C\bigr)^n
\subset\bigl(c_1^{-1}(I_y)\mathcal O_C\bigr)^{n+1}
\quad\text{for some }n\geq1.
$$

Then for every $K\in D^b_{\mathrm{ctf}}(X,A)$ and every morphism
$u:c_2^*K\to c_1^!K$, the local term at $F_0$ is the categorical
trace of the restriction $u_Z$ to $Z=\{y\}$ of $u$ restricted to
that neighbourhood, defined in (E.21).
