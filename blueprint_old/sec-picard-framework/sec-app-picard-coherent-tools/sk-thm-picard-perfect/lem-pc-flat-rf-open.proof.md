+++
kind  = "proof"
of    = "lem-pc-flat-rf-open"
+++
For $s\in S$ write $\beta^q(s)=\dim_{\kappa(s)}H^q(X_s,\mathcal{F}_s)$, and let
$U\subseteq S$ be the set of points $s$ with $\beta^q(s)=0$ for all $q\neq i$
and $\beta^i(s)=r$. Base changes are as in [def-pc-base-change].

*The local model.* Fix $t\in S$ and an affine open $S_0\ni t$. Applying
[lem-pc-rf-perfect-base-change](1) to the restriction
$f^{-1}(S_0)\to S_0$ of $f$, which is again proper of finite presentation
with $\mathcal F|_{f^{-1}(S_0)}$ of finite presentation and flat over $S_0$,
gives an open $V\ni t$ contained in $S_0$ and a bounded complex $P$ of finite
free $\mathcal{O}_V$-modules, concentrated in degrees $[0,d]$, such that for
every morphism $g:T\to V$, with $f_T:X_T\to T$ and $\mathcal F_T$ the base
changes of $f$ and $\mathcal F$ along $T\to V\subseteq S$,

$$
\mathcal H^q(g^*P)\cong R^qf_{T,*}\mathcal F_T\qquad(q\ge0).
$$

For $s\in V$ and $g=g_s:\operatorname{Spec}\kappa(s)\to V$ the target is a
point, on which the higher direct images are the cohomology groups of the
fibre; hence $H^q(X_s,\mathcal F_s)\cong H^q(P\otimes\kappa(s))$ for all $q$
(both sides vanish for $q<0$ and $q>d$).

*The criterion over $V$.* Let $U_P\subseteq V$ be the open subscheme attached
to $P$ and to $i,r$ by [lem-pc-perfect-locus]: a morphism $g:T\to V$ factors
through $U_P$ if and only if $\mathcal H^q(g^*P)=0$ for $q\neq i$ and
$\mathcal H^i(g^*P)$ is finite locally free of rank $r$. Since $P$ lives in
degrees $\ge0$, the local model turns this into: $R^qf_{T,*}\mathcal F_T=0$ for
$q\neq i$ and $R^if_{T,*}\mathcal F_T$ is finite locally free of rank $r$. For
$g=g_s$ ($s\in V$) a finite locally free module of rank $r$ over the point
$\operatorname{Spec}\kappa(s)$ is an $r$-dimensional vector space, so
$s\in U_P$ if and only if $\beta^q(s)=0$ for $q\neq i$ and $\beta^i(s)=r$,
i.e. $s\in U$. Thus $U\cap V=U_P$, an open subset of $V$.

*Globalisation.* Such opens $V$ cover $S$, so $U$ is open. Let $g:T\to S$ be a
morphism. Whether $g$ factors through $U$ is local on $T$, and so is the
condition on the $R^qf_{T,*}\mathcal F_T$, since higher direct images are
compatible with restriction to opens of $T$. Cover $T$ by the opens
$g^{-1}(V)$ for the $V$ above. Over $g^{-1}(V)$ the restriction of $f_T$ is
the base change of $f$ along $g^{-1}(V)\to V\subseteq S$, and by the
criterion over $V$, $g|_{g^{-1}(V)}$ factors through $U\cap V=U_P$ if and only
if the higher direct images of $\mathcal F_T$ restricted over $g^{-1}(V)$
vanish outside degree $i$ and are finite locally free of rank $r$ in degree
$i$. Hence $g$ factors through $U$ if and only if $R^qf_{T,*}\mathcal F_T=0$
for $q\neq i$ and $R^if_{T,*}\mathcal F_T$ is finite locally free of rank $r$,
which is the claim. No reducedness of $S$ is needed.
