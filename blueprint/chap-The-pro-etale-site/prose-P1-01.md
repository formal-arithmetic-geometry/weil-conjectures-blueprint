+++
id = "prose-P1-01"
kind = "hidden"
title = "The six operations"
order = 22
+++
On the étale site the constant sheaf $\mathbf Z_\ell$ on
$\operatorname{Spec}\mathbf F_q$ has $H^1=0$, although
$\varprojlim_nH^1(\operatorname{Spec}\mathbf F_q,\mathbf Z/\ell^n)=\mathbf Z_\ell$
(Section [sec-Weil-cohomology]). Frobenius eigenvalues live in
$\overline{\mathbf Q}_\ell$, but SGA 4 constructs $Rf_!$ and $f^!$ and proves the finiteness
theorems only for $\mathbf Z/\ell^n$ [sga4], [sga4-5]. So the theory we
need is not the one SGA 4 provides. The first task of the notes is to pass to the limit over $n$ without losing cohomology.
Classically one works with systems $(F_n)$ and makes every derived
construction by hand [ekedahl90]. We work instead on the pro-étale site
of Bhatt and Scholze (Section [chap-The-pro-etale-site]). There $\mathbf Z_\ell$ is a sheaf
of rings with the expected cohomology. Moreover, one definition serves all the
coefficient rings

$$
A,\ \mathbf Z_\ell,\ \mathcal O_E,\ \mathbf Q_\ell,\ E,\ \overline{\mathbf Q}_\ell,
$$

compatibly with every change of coefficients between them
(Section [sec-Change-of-coefficients]).

What the rest of the notes needs from this part is the table of
Section [sec-The-function-sheaf-dictionary]: for every morphism $f$ of schemes of finite
type over $k$, the operations $f^*$, $Rf_*$, $Rf_!$, $f^!$,
$\otimes^{\mathbf L}$ and $\cHom$, with their adjunctions, base change and
projection formulas, and the finiteness statement that each carries
constructible complexes to constructible complexes
(Theorem [theorem-exceptional-inverse-image] and
Proposition [proposition-six-operations-dctf]). Each later part uses
them. The trace formula of Part II sums trace functions
over the fibres of $f$ by applying $Rf_!$. Poincaré duality comes from the
computation of $a^!\Lambda$. The Fourier transform of Part III
is built from $f^*$, $\otimes^{\mathbf L}$ and $Rf_!$.

The second difficulty is independent of the coefficients. The functor $f^!$ is
given only by its universal property, and already for a closed immersion $i$
with open complement $j$ its value is not obvious. We know only that $i^!K$
sits in a triangle $i^!K\to i^*K\to i^*Rj_*j^*K$. To see that it is
constructible we need to know that $Rj_*$ preserves constructibility, and this
is Deligne's generic base change theorem. We construct $f^!$ in
Section [chap-Construction-of-f] and prove that it preserves
constructible complexes in Section [chap-Constructibility-of-f], as
sketched in Section [sec-The-six-operations].

The geometry, namely proper base change
(Section [chap-Proper-base-change]) and the computation of $f^!$, is
done once, with torsion coefficients on the étale site, where it is
classical. Two facts carry it to $\ell$-adic coefficients
(Sections [chap-Constructible-complexes]
and [chap-The-six-operations-on-Dbctf]). A constructible complex over $\mathcal O_E$
is determined by its reductions modulo $\pi_E^n$
(Proposition [proposition-integral-constructibility-criterion]), and whether
an exact transformation is an isomorphism may be checked with finite
coefficients (Proposition [proposition-isomorphisms-reduce-finite-coefficients]).
