+++
id = "lemma-invariant-additive-characters--1"
kind = "lemma"
title = "Integral and rational invariant additive characters"
name_showing = false
order = 1101001
aliases = ["bp-r337-1"]
lean = ["AlgebraicGeometry.WeilGroup.eq_one_of_conj_invariant", "AlgebraicGeometry.WeilGroup.eq_one_of_conj_invariant_of_continuous"]
uses = ["situation-weil"]
+++
Let $U_0/k_0$ be a smooth geometrically connected curve over the finite
field $k_0$, and let $\ell\ne\operatorname{char}(k_0)$ be prime. Put
$U=U_0\times_{k_0}k$ and $W=W(U_0)$, as in Convention [situation-weil].
Identify the geometric subgroup $\ker(\deg:W\to\mathbf Z)$ with
$\pi_1(U)$ compatibly with Frobenius, and let $s\in W$ be the chosen
lift of degree one.

Every continuous additive homomorphism $a:\pi_1(U)\to\mathbf Z_\ell$
satisfying $a(s^{-1}gs)=a(g)$ for all $g\in\pi_1(U)$ is zero.
The same assertion holds for a continuous additive homomorphism
$a:\pi_1(U)\to\mathbf Q_\ell$.
