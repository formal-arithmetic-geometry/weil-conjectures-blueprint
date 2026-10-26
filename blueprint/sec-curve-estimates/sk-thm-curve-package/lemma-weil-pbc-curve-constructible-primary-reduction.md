+++
id = "lemma-weil-pbc-curve-constructible-primary-reduction"
kind = "lemma"
title = "Constructible and primary reduction on curves"
lean = ["AlgebraicGeometry.IsCurve.Assertions.of_forall_isReduced"]
order = 1313
uses = ["def-weil-pbc-eight-curve-assertions", "lemma-weil-pbc-curve-filtered-cohomology", "lemma-weil-pbc-eight-curve-devissage", "lemma-weil-pbc-universal-homeomorphism-coverings", "lemma-weil-pbc-universal-homeomorphism-site-equivalence"]
+++
Let $k$ be an algebraically closed field and let $\Lambda$ be a finite
commutative ring. Suppose that for every reduced curve $X$ over $k$ (separated
of finite type, $\dim X\leq1$), every prime $\ell$ and every constructible
sheaf $G$ of $\mathbf F_\ell$-modules on $X_{\Et}$, the eight assertions
$\mathcal C(X,G)$ of [def-weil-pbc-eight-curve-assertions] hold. Then
$\mathcal C(C,F)$ holds for every curve $C$ over $k$ and every torsion sheaf
$F$ of $\Lambda$-modules on $C_{\Et}$, with cohomology that of the underlying
abelian sheaf.
