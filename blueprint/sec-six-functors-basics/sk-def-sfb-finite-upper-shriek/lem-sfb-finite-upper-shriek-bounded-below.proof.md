+++
kind  = "proof"
of    = "lem-sfb-finite-upper-shriek-bounded-below"
uses = ["thm-sfb-finite-proper-pushforward-left-adjoint"]
+++
Let $K\in D^{\ge n}$. For $M\in D^{\le n-d-1}(\bar X_{\mathrm{proét}},\mathcal A)$ we have
$Rg_*M\in D^{\le n-1}$, so by the adjunction of
[thm-sfb-finite-proper-pushforward-left-adjoint]
$\Hom(M,Rg^!K)=\Hom(Rg_*M,K)=0$. Hence $Rg^!K\in D^{\ge n-d}$. The exact functor $D(i^*)$
preserves this bound, so $Rf^!K=D(i^*)Rg^!K\in D^{\ge n-d}$.

The bound $d$ cannot be dropped. Let $k$ be separably closed with $\ell\ne\operatorname{char}k$,
let $\mathcal A=\Mod_{\mathbf Z/\ell}$, and let $f\colon\coprod_{n\ge0}\mathbf P^n_k\to
\coprod_{n\ge0}\operatorname{Spec}k$ be the disjoint union of the structure morphisms. This
$f$ is proper. For any compactification, $i$ is an open and closed immersion, so
$\Hom(M,Rf^!K)=\Hom(Rf_*M,K)$. On the $n$-th component, $H^{2n}(\mathbf P^n_k,\mathbf Z/\ell)\ne0$
gives $\Hom(Rf_*(\mathbf Z/\ell_{\mathbf P^n})[2n],\mathbf Z/\ell)\ne0$, hence
$H^{-2n}(\mathbf P^n_k,Rf^!\mathbf Z/\ell)\ne0$ for every $n$. This is impossible if
$Rf^!\mathbf Z/\ell$ is bounded below.
