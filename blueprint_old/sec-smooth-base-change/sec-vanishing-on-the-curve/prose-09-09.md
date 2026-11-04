+++
id = "prose-09-09"
kind = "hidden"
title = "Vanishing on the curve"
order = 410
+++
After these reductions it remains to prove one vanishing statement, which
we deduce from the cohomology of curves and the extension theorem for Galois covers.

The sheaf $R^qh_*\mathbf Z/m$ is the sheafification of
$U\mapsto H^q(U_\Omega,\mathbf Z/m)$ on $C_{\acute{e}t}$, so we must show that classes on $U_\Omega$ die after étale localization on $U$.
In degrees $q\geq2$ there is nothing to kill, since affine curves over an
algebraically closed field have cohomological dimension one. In degree one
the problem is a question about covers. Over the generic point of $S$,
a class on $C_\Omega$ already comes from $C_L$, by the invariance of $H^1$
of a curve under extension of algebraically closed fields
(Theorem [sk-thm-curve-package]), so it is a $\mathbf Z/m$-torsor over
$C_L$. It suffices to find an étale cover of $C$ on which this torsor
becomes trivial, and we take a connected component of the torsor and
extend it over $C$ by the extension theorem for Galois covers of order
invertible on $S$. This theorem needs $S$ normal and a section of
$C\to S$. Since the fraction field $L$ is algebraically closed, the
generic fibre $C_L$ has a rational point, and after étale localization
on $S$ it extends to a section. Proposition [sk-thm-vanishing] contradicts
Lemma [sk-lem-universal-datum] and so finishes the induction.

The hypothesis that $m$ is invertible enters in two places, and both
fail for $p$-torsion. The invariance of $H^1$ fails, since the
Artin–Schreier class of $tx$ on $\mathbf A^1_{k(t)^{\mathrm{sep}}}$ does
not come from $\mathbf A^1_k$, and the
extension theorem can fail for covers of degree divisible by a residue
characteristic, since such covers may be wildly ramified along the
special fibres.
