+++
id = "def-sfb-preserves-kflat-quasi-iso"
kind = "definition"
title = "K-flat complexes; functors preserving K-flat quasi-isomorphisms"
order = 1556
uses = ["def-weil-abstract-derived-category"]
lean = ["CategoryTheory.Functor.PreservesKFlatQuasiIso"]
+++
Let $\mathcal C$ be a monoidal abelian category whose tensor product is additive in each
variable. Complexes are tensored by totalizing the termwise tensor product. A complex $P$
is *K-flat* if $P\otimes-$ and $-\otimes P$ send quasi-isomorphisms to
quasi-isomorphisms. An additive functor $F\colon\mathcal C\to\mathcal D$ to an abelian
category *preserves K-flat quasi-isomorphisms* if $F(s)$ is a quasi-isomorphism for every
quasi-isomorphism $s\colon P\to P'$ between K-flat complexes. Every exact functor does.
