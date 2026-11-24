+++
id = "prose-12-17"
kind = "hidden"
title = "Frobenius and $Rf_!$ (1)"
order = 999
+++
The [trace formula with finite coefficients](@theorem-trace-formula-frobenius-correspondence) is proved by induction on the
number of affine coordinates. We project a closed subscheme of
$\mathbf A^d$ to $\mathbf A^{d-1}$, apply the induction hypothesis to
[$Rf_!K$](@proposition-construction-independence-rf-shriek), and identify each stalk of [$Rf_!K$](@proposition-construction-independence-rf-shriek) at a rational point with
the cohomology of the fibre, a closed subscheme of $\mathbf A^1$ over a
larger finite field. For this, [$Rf_!K$](@proposition-construction-independence-rf-shriek) must carry a [Frobenius
correspondence](@definition-frobenius-correspondences-their-operators) with two properties: its operator on $R\Gamma_c$ is that of
$\psi$, and its stalk maps are the [Frobenius operators](@definition-frobenius-operator) on the cohomology of the
fibres.

The square formed by $f$ and the two Frobenii commutes, but it is
usually not cartesian. Indeed, already for $f:\mathbf A^1\to s$ the Frobenius of $s$ is the identity, so the fibre product is $\mathbf A^1$ itself,
while [$\Phi_{\mathbf A^1}$](@definition-frobenius-correspondences-their-operators) has degree $q$. The difference is
measured by the relative Frobenius. It is a universal homeomorphism, so pullback
along it is an equivalence on étale sheaves, and the comparison map
built from it is an isomorphism.
