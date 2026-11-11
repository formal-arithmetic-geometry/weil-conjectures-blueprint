+++
id = "proposition-lattices-representations-normal-scheme--1"
kind = "proposition"
title = "Lattices and representations on a normal scheme (1)"
name_showing = false
order = 1083001
aliases = ["bp-r332-1"]
lean = ["AlgebraicGeometry.ProEtale.exists_lisseMonodromy", "AlgebraicGeometry.ProEtale.exists_lisseMonodromy_of_isIntegrallyClosed_stalk"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1"]
+++
Let $X$ be a nonempty connected normal scheme of finite type over a
field, let $E/\mathbf Q_\ell$ be finite, and fix a geometric point $\bar x$. By
Lemma [lemma-global-lattice-normal-scheme], every lisse $E_X$-module $L$
contains a lisse $\mathcal O_{E,X}$-submodule $M$ with $M[1/\ell]=L$ and
$M\simeq\varprojlim_nM/\pi_E^nM$, whose reductions are finite locally
constant étale sheaves. The fibre functor at $\bar x$,
$L\mapsto\bigl(\varprojlim_n(M/\pi_E^nM)_{\bar x}\bigr)\otimes_{\mathcal O_E}E$,
does not depend on the choice of $M$ up to canonical isomorphism, and it
gives an equivalence between lisse $E_X$-modules and finite-dimensional
continuous $E$-representations of the ordinary profinite group
$\pi_1(X,\bar x)$.
