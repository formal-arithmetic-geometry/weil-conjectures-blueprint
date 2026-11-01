+++
kind  = "proof"
of    = "det-lem-coefficient-finite-descent-sections"
+++
(1) Let $\mathcal P$ be the presheaf colimit $U\mapsto\varinjlim_\alpha\mathcal F_\alpha(U)$. We
claim that on quasi-compact quasi-separated objects $\mathcal P$ already satisfies the sheaf
condition and agrees with its sheafification. Every covering of a quasi-compact
quasi-separated $W$ in $X_{\mathrm{proét}}$ admits a finite subcovering by affine objects
(\stacks{0988}), and the fibre products of these over $W$ are again quasi-compact (and
quasi-separated) because $W$ is quasi-separated. For a finite covering
$\{W_k\to W\}$, the sheaf condition is the equalizer
$\mathcal F(W)\to\prod_k\mathcal F(W_k)\rightrightarrows\prod_{k,k'}\mathcal F(W_k\times_WW_{k'})$,
a finite limit; filtered colimits of sets commute with finite limits, so $\mathcal P$
satisfies it for such coverings. Since the quasi-compact quasi-separated (e.g. affine) objects form a basis of the site
whose coverings are refined by finite ones, the sheafification of $\mathcal P$ agrees with
$\mathcal P$ on quasi-compact quasi-separated objects. (This is the degree-zero case of \stacks{0739}.)

(2) By [sk-prop-sfb-qlbar-colimit-x], $\QbarX=\varinjlim_EE_X$, a filtered colimit, so by (1)
$\QbarX(V)=\varinjlim_EE_X(V)$. The transition maps are injective: $E_X\to F_X$ is the
inclusion of a direct summand of a finite free module (a basis of $F$ over $E$ containing
$1$), so injective on sections. Hence the colimit is the union, and finitely many elements
lie in a common $E_X(V)$ because the poset of finite subextensions is filtered.
