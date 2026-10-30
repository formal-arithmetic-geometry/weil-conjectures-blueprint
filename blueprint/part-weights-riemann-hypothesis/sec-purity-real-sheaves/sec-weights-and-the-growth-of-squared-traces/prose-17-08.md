+++
id = "prose-17-08"
kind = "hidden"
title = "Weights and the growth of squared traces"
order = 700
+++
In Section [sec-deligne-laumon-a1] we determine weights from trace
functions alone. This is possible because the growth of the squared
trace sums of a pure sheaf equals its weight
(Theorem [sk-thm-wrp-l2-dictionary]). Since Theorem [sk-p-real-purity] only applies to real
sheaves, we reach an arbitrary pure sheaf by twisting it to weight zero
and adding its dual.

The inequality $\nu\le w$ is a count of points. The content of the
theorem is the reverse inequality, which says that the squared traces
of a pure sheaf are not small on average, and this is again
positivity. For a real sheaf $\mathcal G$, the squared trace
$|\iota t_{\mathcal G,n}(x)|^2$ is the trace of
$\mathcal G\otimes\mathcal G$ at $x$, so the generating series of the
sums $S_n(\mathcal G)$ is the logarithmic derivative of the
$L$-function of $\mathcal G\otimes\mathcal G$. The trace formula and
Lemma [sk-lem-wrp-hc2] put all poles of this $L$-function on the circle
$|t|=q^{-w-1}$, and the nonnegative coefficients of its Euler factors
(Lemma [sk-lem-wrp-positive-euler]) show that it is not a polynomial, so
that a pole exists. The twist and the dual in the proposition below
reduce the general case to this one, and the same construction makes
the direct images in Section [sec-deligne-laumon-general] real.
