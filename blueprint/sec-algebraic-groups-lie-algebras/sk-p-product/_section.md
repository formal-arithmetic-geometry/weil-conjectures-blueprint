+++
id = "sk-p-product"
kind = "lemma"
title = "The identity component"
lean = ["AlgebraicGeometry.GeneralLinearGroup.surjective_mulCenterIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.exists_mul_eq_of_containsCommutators", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.surjective_mul_center_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_mem_center_mul_mem_geometricMonodromy_eq"]
order = 3744
uses = ["sk-i-restriction", "sk-p-comparison", "sk-p-geometry", "sk-p-lie"]
tags = ["sketch"]
+++
For a representation $\rho\colon W\to\GL(V)$ set

$$
H=\overline{\rho(P)}^{\mathrm{Zar}},\qquad
G=\overline{\rho(W)}^{\mathrm{Zar}},\qquad F=\rho(s).
$$

These closures are reduced closed algebraic subgroups of $\GL(V)$, since
by density multiplication and inversion preserve them. Conjugation by
$\rho(W)$ preserves $H$, so $H$ is normal in $G$. Moreover, the commutator
morphism of $G$ takes values in $H$, because it does so on the dense
subgroup $\rho(W)$. We write this as $[G,G]\subseteq H$. In particular,
every commutator of elements of $G$ lies in $H$.

If $V$ is a semisimple $W$-representation, then

$$
G^\circ=Z(G^\circ)^\circ H^\circ.
$$

*Complement.* The multiplication morphism
$Z(G^\circ)^\circ\times H^\circ\to G^\circ$ is surjective, and every
$g\in G^\circ(\overline{\mathbf Q}_\ell)$ is a product $g=ch$ with
$c\in Z(G^\circ)^\circ$ and $h\in H^\circ$. More generally, the same holds
over any algebraically closed field $k$ of characteristic zero for closed
subgroup schemes $H\subseteq G$ of $\GL_n$ such that $H$ contains the
commutators of $G$ and $k^n$ is a semisimple representation of
$G^\circ(k)$.
