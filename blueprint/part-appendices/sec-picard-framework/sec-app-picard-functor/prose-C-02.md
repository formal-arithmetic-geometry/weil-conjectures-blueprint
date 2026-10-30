+++
id = "prose-C-02"
kind = "hidden"
title = "The Picard functor and rigidification"
order = 875
+++
We want a scheme whose points over $T$ are families of invertible sheaves
on $C$ parametrized by $T$, and the obvious candidate
$T\mapsto\operatorname{Pic}(C_T)$ contains too much. For $C=\mathbf P^1_k$
and connected $T$, every invertible sheaf on $\mathbf P^1_T$ is
$\mathcal O(d)\otimes f_T^*\mathcal M$ for a unique $d\in\mathbf Z$ and a
unique $\mathcal M\in\operatorname{Pic}(T)$, so
$\operatorname{Pic}(\mathbf P^1_T)=\mathbf Z\oplus\operatorname{Pic}(T)$,
and the Picard scheme should be the constant scheme $\mathbf Z$. The summand $\operatorname{Pic}(T)$ records only invertible
sheaves on the parameter space. These are trivial Zariski locally on
$T$, whereas a functor represented by a scheme is a Zariski sheaf, so it
cannot contain a summand that vanishes locally without vanishing. We
therefore divide by $f_T^*\operatorname{Pic}(T)$, and sheafify to
obtain a functor that a scheme could represent. In the rigidified form of
Lemma [sk-prop-picard-pic-split], the pullbacks from $T$ are removed
by fixing a trivialization along a section, and this is the description
used to construct the chart of Proposition [sk-thm-picard-f-representable]
and the Picard scheme of Theorem [sk-thm-picard-main].
