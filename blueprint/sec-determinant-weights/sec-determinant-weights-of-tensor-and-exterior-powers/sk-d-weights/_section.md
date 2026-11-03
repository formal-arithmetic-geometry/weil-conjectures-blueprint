+++
id = "sk-d-weights"
kind = "definition"
title = "Determinant weight"
order = 672
lean = ["Representation.RealCharacter", "Representation.detCharacter", "Representation.HasFiniteGeometricDet", "Representation.detWeight", "AlgebraicGeometry.WeilGroup.hasFiniteGeometricDet_and_detWeight_eq"]
uses = ["sk-d-real-weil", "sk-r-real-linear", "sk-p-real-rankone", "sk-cor-wrp-rankone-pure", "sk-d-real-detweights"]
tags = ["sketch"]
+++
The determinant weight of a nonzero Weil representation $Q$ is

$$
\operatorname{dw}_\iota(Q)
=\frac{\lambda_\iota(\det(s\mid Q))}{\dim Q},
$$

and $\operatorname{DW}(V)$ denotes the set of determinant weights of the
simple factors of a Weil representation $V$.

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
