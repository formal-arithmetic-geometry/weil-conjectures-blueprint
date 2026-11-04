+++
id = "prose-12-03"
kind = "hidden"
title = "Frobenius correspondences (1)"
order = 944
+++
Two Frobenius maps act on $X=X_0\times_{k_0}k$: the $k$-linear scheme
Frobenius $\Phi_X$ and the semilinear geometric Frobenius $\operatorname{Fr}_X$
that defines Weil structures. We prove the trace formula for $\Phi_X$, whose graph is a
correspondence over $k$, and Lemma [lemma-scheme-frobenius-geometric-frobenius]
translates it to $\operatorname{Fr}_X$.

The operator $T_{c_m}$ on cohomology with compact support defined below
makes sense even when $X$ is not proper, because the second leg
$\Phi_X^m$ of the graph $c_m$ is proper. Indeed, $\Phi_X$ and all its iterates
are finite, since a finitely generated algebra over a perfect field is finite over
its subring of $q$-th powers.

We cannot work with $\operatorname{Fr}_X$ directly. The Weil structure
$\phi_K$ is a map $\operatorname{Fr}_X^*K\to K$, but
$\operatorname{Fr}_X$ lies over the automorphism $\operatorname{Spec}(\sigma)$
of $s$. Hence its graph is not a morphism $X\to X\times_sX$ of $k$-schemes.
The formalism of Section [chap-The-Lefschetz-Verdier-formula] uses $c_1^!$ only for
$k$-morphisms, so it does not apply to this graph. The $k$-linear
$\Phi_X=F_X\circ\operatorname{Fr}_X$, on the other hand, has a graph of the
required kind. Pullback along the absolute Frobenius $F_X$ is the
identity on étale sheaves, and this is how
Lemma [lemma-scheme-frobenius-geometric-frobenius]
turns $\phi_K$ into a map $\Phi_X^*K\to K$. For example, on $X=\mathbf A^1_k$ the map
$\Phi_X$ is $t\mapsto t^q$. The fixed points of $\Phi_X^m$ are then the
$q^m$ elements of $\mathbf F_{q^m}$, and Lemma [lemma-frobenius-fixed-scheme]
describes them in general.

We allow maps $\Phi_X^*K\to K$ that are not isomorphisms,
because the proof over $E$ clears denominators: it multiplies a Weil
structure by a power of $\pi_E$ (Lemma [lemma-integral-models-rational-frobenius-correspondences]). The
operators below are the two sides of the trace formula in
Theorem [theorem-trace-formula-frobenius-correspondence].
