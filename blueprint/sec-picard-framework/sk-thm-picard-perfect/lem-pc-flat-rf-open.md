+++
id = "lem-pc-flat-rf-open"
kind = "lemma"
title = "The open locus of invertible $Rf_*$"
order = 682
uses = ["def-pc-derived-category", "def-pc-derived-pullback", "def-pc-perfect-complex", "lem-pc-flat-complex-derived-pullback", "lem-pc-perfect-locus", "lem-pc-rf-perfect-base-change", "thm-pc-semicontinuity-base-change"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_opens_range_subset_iff_isFiniteLocallyFreeInDegree"]
+++
Let
$f:X\to S$ be a proper morphism of finite presentation and let $\mathcal{F}$ be an
$\mathcal{O}_X$-module of finite presentation, flat over $S$. Fix integers $i,r\ge0$.
Then there exists an open subscheme $U\subset S$, namely the set $U_{i,r}$ of points
$s\in S$ with $H^q(X_s,\mathcal F_s)=0$ for $q\neq i$ and
$\dim_{\kappa(s)}H^i(X_s,\mathcal F_s)=r$, such that a morphism
$T\to S$ factors through $U$ if and only if $Rf_{T,*}\mathcal{F}_T$ is isomorphic
to a finite locally free $\mathcal{O}_T$-module of rank $r$ placed in degree $i$,
that is, $R^qf_{T,*}\mathcal F_T=0$ for $q\neq i$ and $R^if_{T,*}\mathcal F_T$ is
finite locally free of rank $r$. Here $f_T:X_T\to T$ is the base change of $f$ and
$\mathcal F_T$ the pullback of $\mathcal F$ to $X_T$.

## Proof

Put $E=Rf_*\mathcal{F}\in D(\mathcal{O}_S)$ (see [def-pc-derived-category]).
By [lem-pc-rf-perfect-base-change], $E$ is perfect and for every
$g:T\to S$ the canonical map $Lg^*E\to Rf_{T,*}\mathcal{F}_T$ is an
isomorphism, with $Lg^*$ the [def-pc-derived-pullback]. For $s\in S$
write $\beta^q(s)=\dim_{\kappa(s)}H^q(X_s,\mathcal{F}_s)$.

*The locus.* Let $U\subseteq S$ be the set of points $s$ with
$\beta^q(s)=0$ for all $q\neq i$ and $\beta^i(s)=r$. We show $U$ is
open. Fix $t\in S$. As in the proof of
[thm-pc-semicontinuity-base-change], by [def-pc-perfect-complex] there is
an affine open $V=\operatorname{Spec}(A)\ni t$ on which $E|_V$ is
represented by a bounded complex
$K:\;0\to K^a\to\cdots\to K^b\to0$ with $K^q\cong A^{n_q}$, and for
$s\in V$, since the terms of $K$ are flat,
[lem-pc-flat-complex-derived-pullback] and the base-change isomorphism
give

$$
H^q(X_s,\mathcal{F}_s)\cong H^q(K\otimes_A\kappa(s)).
$$

In particular $\beta^q\equiv0$ on $V$ for $q\notin[a,b]$, so on $V$ only
the finitely many conditions with $q\in[a,b]$ matter. By
[thm-pc-semicontinuity-base-change](2) each $\beta^q$ is upper
semicontinuous, so

$$
W=\{s\in V:\ \beta^q(s)\le0\ (q\neq i,\ a\le q\le b),\ \beta^i(s)\le r\}
$$

is a finite intersection of open subsets of $V$, hence open. For $s\in W$
the complex $K\otimes_A\kappa(s)$ of finite dimensional vector spaces has
cohomology only in degree $i$, so

$$
(-1)^i\beta^i(s)=\sum_q(-1)^q\dim_{\kappa(s)}H^q(K\otimes_A\kappa(s))
=\sum_q(-1)^qn_q ,
$$

which does not depend on $s\in V$. Hence $\beta^i$ is constant on $W$,
and $U\cap V$ is either $W$ or empty. In either case it is open, and
since such $V$ cover $S$, $U$ is open.

*The functorial characterization.* Let $g:T\to S$. Both sides of the
claimed equivalence are local on $T$: $g$ factors through the open $U$ iff
it does so over each member of an open cover of $T$, and the vanishing and
local freeness of the $R^qf_{T,*}\mathcal F_T$ are local on $T$, while
higher direct images are compatible with restriction to opens of $T$. So
we may assume that $g$ maps $T$ into one of the affine opens
$V=\operatorname{Spec}(A)$ above, on which $E|_V$ is represented by the
bounded complex $K$ of finite free modules; padding $K$ with zero terms we
may assume $a\le i$, so that after shifting by $-a$ it is concentrated in
degrees $[0,b-a]$ and $i$ becomes $i-a\ge0$. Let $U_K\subseteq V$ be the
open subscheme attached to this complex and to $i-a,r$ by
[lem-pc-perfect-locus]; undoing the shift, a morphism into $V$ factors
through $U_K$ iff the pullback of $K$ is a finite locally free module of
rank $r$ placed in degree $i$. A point $s\in V$ lies in $U_K$ iff
$g_s:\operatorname{Spec}\kappa(s)\to V$ factors through $U_K$, i.e. iff
$K\otimes_A\kappa(s)$, which computes $Lg_s^*E\cong Rf_{s,*}\mathcal{F}_s$,
is isomorphic to $\kappa(s)^{r}$ placed in degree $i$. As
$\operatorname{Spec}\kappa(s)$ is a point, the cohomology of
$Rf_{s,*}\mathcal{F}_s$ is $H^*(X_s,\mathcal{F}_s)$, and a complex over a
field is quasi-isomorphic to the sum of its shifted cohomology groups; so
this holds iff $s\in U$. Thus $U\cap V=U_K$. By [lem-pc-perfect-locus],
$g:T\to V$ factors through $U_K=U\cap V$ iff $Lg^*E$ is isomorphic to a
finite locally free $\mathcal{O}_T$-module of rank $r$ placed in degree
$i$, i.e. by the base-change isomorphism iff $Rf_{T,*}\mathcal{F}_T$ is;
since $Rf_{T,*}\mathcal F_T$ has cohomology sheaves
$R^qf_{T,*}\mathcal F_T$, this is the condition of the statement.
On $U$ itself this gives (Nakayama, as in [lem-pc-perfect-locus]) that
$Rf_*\mathcal{F}|_U$ is locally a free module of rank $r$ in degree $i$;
no reducedness of $S$ is needed.
