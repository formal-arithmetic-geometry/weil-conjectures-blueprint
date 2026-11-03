+++
id = "prose-02-49"
kind = "hidden"
title = "Condensed rings (1)"
order = 172
+++
The constant sheaf with value the abstract ring $\mathbf Z_\ell$ forgets the topology
of $\mathbf Z_\ell$, and on $\operatorname{Spec}\mathbf F_q$ it has $H^1=0$
(Section [sec-Weil-cohomology]). We therefore need a notion
of coefficient ring on a geometric point that retains the topology. The
pro-étale site of a separably closed field is the site of profinite sets
(Proposition [proposition-pro-etale-site-separably-closed] below). So a
coefficient ring must at least be a sheaf of rings on profinite sets, that
is, a condensed ring. The continuous maps from profinite sets into $\mathbf Z_\ell$ form
such a sheaf. With it, $H^1$ of $\mathbf F_q$ becomes $\mathbf Z_\ell$
(Example [example-first-cohomology-finite-field]).

Let $*_{\mathrm{pro}\acute{e}t}$ be the site of profinite sets, with finite jointly
surjective families as covers. A *condensed ring* is a sheaf of
rings on $*_{\mathrm{pro}\acute{e}t}$. A topological ring $V$ defines a condensed ring
$\underline V$, whose sections over $S$ are the continuous maps $S\to V$.
This is a sheaf because a surjection of profinite sets is a quotient map.
