+++
id = "lemma-kunneth-formula-compact-supports--1"
kind = "lemma"
title = "Composition of compactly supported direct images"
name_showing = false
order = 1222001
aliases = ["bp-r377-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl"]
uses = ["proposition-construction-independence-rf-shriek"]
+++
Lean's Fourier-vanishing argument bypasses the Künneth composite; the
composition, base-change and projection isomorphisms used in the
calculation are recorded separately in these details.

Let $k$ be a field of characteristic $p>0$, let $\ell$ be a prime
different from $p$, and put $E=\overline{\mathbf Q}_\ell$. For morphisms
$u:Z\to X$ and $f:X\to S$ of separated schemes of finite type over $k$,
there is a natural isomorphism on bounded constructible $E$-complexes

$$
R(f\circ u)_!\simeq Rf_!Ru_!.
$$

In particular, with $u=p_1$ and $h=f\circ p_1$, it identifies
$Rh_!(p_1^*K\otimes p_2^*L)$ with
$Rf_!Rp_{1!}(p_1^*K\otimes p_2^*L)$.
