+++
id = "lemma-coherent-base-change-invertible-sheaves--2"
kind = "lemma"
title = "Restricting the cohomology comparison after base change"
name_showing = false
order = 1530002
aliases = ["bp-r477-2"]
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_restrict_higherDirectImage_iso_homology"]
uses = ["lemma-coherent-base-change-invertible-sheaves--1"]
+++
Lean bypasses the canonical derived base-change assertion and uses the
following comparison of cohomology sheaves.

Let $f:X\to T$ be a morphism, let $\mathcal F$ be an
$\mathcal O_X$-module, and let $U\subseteq T$ be open. Suppose a complex
$P^\bullet$ on $U$ has the cohomology comparisons after every base change
stated in [lemma-coherent-base-change-invertible-sheaves--1].
Let $a:T'\to T$ and let $f':X'\to T'$ and $b:X'\to X$ form a
cartesian square with $f$ and $a$. If $V\subseteq T'$ is open and
$a_V:V\to U$ satisfies $\iota_Ua_V=a\iota_V$, then, for every $q\geq0$,
there exists an isomorphism
$$
(R^qf'_*b^*\mathcal F)|_V\simeq
\mathcal H^q(a_V^*P^\bullet).
$$
Only the comparison property of $P^\bullet$ is assumed here; no
properness, flatness or finite-freeness hypothesis is needed for this step.
