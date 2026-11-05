+++
id = "prose-03-07"
kind = "hidden"
title = "Integral constructible complexes (1)"
order = 226
+++
Constructibility over $\mathcal O_E$ is defined by a local condition, but in
practice we know a complex $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ through
its reductions
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$ of
Definition [definition-derived-adic-completeness]. The criterion below says that
$K$ is constructible exactly when it is derived complete and $K_1$ is
constructible. Write $\mathbf F_E=\mathcal O_E/\pi_E$ for the residue
field, so that $K_1\in D(X_{\mathrm{pro}\acute{e}t},\mathbf F_E)$.

To prove the criterion we must produce, on each stratum, one complex of
finite free $\mathcal O_E$-modules that is locally a model for all the
$K_n$ at once. Each $K_n$ separately is easy to control: its bounds and
its stratification are inherited from $K_1$ by dévissage along the
powers of $\pi_E$, and on a stratum it is locally isomorphic to a
constant perfect complex. The difficulty is that these local isomorphisms
are chosen independently at each level, so they have to be made
compatible before we pass to the limit. On a weakly contractible cover
we do this by a Mittag–Leffler argument, which needs a uniform
rate. Such a rate exists because a bounded complex of finite free modules over the
discrete valuation ring $\mathcal O_E$ has finitely generated
cohomology, and the torsion of this cohomology is killed by a fixed power of
$\pi_E$.
Throughout, we use the étale site only at the finite levels, through
Theorem [theorem-comparison-constructible-sheaves].
