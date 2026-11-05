+++
id = "lemma-scheme-frobenius-geometric-frobenius--3"
kind = "lemma"
title = "Comparing the global operators for a Weil object"
name_showing = false
order = 953003
aliases = ["bp-r290-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.globalOperator_eq_correspondenceGlobalOperator", "AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.globalOperator_eq_frobeniusCompactOperator"]
uses = ["definition-weil-structure", "definition-frobenius-operator", "definition-frobenius-correspondences-their-operators", "definition-action-correspondence"]
+++
Lean bypasses the comparison with semilinear geometric Frobenius and compares
operators for the same endomorphism $\Phi$.

Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime, and let
$X/k$ be separated and of finite type. Let $\Phi:X\to X$ be a $k$-endomorphism
and let $(K,\phi)$ be a Weil object for $\Phi$, with
$K\in\Dbc(X,\Qbarl)$ in the condensed coefficient model. Fix $m\geq0$,
put $\Phi_m=\Phi^m$, and assume that $\Phi_m$ is finite and a universal
homeomorphism. Let $F^W_{c,m}(K,\phi)$ be the compactly supported Frobenius
of the iterated Weil object $(K,\phi_m)$ for $\Phi_m$, acting on
$\RGammac(X,K)$. Then

$$
F^W_{c,m}(K,\phi)=T_{c_m}(\phi_m),
\qquad c_m=(\operatorname{id}_X,\Phi_m).
$$

If $\Phi$ is also proper, regard $\phi$ as a coefficient morphism $\psi$.
Its operator

$$
F_{c,m}(\psi)=\RGammac(X,\psi_m)\circ\Phi_m^\sharp
$$

also equals $F^W_{c,m}(K,\phi)$, where $\Phi_m^\sharp$ is the pullback on
compactly supported cohomology. These are identifications with the operator
of the iterated Weil object; they do not identify it with a power of the
semilinear geometric Frobenius of [definition-frobenius-operator].
