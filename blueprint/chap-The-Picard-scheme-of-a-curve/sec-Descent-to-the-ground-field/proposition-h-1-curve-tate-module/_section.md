+++
id = "proposition-h-1-curve-tate-module"
kind = "proposition"
title = "$H^1$ of a curve and the Tate module of its Jacobian"
order = 1568
lean = ["AlgebraicGeometry.JacobianTorsionDatum.exists_kummerEquiv_eq", "AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv", "AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv_map_rootsOfUnityPowMap", "AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv_restrictMuH"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "proposition-kummer-duality-integral-tate-module", "lemma-schematic-closure-uniqueness", "definition-abelian-variety", "lemma-abelian-variety-commutative", "definition-relative-picard-functor"]
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
on the torsion points. Consequently

$$
\varprojlim_n H^1(C,\mathbf Z/\ell^n(1))\simeq T_\ell J_0
$$

as $\mathbf Z_\ell$-modules with Galois action.
