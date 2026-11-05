+++
id = "lemma-extension-scalars-preserves-dctf--1"
kind = "lemma"
title = "Exact extension of scalars preserves bounded constructible complexes"
name_showing = false
order = 633001
aliases = ["bp-r192-1"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_leftDerivedExtendScalars_obj"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "proposition-topos-functoriality"]
+++
Lean bypasses the general finite-Tor statement above and uses the following
result for exact extension of scalars.

Let $X$ be a scheme and let $\varphi:R\to S$ be a morphism of commutative
ring objects in abelian sheaves on $X_{\mathrm{pro}\acute{e}t}$. Suppose that
extension of scalars $S\otimes_R-$ preserves finite limits. Then its left
derived functor sends bounded constructible complexes of $R$-modules to
bounded constructible complexes of $S$-modules.

Here a complex is bounded constructible if its cohomology vanishes outside
a finite interval and each cohomology sheaf admits a finite stratification
of $X$ by constructible locally closed subschemes on which it is pro-étale
locally finitely presented. A local finite presentation is a cokernel of a
map between finite free modules over the restricted ring sheaf; the matrix
entries need not come from a fixed ring of constant coefficients. No finite
Tor amplitude is assumed or asserted.
