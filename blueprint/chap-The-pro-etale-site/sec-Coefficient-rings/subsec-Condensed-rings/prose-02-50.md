+++
id = "prose-02-50"
kind = "hidden"
title = "Condensed rings (2)"
order = 175
+++
The étale topos of $\Omega$ is the topos of sets, whereas by the
proposition its pro-étale topos is the topos of condensed sets. The final
object of $*_{\mathrm{pro}\acute{e}t}$ is weakly contractible, so taking global sections is
exact. However, a condensed sheaf is not determined by its global sections.
For classical sheaves geometric stalks still suffice, whereas a general sheaf of
modules on the pro-étale site has to be evaluated on all
weakly contractible affines
(Corollary [corollary-evaluation-weakly-contractible-objects]). For example, the
completed coefficient sheaf $\mathbf Z_{\ell,X}$ of
Example [example-coefficient-sheaf-outside-classical-part] is of this
general kind: its sections on a profinite set $S$ are all continuous
functions $S\to\mathbf Z_\ell$.

Fix an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$. Throughout, $E$ denotes a
finite extension of $\mathbf Q_\ell$ inside $\overline{\mathbf Q}_\ell$, with ring of integers
$\mathcal O_E$ and uniformizer $\pi_E$. For $\mathcal O_E$ and $E$ the $\ell$-adic topologies define condensed rings
$\underline{\mathcal O_E}$ and $\underline E$. For $\overline{\mathbf Q}_\ell$, however, the
topology causes a problem. To see why, recall that classically a $\overline{\mathbf Q}_\ell$-sheaf is an $E$-sheaf for
some finite $E$ with scalars extended, and all arguments with lattices and
reduction modulo $\pi_E$ take place over that $E$. They cannot be made over
$\overline{\mathbf Q}_\ell$ itself, because $\overline{\mathbf Q}_\ell$ is not complete and its valuation ring is not
a discrete valuation ring. But the sheaf of all continuous maps to $\overline{\mathbf Q}_\ell$
has sections that are defined over no finite $E$ (see below), so it would
lose this reduction. To keep it available, we take instead the filtered
colimit over the finite coefficient fields.
Using the valuation topology on $\overline{\mathbf Q}_\ell$, we put

$$
\underline{\overline{\mathbf Q}_\ell}(S)=
\{a:S\to\overline{\mathbf Q}_\ell\text{ continuous}:a(S)\subset E\text{ for some finite }E/\mathbf Q_\ell\}
=\varinjlim_E\underline E(S).
$$

This is already a sheaf, because a cover of a profinite set can be refined by a
finite one, and finitely many finite extensions of $\mathbf Q_\ell$ lie in a common
one. Since
filtered colimits of sheaves on $*_{\mathrm{pro}\acute{e}t}$ are computed sectionwise,
$\underline{\overline{\mathbf Q}_\ell}=\varinjlim_E\underline E$ as condensed rings.

This condensed ring is smaller than $\underline V$ for $V=\overline{\mathbf Q}_\ell$ with the valuation
topology. Indeed, algebraic numbers of unbounded degree can tend to $0$.
Such a sequence is a continuous map from a convergent sequence to $\overline{\mathbf Q}_\ell$
with image in no finite extension. With our choice,
Lemma [lemma-descent-finite-coefficient-field] shows that every
constructible $\overline{\mathbf Q}_\ell$-complex and every morphism between such complexes
descends to a finite $E$.
