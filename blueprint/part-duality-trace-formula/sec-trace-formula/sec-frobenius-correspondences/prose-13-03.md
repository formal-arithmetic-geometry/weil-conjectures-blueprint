+++
id = "prose-13-03"
kind = "hidden"
title = "Frobenius correspondences"
order = 571
+++
Two Frobenius maps act on $X=X_0\times_{k_0}k$: the $k$-linear scheme
Frobenius $\Phi_X$ and the semilinear geometric Frobenius $\operatorname{Fr}_X$
that defines Weil structures. We prove the trace formula for $\Phi_X$, whose graph is a
correspondence over $k$, and Lemma [sk-lem-tf-frobenius-convention]
translates it to $\operatorname{Fr}_X$.

Since a finitely generated algebra over a perfect
field is finite over its subring of $q$-th powers, $\Phi_X$ and all
its iterates are finite. Hence the second leg $\Phi_X^m$ of the graph $c_m$
below is proper, and the operator $T_{c_m}$ on cohomology with compact
support is defined even when $X$ is not proper.

The Weil structure $\phi_K$ is a map $\operatorname{Fr}_X^*K\to K$, but
$\operatorname{Fr}_X$ lies over the automorphism $\operatorname{Spec}(\sigma)$
of $s$, so its graph is not a morphism $X\to X\times_sX$ of $k$-schemes
and the formalism of Section [sec-lefschetz-verdier], which uses
$c_1^!$ for $k$-morphisms, does not apply to it. The $k$-linear
$\Phi_X=F_X\circ\operatorname{Fr}_X$ has a graph of the required kind, and
since pullback along the absolute Frobenius $F_X$ is the identity on
étale sheaves, $\phi_K$ gives a map $\Phi_X^*K\to K$
(Lemma [sk-lem-tf-frobenius-convention]). On $X=\mathbf A^1_k$, the map
$\Phi_X$ is $t\mapsto t^q$, and the fixed points of $\Phi_X^m$ are the
$q^m$ elements of $\mathbf F_{q^m}$ (Lemma [sk-lem-tf-fixed-points] in
general). We allow maps $\Phi_X^*K\to K$ that are not isomorphisms,
since the proof over $E$ clears denominators and multiplies a Weil
structure by a power of $\pi_E$ (Lemma [sk-lem-tf-rational-model]). The
operators below are the two sides of the trace formula in
Theorem [sk-thm-tf-coefficient-morphism-formula].
