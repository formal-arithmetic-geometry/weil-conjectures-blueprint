+++
kind  = "proof"
of    = "lem-sfb-finite-upper-shriek-bounded-below"
+++
*The étale $f^\times$.* Write $f^\times=D(i^*)\circ Rg^!$ for the chosen compactification
$X\xrightarrow{i}\bar X\xrightarrow{g}Y$. Since $Y$ is quasi-compact, the proper $Rg_*$ has
finite cohomological amplitude: there is $d\ge0$ with $Rg_*(D^{\le0})\subseteq D^{\le d}$. Let
$K\in D^{\ge n}(Y_{\et})$. For $M\in D^{\le n-d-1}(\bar X_{\et})$ we have $Rg_*M\in D^{\le n-1}$,
so by the adjunction of [thm-sfb-finite-proper-pushforward-left-adjoint]
$\Hom(M,Rg^!K)=\Hom(Rg_*M,K)=0$. Hence $Rg^!K\in D^{\ge n-d}$, and the exact $D(i^*)$
preserves this bound.

The bound $d$ cannot be dropped without quasi-compactness. Let $k$ be separably closed with
$\ell\ne\operatorname{char}k$, let $\Lambda=\mathbf Z/\ell$, and let
$f\colon\coprod_{n\ge0}\mathbf P^n_k\to\coprod_{n\ge0}\operatorname{Spec}k$ be the disjoint union
of the structure morphisms. On the $n$-th summand $f^\times\Lambda=\Lambda(n)[2n]$, so $f^\times$
of the bounded below $\Lambda$ is not bounded below.

*The pro-étale $Rf^!$.* $R\nu_{Y,*}$ preserves bounded below objects, $f^\times$ does by the
first part, and $\nu_X^*$ is exact. So $Rf^!L=\nu_X^*(f^\times R\nu_{Y,*}L)$ is bounded below,
and it is of étale origin by definition, being $\nu_X^*$ of a bounded below étale complex.
