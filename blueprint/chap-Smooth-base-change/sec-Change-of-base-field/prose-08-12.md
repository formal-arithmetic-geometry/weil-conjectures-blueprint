+++
id = "prose-08-12"
kind = "hidden"
title = "Change of base field (1)"
order = 686
+++
Lemma [lemma-reduction-curve-over-normal-base] turned a failure of
$\mathrm{BC}(g,n,q)$ into a single nonvanishing sheaf $R^qh_*\mathbf Z/m\ne0$,
where $h:C_\Omega\to C$ is the base change of a smooth affine curve $C$ over a
normal base $S$ to a larger algebraically closed field $\Omega$.
Proposition [proposition-base-change-larger-algebraically-closed] below
shows that this sheaf vanishes, which contradicts the lemma and finishes the
induction. As the sheaf $R^qh_*\mathbf Z/m$ is the sheafification of
$U\mapsto H^q(U_\Omega,\mathbf Z/m)$ on $C_{\acute{e}t}$, we must show
that classes on $U_\Omega$ die after étale localization on $U$.
In degrees $q\geq2$ there is nothing to kill, since affine curves over an
algebraically closed field have cohomological dimension one.

In degree one the problem is about covers. Recall that $S=\operatorname{Spec}R$
with $R$ a normal domain whose fraction field $L$ is algebraically closed, and
$L\subset\Omega$ (Lemma [lemma-reduction-curve-over-normal-base]). Over the
generic point of $S$, a class on $C_\Omega$ already comes from $C_L$, by the invariance of $H^1$ of
a curve under extension of algebraically closed fields
(Theorem [theorem-cohomology-curves]). In other words, it is given by a
$\mathbf Z/m$-torsor over $C_L$, so it suffices to find an étale cover of
$C$ on which this torsor becomes trivial. To find one, we take a connected
component of the torsor and extend it over $C$ by the extension theorem for
Galois covers of order invertible on $S$. This theorem needs $S$ normal and
a section of $C\to S$. The section is available: since $L$ is
algebraically closed, the generic fibre $C_L$ has a rational point, and
after étale localization on $S$ this point extends to a section.

We use that $m$ is invertible in two places, and both fail for
$p$-torsion. First, the invariance of $H^1$ fails: the Artin–Schreier
class of $tx$ on $\mathbf A^1_{k(t)^{\mathrm{sep}}}$ does not come from
$\mathbf A^1_k$. Second, the extension theorem can fail for covers of
degree divisible by a residue characteristic, because such covers may be
wildly ramified along the special fibres.
