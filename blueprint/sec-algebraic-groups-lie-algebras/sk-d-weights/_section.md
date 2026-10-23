+++
id = "sk-d-weights"
kind = "definition"
title = "Determinant weight"
lean = ["Representation.RealCharacter", "Representation.detCharacter", "Representation.HasFiniteGeometricDet", "Representation.detWeight"]
order = 3774
uses = ["sk-i-restriction", "sk-r-linear-library"]
tags = ["sketch"]
+++
We work over $\overline{\mathbf Q}_\ell$, with the embedding $\iota$ and
the weight normalization of [sk-d-real-weights]. Put

$$
\lambda_\iota(a)=2\log_q|\iota(a)|\qquad(a\in\overline{\mathbf Q}_\ell^\times).
$$

This is an additive function on $\overline{\mathbf Q}_\ell^\times$ that
vanishes on roots of unity.

If a nonzero representation $Q$ has finite geometric determinant, its
determinant weight is

$$
\dw_\iota(Q)=\frac{\lambda_\iota(\det(F\mid Q))}{\dim Q}.
$$

Changing the degree-one lift multiplies the determinant by an element of
the finite group $\det\rho(P)$, so the value does not depend on the lift.
For a simple Weil sheaf on a curve it is the weight of the determinant
divided by the rank, as in [sk-d-real-detweights].

*Complement.* More generally, a real weight character is a homomorphism
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
