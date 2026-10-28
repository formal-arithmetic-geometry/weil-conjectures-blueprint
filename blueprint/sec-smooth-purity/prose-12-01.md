+++
id = "prose-12-01"
kind = "hidden"
title = "Frobenius and Lefschetz–Verdier: overview and conventions"
order = 3014
+++
Weil's axiom (b) asks that $\ell$-adic cohomology count rational points, by a
Lefschetz trace formula for Frobenius. This section provides the two
ingredients of such a formula. The first is Frobenius itself: a variety
$X_0$ over $\mathbf F_q$ endows $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$
and every complex pulled back from $X_0$ with a Frobenius action, and we
check that smooth purity and duality respect it (Section “Frobenius and Weil complexes”).
The second is the Lefschetz–Verdier formula, which computes the trace of
the endomorphism of $R\Gamma_c$ induced by a cohomological correspondence as
a sum of local terms at its fixed points
(Theorem [sk-p-proper]). Section “The Grothendieck–Lefschetz trace formula”
applies it to the graph of Frobenius.

Throughout, $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$ and
$s=\operatorname{Spec}k$. For a scheme $X$ over $k$, $a_X:X\to s$
is the structure morphism, and $X=X_0\times_{k_0}k$ whenever a model
$X_0$ over $k_0$ is given. In Section “Frobenius and Weil complexes” the coefficient ring
$\Lambda$ is any admissible ring; from Section “Traces of perfect complexes”
until Section “Integral, rational and algebraic coefficients” it is an arbitrary finite commutative
$\ell$-primary ring $A$, with $\ell\ne\operatorname{char}k$. We write $\omega_X=a_X^!A_s$ and
$\mathbb D_XK=\cHom_A(K,\omega_X)$ for the dualizing complex and the
Verdier dual of Definition [sk-def-ops] with coefficients $A$.
In some proofs we compute on small
étale sites and transport the result by means of the comparison
theorems for complexes of finite Tor amplitude.

The Weil conjectures concern varieties over $\mathbf F_q$, while the six
operations of Part “The six operations” live on schemes over the algebraic
closure. What a variety $X_0$ over $\mathbf F_q$ leaves behind on
$X=X_0\times_{\mathbf F_q}k$ is an action of Frobenius, on $X$ and on every
complex pulled back from $X_0$. We fix the conventions for this action once
here: the geometric Frobenius $\operatorname{Fr}_X$, Weil structures on
complexes, the Frobenius operator they induce on cohomology with compact
support, and its effect on Tate twists. We then check that smooth purity and duality respect these structures. The
comparison of $\operatorname{Fr}_X$ with the scheme Frobenius, whose graph
the trace formula uses, is made in Section “The Grothendieck–Lefschetz trace formula”.

Here $k_0=\mathbf F_q$ and $k$ is an algebraic closure of
$k_0$. The geometric Frobenius
$\sigma\in\operatorname{Gal}(k/k_0)$ is the inverse of the arithmetic
Frobenius $a\mapsto a^q$. For a scheme $T$ of the form
$T_0\times_{k_0}k$, with $T_0$ over $k_0$, let

$$
\operatorname{Fr}_T:T\longrightarrow T
$$

be the semilinear automorphism induced by $\sigma$. It is a morphism of
schemes covering the automorphism $\operatorname{Spec}(\sigma)$ of
$\operatorname{Spec}k$.

We use $\operatorname{Fr}_T$ to define Weil structures. Two other
Frobenius maps are common: the absolute $q$-power Frobenius
$F_T$, and the $k$-linear map
$\Phi_T=F_{T_0/k_0}\times_{k_0}k$ obtained by base change from the
$q$-power Frobenius of $T_0$, which on coordinate rings is
$a\otimes b\mapsto a^q\otimes b$. They are related by

$$
\Phi_T=F_T\circ\operatorname{Fr}_T .
$$

Since pullback along absolute Frobenius is isomorphic to the identity
functor on étale sheaves, Weil structures defined with
$\operatorname{Fr}_T$ correspond to the usual formulation with $\Phi_T$.
The trace formula is proved for $\Phi_X$, whose graph is a
correspondence over $k$, and translated to $\operatorname{Fr}_X$ by
Lemma [sk-lem-tf-frobenius-convention]. The fixed points of $\Phi_X^m$ are
the points of $X_0$ over $\mathbf F_{q^m}$.
