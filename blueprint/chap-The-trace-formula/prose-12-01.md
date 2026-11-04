+++
id = "prose-12-01"
kind = "hidden"
title = "The trace formula (1)"
order = 940
+++
The Lefschetz–Verdier formula
(Theorem [theorem-proper-pushforward-lefschetz-verdier]) writes a
trace on cohomology as a sum of local terms, but it says nothing about what a local
term is. To count points we need the local term of Frobenius at a fixed point to be
the trace on the stalk. Let $X_0$ be a separated scheme of finite type over
$\mathbf F_q$, let $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and let
$\ell\nmid q$. By Lemma [lemma-frobenius-fixed-scheme], the points of $X_0$ over
$\mathbf F_{q^m}$ are the fixed points of the $m$-th power of the Frobenius $\Phi_X$
on $X$. For a self-map $\varphi$ of a compact manifold with transverse fixed points,
the Lefschetz formula counts each fixed point $x$ with the sign of
$\det(1-d\varphi_x)$. The differential of Frobenius is zero, so we expect every sign to
be $+1$. On a curve this can be seen directly. If $y$ is a fixed point of
$\Phi_X^m$, $u$ is a uniformizer at $y$ defined over $\mathbf F_{q^m}$, and $v$ is the
same function on the second factor, then near $(y,y)$ the graph of $\Phi_X^m$ is
$v=u^{q^m}$, and it meets the diagonal $v=u$ with multiplicity one, since
$u^{q^m}-u$ has a simple zero at $u=0$.
