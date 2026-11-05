+++
kind = "proof"
of = "corollary-point-count-estimates"
order = 1395
uses = ["theorem-trace-isomorphism-top-degree", "corollary-cup-product-pairing", "corollary-point-counting-zeta-function", "corollary-purity-cohomology-smooth-proper-variety", "lemma-hankel-rank-rationality", "theorem-weil-conjectures-smooth-proper-schemes", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "corollary-degree-jacobian"]
+++
Since $X_0$ is proper, the point-counting formula of
Corollary [corollary-point-counting-zeta-function] reads

$$
\#X_0(\mathbf F_{q^m})
=\sum_{i=0}^{2d}(-1)^i\operatorname{Tr}(F^m\mid H^i_\ell).
$$

The terms in degrees $0$ and $2d$ are $1$ and $q^{dm}$ by
Theorem [theorem-weil-conjectures-smooth-proper-schemes](3). The
left side of the estimate is therefore the absolute value of the sum of
the remaining terms. In degree $i$, the trace is a sum of $b_i$
eigenvalues of $F^m$, each of complex modulus $q^{mi/2}$ by
Theorem [theorem-weil-conjectures-smooth-proper-schemes](2). Its
absolute value is thus at most $b_iq^{mi/2}$, and the triangle
inequality proves the first bound. For a curve, $b_1=2g$ by the
cohomology calculation of Appendix [chap-Cohomology-of-torsion-sheaves-on-curves].
