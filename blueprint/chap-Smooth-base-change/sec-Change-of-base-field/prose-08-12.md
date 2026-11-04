+++
id = "prose-08-12"
kind = "hidden"
title = "Change of base field (1)"
order = 680
+++
Proposition [proposition-base-change-larger-algebraically-closed] below
shows that $R^qh_*\mathbf Z/m=0$. This contradicts
Lemma [lemma-reduction-curve-over-normal-base] and finishes the
induction. The sheaf $R^qh_*\mathbf Z/m$ is the sheafification of
$U\mapsto H^q(U_\Omega,\mathbf Z/m)$ on $C_{\acute{e}t}$. We must therefore show
that classes on $U_\Omega$ die after étale localization on $U$.
In degrees $q\geq2$ there is nothing to kill, since affine curves over an
algebraically closed field have cohomological dimension one.

In degree one the problem is about covers. Over the generic point of $S$, a
class on $C_\Omega$ already comes from $C_L$, by the invariance of $H^1$ of
a curve under extension of algebraically closed fields
(Theorem [theorem-cohomology-curves]). In other words, it is given by a
$\mathbf Z/m$-torsor over $C_L$. It suffices to find an étale cover of $C$
on which this torsor becomes trivial. We take a connected component of the
torsor and extend it over $C$ by the extension theorem for Galois covers of
order invertible on $S$. This theorem needs $S$ normal and a section of
$C\to S$. Since the fraction field $L$ is algebraically closed, the generic
fibre $C_L$ has a rational point. After étale localization on $S$ this
point extends to a section.

We use that $m$ is invertible in two places, and both fail for
$p$-torsion. First, the invariance of $H^1$ fails: the Artin–Schreier
class of $tx$ on $\mathbf A^1_{k(t)^{\mathrm{sep}}}$ does not come from
$\mathbf A^1_k$. Second, the extension theorem can fail for covers of
degree divisible by a residue characteristic, because such covers may be
wildly ramified along the special fibres.
