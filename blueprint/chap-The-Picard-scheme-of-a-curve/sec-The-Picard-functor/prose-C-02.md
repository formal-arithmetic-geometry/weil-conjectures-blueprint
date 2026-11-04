+++
id = "prose-C-02"
kind = "hidden"
title = "The Picard functor (1)"
order = 1511
+++
We want a scheme whose points over $T$ are families of invertible sheaves
on $C$ parametrized by $T$. The obvious candidate
$T\mapsto\operatorname{Pic}(C_T)$ contains too much. For $C=\mathbf P^1_k$
and connected $T$, every invertible sheaf on $\mathbf P^1_T$ is
$\mathcal O(d)\otimes f_T^*\mathcal M$ for a unique $d\in\mathbf Z$ and a
unique $\mathcal M\in\operatorname{Pic}(T)$. In other words
$\operatorname{Pic}(\mathbf P^1_T)=\mathbf Z\oplus\operatorname{Pic}(T)$,
whereas the Picard scheme should be the constant scheme $\mathbf Z$. In
fact the functor $T\mapsto\operatorname{Pic}(C_T)$ is not even a Zariski
sheaf. The pullback $f_T^*\mathcal M$ of a nontrivial invertible sheaf
$\mathcal M$ on $T$ is trivial locally on $T$ but not globally, so no
scheme represents this functor.

The Picard functor is therefore defined as the sheafification of
$T\mapsto\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)$
(Definition [definition-relative-picard-functor]). When $C$ has a
section, Lemma [lemma-rigidification-along-section] removes the
pullbacks from $T$ in another way, by fixing a trivialization along the
section. We use this rigidified description to construct the chart of
Proposition [proposition-divisors-degree-g-open-chart] and the Picard
scheme of Theorem [theorem-picard-scheme-jacobian-over-separably].
