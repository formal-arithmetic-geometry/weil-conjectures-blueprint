+++
id = "theorem-weil-conjectures-smooth-proper-schemes--text-1"
kind = "hidden"
title = "The Weil conjectures for smooth proper schemes"
order = 1388001
+++
*Shared context.* In the Lean statements below, $X_0/\mathbf F_q$ is smooth, proper and geometrically connected of pure dimension $d$, unless weaker hypotheses are stated explicitly. Put $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$ and
$$
\overline H^i_\ell=H^i(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell),\qquad
\overline P_{i,\ell}(T)=\det(1-TF_i\mid\overline H^i_\ell).
$$
These are the coefficient field and determinant factors used by `AlgebraicGeometry.Scheme.frobeniusCharpolyRev`. The comparison with the $\mathbf Q_\ell$-cohomology in the human statement is not part of the assembly theorem.

An *integral Weil factorization* $P=(P_0,\ldots,P_{2d})$ of a series $Z\in\mathbf Q[[T]]$ means that $P_i\in\mathbf Z[T]$, $P_i(0)=1$, $P_0=1-T$, $P_{2d}=1-q^dT$, and $Z\prod_{i\ \mathrm{even}}P_i=\prod_{i\ \mathrm{odd}}P_i$. Unless specified otherwise, $P$ denotes a family supplied by [theorem-weil-conjectures-smooth-proper-schemes--1]. The two definitions of $b_i$ and $\chi$ below retain the human notation.
