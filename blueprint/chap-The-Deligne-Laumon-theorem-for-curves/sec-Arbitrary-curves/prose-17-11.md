+++
id = "prose-17-11"
kind = "hidden"
title = "Arbitrary curves (1)"
order = 1305
+++
Theorem [theorem-weight-bound-affine-line] assumes that the curve is
an open of the affine line and that the sheaf is unramified at infinity.
We remove the second hypothesis by moving a point where the sheaf is
lisse to infinity, and the first by taking the direct image along a
finite map to the line.

For an upper bound it is enough to replace $H^1_c$ by a group that
surjects onto it, and each move does this. For the first move, let $s$ be a point where the
sheaf is lisse. Since a point has no $H^1_c$, deleting $s$ gives a
surjection $H^1_c(W\setminus\{s\},F)\to H^1_c(W,F)$, and after a finite
extension of the constant field and an automorphism of $\mathbf P^1$
sending $s$ to infinity, the sheaf is unramified there. For the second, a finite map
$\pi:C\to\mathbf A^1$ does not change compactly supported cohomology at
all, since $R\Gamma_c(\mathbf A^1,\pi_*j_!F)=R\Gamma_c(C,F)$. However,
$\pi_*j_!F$ is lisse and pure only off the branch locus, so we
remove the bad points by one more localization. Such a map $\pi$ exists
by Riemann–Roch, because a function with a single pole of order prime to
$p$ defines a finite generically étale map
(Lemma [lemma-finite-generically-etale-map-line]). Curves that are not
affine, and the degrees $r\ne1$, are treated afterwards in
Theorem [theorem-weight-bound-curve].
