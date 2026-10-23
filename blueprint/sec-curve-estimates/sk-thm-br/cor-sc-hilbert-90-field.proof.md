+++
kind  = "proof"
of    = "cor-sc-hilbert-90-field"
uses  = ["lem-sc-torsor-h1"]
+++
By [lem-sc-torsor-h1], $H^1(\operatorname{Spec}K_{\Et},\mathbf G_m)=
\operatorname{Ext}^1(\mathbf Z,\mathbf G_m)$, and the class of an extension
$0\to\mathbf G_m\to E\xrightarrow{\pi}\mathbf Z\to0$ vanishes as soon as the
global section $1$ of $\mathbf Z$ lifts to $E$ (the fibre $\pi^{-1}(1)$ is the
corresponding torsor, and a torsor with a global section is trivial,
[lem-sc-torsor-h1](a)). So it suffices to prove the surjectivity of
$\Gamma(E)\to\Gamma(Q)$ for every short exact sequence
$0\to\mathbf G_m\to E\xrightarrow{\pi}Q\to0$; we do this by Galois descent.

Let $q\in\Gamma(Q)$. Since $\pi$ is an epimorphism of sheaves, $q$ lifts
étale locally, and every étale covering of $\operatorname{Spec}K$ is refined by
$\operatorname{Spec}L\to\operatorname{Spec}K$ for a finite separable extension
$L/K$. So there is $e\in E(\operatorname{Spec}L)$ with $\pi(e)=q|_L$. Let
$p_1,p_2\colon\operatorname{Spec}(L\otimes_KL)\to\operatorname{Spec}L$ be the
two projections. The difference $p_1^*e-p_2^*e$ maps to $0$ in $Q$, so it is a
section of $\mathbf G_m$, i.e. a unit $c$ of $L\otimes_KL$, and it satisfies
the cocycle identity $c_{13}=c_{12}c_{23}$ in $L\otimes_KL\otimes_KL$.

By Hilbert 90 for the Amitsur complex, $c=p_1^*w\cdot(p_2^*w)^{-1}$ for a
unit $w\in L^\times$: the cocycle $c$ is a descent datum on the one-dimensional
$L$-vector space $L$ along the faithfully flat map $K\to L$, so it descends to
a one-dimensional $K$-vector space, and $w$ comes from a basis vector of it.
Replacing $e$ by $e-w$ (the group law of $E$ written additively, $w$ viewed as
a section of $\mathbf G_m\subseteq E$ over $\operatorname{Spec}L$) gives a lift of $q|_L$ with $p_1^*e=p_2^*e$. Then the
pullbacks of $e$ along any two morphisms from an étale $K$-scheme to
$\operatorname{Spec}L$ agree, so by the sheaf property $e$ descends to a global
section of $E$ lifting $q$.
