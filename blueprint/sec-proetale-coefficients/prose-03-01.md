+++
id = "prose-03-01"
kind = "hidden"
title = "Coefficient rings defined once on a point"
order = 1228
+++
The main theorem of Part “The six operations” says that for a separated morphism $f$ of
finite type, the functor $Rf_!$ has a right adjoint $f^!$, and that $f^!$
preserves constructible complexes of finite Tor amplitude, for every
coefficient ring $\Lambda$ among $A$, $\Zl$, $\mathcal O_E$, $\Ql$, $E$
and $\overline{\mathbf Q}_\ell$. Everything after this section takes place in the categories
$\Dctf(X,\Lambda)$ defined here: Part “The six operations” proves the theorem, and the
geometric theorems and the theory of weights use the six operations it
provides. To make one argument work for all these rings, each coefficient
ring is defined once, as a condensed ring on a point, and pulled back to
every scheme. For $\mathcal O_E$ we also prove a criterion that reduces
constructibility to the reduction modulo $\pi_E$
(Proposition [sk-prop-integral-criterion]). The section ends with the
statement of the theorem (Theorem [sk-thm-existence]) and the plan of its
proof.

We want pullback along morphisms and change of coefficients to be
compatible without any bookkeeping. For this we define each coefficient
ring once, on a point, and pull it back to every scheme along a single
morphism of topoi. This gives $A_X$, $\mathcal O_{E,X}$,
$E_X$ and $\overline{\mathbf Q}_{\ell,X}$. Here $A$ is a finite commutative ring killed by a
power of $\ell$, with the discrete topology, and $A_X$ is the usual
constant sheaf. The role of the point is played by the site of
profinite sets described below. By Proposition [sk-prop-pe-condensed-point]
it is the pro-étale site of a separably closed field, which keeps the
topology of the coefficient rings that the étale site of the field
forgets.

Let $*_{\mathrm{pro\acute et}}$ be the site of profinite sets, with finite jointly
surjective families as covers. A *condensed ring* is a sheaf of
rings on $*_{\mathrm{pro\acute et}}$. A topological ring $V$ defines a condensed ring
$\underline V$, whose sections over $S$ are the continuous maps $S\to V$.
This is a sheaf because a surjection of profinite sets is a quotient map.

Fix an algebraic closure $\overline{\mathbf Q}_\ell$ of $\Ql$. Throughout, $E$ denotes a
finite extension of $\Ql$ inside $\overline{\mathbf Q}_\ell$, with ring of integers
$\mathcal O_E$ and uniformizer $\pi_E$. The $\ell$-adic topologies define
condensed rings $\underline{\mathcal O_E}$ and $\underline E$. For
$\overline{\mathbf Q}_\ell$ we take the filtered colimit of the finite
coefficient fields. Explicitly, using the valuation topology on $\overline{\mathbf Q}_\ell$,
we put

$$
\underline{\overline{\mathbf Q}_\ell}(S)=
 \{a:S\to\overline{\mathbf Q}_\ell\text{ continuous}:a(S)\subset E\text{ for some finite }E/\Ql\}
 =\varinjlim_E\underline E(S).
$$

This is already a sheaf, because a cover of a profinite set can be refined by a
finite one, and finitely many finite extensions of $\Ql$ lie in a common
one. Since
filtered colimits of sheaves on $*_{\mathrm{pro\acute et}}$ are computed sectionwise,
$\underline{\overline{\mathbf Q}_\ell}=\varinjlim_E\underline E$ as condensed rings.

This condensed ring is smaller than $\underline V$ for $V=\overline{\mathbf Q}_\ell$ with the valuation
topology. Indeed, algebraic numbers of unbounded degree can tend to $0$, and
such a sequence is a continuous map from a convergent sequence to $\overline{\mathbf Q}_\ell$
with image in no finite extension. We exclude these maps because we want
a theory over finite coefficient fields. With our choice, every
constructible $\overline{\mathbf Q}_\ell$-complex and every morphism between such complexes
descends to a finite $E$ (Lemma [sk-thm-sfb-qlbar-two-colimit]).

A profinite set $S$ defines a pro-étale scheme
$\operatorname{Spec}LC(S,\mathbf Z)$ over $\mathbf Z$, where
$LC(S,\mathbf Z)$ is the ring of locally constant functions. The functor
$S\mapsto\operatorname{Spec}LC(S,\mathbf Z)$ is continuous and preserves
finite limits, as one checks on finite quotients of $S$. Hence it induces a
morphism of topoi $\Sh((\operatorname{Spec}\mathbf Z)_{\mathrm{pro\acute et}})\to
\Sh(*_{\mathrm{pro\acute et}})$ ([Stacks, Tag 00X6](https://stacks.math.columbia.edu/tag/00X6)). Composing with the structure morphism of
$X$, we obtain

$$
p_X:\Sh(X_{\mathrm{pro\acute et}})\longrightarrow\Sh(*_{\mathrm{pro\acute et}}),
$$

and for a condensed ring $\Lambda$ we write $\Lambda_X=p_X^*\Lambda$.
For a morphism $f:X\to Y$ we have $p_Y\circ f=p_X$, and hence a canonical
isomorphism $f^{-1}\Lambda_Y\simeq\Lambda_X$, compatible with identities
and composition. Likewise, a morphism $\Lambda\to\Lambda'$ of condensed
rings pulls back to $\Lambda_X\to\Lambda'_X$, which defines extension of
scalars $\Lambda'_X\otimes_{\Lambda_X}-$ from $\Lambda_X$-modules to
$\Lambda'_X$-modules on $X_{\mathrm{pro\acute et}}$. Thus both pullback along morphisms
and change of coefficients are obtained from $p_X^*$.

The next lemma identifies these rings with the completed coefficient
rings of classical $\ell$-adic cohomology.
