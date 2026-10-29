+++
id = "sk-d-weights"
kind = "definition"
title = "Determinant weight"
lean = ["Representation.RealCharacter", "Representation.detCharacter", "Representation.HasFiniteGeometricDet", "Representation.detWeight", "AlgebraicGeometry.WeilGroup.hasFiniteGeometricDet_and_detWeight_eq"]
order = 4063
uses = ["sk-d-real-weil", "sk-r-real-linear", "sk-p-real-rankone", "sk-cor-wrp-rankone-pure", "sk-d-real-detweights"]
tags = ["sketch"]
+++
We use the embedding $\iota$ and the function
$\lambda_\iota(a)=2\log_q|\iota(a)|$ on
$\overline{\mathbf Q}_\ell^\times$ of [sk-r-real-linear]. It is additive
and vanishes on roots of unity.

The determinant weight of a nonzero Weil representation $Q$ is

$$
\dw_\iota(Q)=\frac{\lambda_\iota(\det(s\mid Q))}{\dim Q},
$$

and $\operatorname{DW}(V)$ denotes the set of determinant weights of the
simple factors of a Weil representation $V$.

Changing the degree-one lift multiplies the determinant by an element of
the finite group $\det\rho(\pi_1(U))$, and hence the value does not
depend on the lift; it is the number $\dw_\iota$ of
[sk-d-real-detweights].

*Complement.* More generally, for a group $W=P\rtimes\langle s\rangle$, a
real weight character is a homomorphism
$\lambda\colon\overline{\mathbf Q}_\ell^\times\to(\mathbf R,+)$, and
$\dw_\lambda(Q)=\lambda(\delta_Q(s))/\dim Q$, where
$\delta_Q(w)=\det(\rho_Q(w))$ is the character of the determinant
representation $\bigwedge^{\dim Q}Q$ and finite geometric determinant
means that $\delta_Q(P)$ is finite. Representations of $W$ carry the
diagonal action on tensor products and the induced action on exterior
powers. For a composition series, constituent weights mean the weights of
its simple quotients; for a chosen simple decomposition
$V=\bigoplus_jV_j$, the rank-counted list repeats $\dw_\lambda(V_j)$ exactly
$\dim V_j$ times.
On the curve $U_0$, every nonzero Weil representation has finite
geometric determinant, and for $\lambda=\lambda_\iota$ the number
$\dw_\lambda$ of an irreducible one is its determinant weight
$\dw_\iota$ of [sk-d-real-detweights].
