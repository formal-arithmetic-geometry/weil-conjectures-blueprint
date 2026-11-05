+++
id = "lemma-products-composites-u-admissible-blow--2"
kind = "lemma"
title = "Products and composites of $U$-admissible blow-ups (2)"
name_showing = false
order = 1433003
aliases = ["bp-r445-2"]
lean = ["AlgebraicGeometry.IsAdmissible.exists_comp"]
uses = ["definition-admissible-blow-up--1"]
+++
Let $T$ be quasi-compact and quasi-separated, and let $U\subseteq T$ be
an open. Let $\mathcal I\subseteq\mathcal O_T$ be a quasi-coherent ideal
of finite type with $\mathcal I|_U=\mathcal O_U$, and write
$\pi:T_1=\operatorname{Bl}_{\mathcal I}(T)\to T$.
Let $\mathcal J\subseteq\mathcal O_{T_1}$ be a quasi-coherent ideal of
finite type equal to the unit ideal over $\pi^{-1}(U)$, and write
$q:T_2=\operatorname{Bl}_{\mathcal J}(T_1)\to T_1$.
There are a quasi-coherent ideal $\mathcal K\subseteq\mathcal O_T$ of
finite type, with $\mathcal K|_U=\mathcal O_U$, and an isomorphism

$$
e:T_2\xrightarrow{\sim}\operatorname{Bl}_{\mathcal K}(T)
$$

such that $b_{\mathcal K}\circ e=\pi\circ q$, where
$b_{\mathcal K}:\operatorname{Bl}_{\mathcal K}(T)\to T$ is the blow-up morphism.
Thus the composite is again a blow-up with center disjoint from $U$;
the open $U$ need not be quasi-compact.
