+++
id = "prose-12-02"
kind = "hidden"
title = "Frobenius and Weil complexes"
order = 530
+++
The Weil conjectures concern varieties over $\mathbf F_q$, while the six
operations of Part “The six operations” live on schemes over the algebraic
closure. What a variety $X_0$ over $\mathbf F_q$ leaves behind on
$X=X_0\times_{\mathbf F_q}k$ is an action of Frobenius, on $X$ and on every
complex pulled back from $X_0$. We fix the conventions for this action once
here: the geometric Frobenius $\operatorname{Fr}_X$, Weil structures on
complexes, the Frobenius operator they induce on cohomology with compact
support, and its effect on Tate twists. We then check that smooth purity and duality respect these structures. The
comparison of $\operatorname{Fr}_X$ with the scheme Frobenius, whose graph
the trace formula uses, is made in Section [sec-trace-formula].

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

Since $\operatorname{Fr}_T$ is an automorphism of schemes, pullback of
sheaves of modules along it is exact and preserves derived completeness.
Hence, for every admissible coefficient ring $\Lambda$, it induces an
autoequivalence

$$
\operatorname{Fr}_T^*:
D^b_{\mathrm{ctf}}(T,\Lambda)\longrightarrow
D^b_{\mathrm{ctf}}(T,\Lambda),
$$

which agrees with the derived inverse image along $\operatorname{Fr}_T$.

One could work with complexes on $T_0$ instead and pull them back to
$T$. We keep only the part of that datum that the trace formula sees:
the complex on $T$, where all cohomology is computed, together with an
identification of it with its Frobenius pullback. This has two
advantages. First, every construction on $T$ (direct images, $f^!$,
truncations, duals) carries such identifications along by base change,
as we check below, without descending anything to $T_0$. Second, there
are more of these pairs than complexes on $T_0$, and the extra ones are
needed. For a $\Ql$-sheaf on $T_0$, the stalk at a geometric point over
a closed point is a continuous representation of a Galois group, so
Frobenius preserves a lattice in it and its eigenvalues are $\ell$-adic
units. On $\operatorname{Spec}k$, the sheaf $\Ql$ with
Frobenius acting by $\ell$ is a pair of this kind that does not come
from $\operatorname{Spec}\mathbf F_q$. Pulled back to a scheme, such
pairs are the sheaves $\mathcal B_b$ that normalize weights in
Proposition [sk-r-real-linear]. We require an
isomorphism so that the Frobenius operator on cohomology is invertible
over a field (Theorem [sk-thm-frobenius]); the trace formula itself
only needs a morphism (Definition [sk-d-weil]). The trace formula
(Theorem [sk-thm-tf-uniform-formula]) is stated for these pairs.
