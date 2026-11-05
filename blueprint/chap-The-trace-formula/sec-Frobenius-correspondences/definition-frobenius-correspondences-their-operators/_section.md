+++
id = "definition-frobenius-correspondences-their-operators"
kind = "definition"
title = "Frobenius correspondences and their operators"
order = 952
lean = ["AlgebraicGeometry.ProEtale.stalkFrobenius", "AlgebraicGeometry.ProEtale.weilDatumIterate"]
uses = ["lemma-stability"]
+++
Let $X_0/k_0$ be separated and of finite type, and put
$X=X_0\times_{k_0}k$. Denote by $\Phi_X:X\to X$ the base change
of the $q$-power scheme Frobenius of $X_0$. It is a finite
$k$-morphism and a universal homeomorphism. A *Frobenius
correspondence* on $K$ is a morphism, not necessarily
invertible,

$$
\psi:\Phi_X^*K\longrightarrow K,
\qquad K\in D^b_{\mathrm{ctf}}(X,A).
$$

Its iterates are the morphisms

$$
\psi_m=\psi\circ\Phi_X^*\psi\circ\cdots\circ
(\Phi_X^{m-1})^*\psi:(\Phi_X^m)^*K\longrightarrow K.
$$

Let $c_m=(\operatorname{id}_X,\Phi_X^m):X\to X\times_sX$ be the graph
of $\Phi_X^m$. Since its first leg is the identity, $\psi_m$ is a
cohomological correspondence on $(X,K)$ for $c_m$. Its operator on
cohomology with compact support
(Definition [definition-action-correspondence]) is the endomorphism

$$
T_{c_m}(\psi_m)
=R\Gamma_c(X,\psi_m)\circ(\Phi_X^m)^*,
$$

where $(\Phi_X^m)^*:R\Gamma_c(X,K)\to R\Gamma_c(X,(\Phi_X^m)^*K)$ is the
pullback map induced by the unit of $(\Phi_X^m)^*\dashv R(\Phi_X^m)_*$.
For $x\in X_0(\mathbf F_{q^m})$ let $\bar x:s\to X$ be the
associated fixed point. The stalk of $\psi_m$ at $\bar x$ is an endomorphism
$\psi_{m,\bar x}:K_{\bar x}\to K_{\bar x}$.
