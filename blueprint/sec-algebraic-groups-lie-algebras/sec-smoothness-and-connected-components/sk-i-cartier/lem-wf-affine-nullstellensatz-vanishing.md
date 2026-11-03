+++
id = "lem-wf-affine-nullstellensatz-vanishing"
kind = "lemma"
title = "Residue fields of closed points and the vanishing principle"
lean = ["eq_zero_of_forall_algHom_apply_eq_zero", "existsUnique_comp_mk\u2090_eq_of_forall_algHom"]
order = 3887
+++
Let $k$ be an algebraically closed field and $A$ a finitely generated
commutative $k$-algebra, $X=\operatorname{Spec}A$.

1. Every closed point $x\in X$, i.e. every maximal ideal
   $\mathfrak m_x\subset A$, has residue field $A/\mathfrak m_x=k$;
   thus closed points are the same as $k$-points, i.e. $k$-algebra
   homomorphisms $A\to k$.
2. (Vanishing principle.) If $A$ is reduced, a function $f\in A$ whose
   value $f(x)\in k$ vanishes at every $k$-point $x$ is zero.
3. Consequently, if $\varphi:X\to Y$ is a regular map of affine
   varieties and $Z\subseteq Y$ is a closed subvariety with
   $\varphi(x)\in Z$ for every $k$-point $x$ of $X$, then $\varphi$
   factors uniquely through $Z$.
