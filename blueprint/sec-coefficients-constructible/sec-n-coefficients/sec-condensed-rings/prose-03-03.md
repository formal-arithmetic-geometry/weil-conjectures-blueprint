+++
id = "prose-03-03"
kind = "hidden"
title = "Condensed rings"
order = 130
+++
The obvious choice of coefficients would be the constant sheaf with value
the abstract ring $\Zl$. It is the wrong one: as computed at the start of
Section [sec-proetale-coefficients], the constant sheaf with value
the discrete group $\Zl$ on $\operatorname{Spec}\mathbf F_q$ has $H^1=0$, whereas
the answer should be $\Zl$, because a constant sheaf only remembers the
underlying group and not the topology. We therefore have to say what a
coefficient ring is on a geometric point in a way that retains its
topology. By Proposition [sk-prop-pe-condensed-point] the pro-étale site of
a separably closed field is the site of profinite sets, so a coefficient
ring must at least be a sheaf of rings on profinite sets, that is, a
condensed ring. The continuous maps from profinite sets into $\Zl$ form such a
sheaf, and it remembers the topology; with it, $H^1$ of $\mathbf F_q$ becomes
$\Zl$ (Example [sk-rem-pe-finite-field-adic]).

Let $*_{\mathrm{pro}\acute{e}t}$ be the site of profinite sets, with finite jointly
surjective families as covers. A *condensed ring* is a sheaf of
rings on $*_{\mathrm{pro}\acute{e}t}$. A topological ring $V$ defines a condensed ring
$\underline V$, whose sections over $S$ are the continuous maps $S\to V$.
This is a sheaf because a surjection of profinite sets is a quotient map.

Fix an algebraic closure $\overline{\mathbf Q}_\ell$ of $\Ql$. Throughout, $E$ denotes a
finite extension of $\Ql$ inside $\overline{\mathbf Q}_\ell$, with ring of integers
$\mathcal O_E$ and uniformizer $\pi_E$. The $\ell$-adic topologies define
condensed rings $\underline{\mathcal O_E}$ and $\underline E$. For
$\overline{\mathbf Q}_\ell$ the topology causes a problem. Classically a $\overline{\mathbf Q}_\ell$-sheaf is an
$E$-sheaf for some finite $E$ with scalars extended, and all arguments
with lattices and reduction modulo $\pi_E$ take place over that $E$.
The field $\overline{\mathbf Q}_\ell$ is not complete, and its valuation ring is not a
discrete valuation ring, so these arguments cannot be made over $\overline{\mathbf Q}_\ell$
itself. The sheaf of all continuous maps to $\overline{\mathbf Q}_\ell$ has sections that are
defined over no finite $E$ (see below), and to keep the reduction to a
finite $E$ available we take instead the filtered colimit of the finite
coefficient fields. Explicitly, using the valuation topology
on $\overline{\mathbf Q}_\ell$, we put

$$
\underline{\overline{\mathbf Q}_\ell}(S)=
\{a:S\to \overline{\mathbf Q}_\ell\text{ continuous}:a(S)\subset E\text{ for some finite }E/\Ql\}
=\varinjlim_E\underline E(S).
$$

This is already a sheaf, because a cover of a profinite set can be refined by a
finite one, and finitely many finite extensions of $\Ql$ lie in a common
one. Since
filtered colimits of sheaves on $*_{\mathrm{pro}\acute{e}t}$ are computed sectionwise,
$\underline{\overline{\mathbf Q}_\ell}=\varinjlim_E\underline E$ as condensed rings.

This condensed ring is smaller than $\underline V$ for $V=\overline{\mathbf Q}_\ell$ with the valuation
topology. Indeed, algebraic numbers of unbounded degree can tend to $0$, and
such a sequence is a continuous map from a convergent sequence to $\overline{\mathbf Q}_\ell$
with image in no finite extension. With our choice, every
constructible $\overline{\mathbf Q}_\ell$-complex and every morphism between such complexes
descends to a finite $E$ (Lemma [sk-thm-sfb-qlbar-two-colimit]).
