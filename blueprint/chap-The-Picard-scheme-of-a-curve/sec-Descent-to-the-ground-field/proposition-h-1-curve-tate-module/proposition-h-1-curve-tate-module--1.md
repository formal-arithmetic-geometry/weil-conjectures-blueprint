+++
id = "proposition-h-1-curve-tate-module--1"
kind = "proposition"
title = "$H^1$ of a curve and the Tate module of its Jacobian (1)"
name_showing = false
order = 1568001
aliases = ["bp-r489-1"]
lean = ["AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv", "AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv_restrictMuH", "AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv_map_rootsOfUnityPowMap", "AlgebraicGeometry.JacobianTorsionDatum.exists_kummerEquiv_eq"]
uses = ["definition-relative-picard-functor", "lemma-acyclic-resolutions--1", "lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1", "definition-abelian-variety--1", "lemma-abelian-variety-commutative--2", "proposition-integral-tate-module--4", "definition-relative-picard-functor--2", "lemma-cohomology-multiplicative-group--3"]
+++
In the preceding setting, suppose $\ell$ is invertible in $k$.
For every $n\geq1$ there is a canonical
Galois-equivariant isomorphism, with cohomology computed on the
pro-étale site,

$$
H^1(C,\mathbf Z/\ell^n(1))
\simeq J_0[\ell^n](\bar k).
$$

The coefficient map $\mu_{\ell^{n+1}}\to\mu_{\ell^n}$,
$z\mapsto z^\ell$, corresponds to multiplication by $\ell$
on the torsion points.
