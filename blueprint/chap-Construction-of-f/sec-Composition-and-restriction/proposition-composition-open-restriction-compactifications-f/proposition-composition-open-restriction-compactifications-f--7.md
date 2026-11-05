+++
id = "proposition-composition-open-restriction-compactifications-f--7"
kind = "proposition"
title = "Local computation on the source"
order = 530008
aliases = ["bp-r161-7"]
lean = []
uses = ["proposition-composition-open-restriction-compactifications-f--1", "proposition-composition-open-restriction-compactifications-f--4"]
+++
The mainline bypasses a separate gluing statement for $f^!$ on open
coverings of $X$ and uses restriction comparisons on individual opens.

For a finite commutative ring $\Lambda$, let $j:U\to X$ be a
quasi-compact open immersion, and let $f:X\to Y$. Suppose that $j$, $f$,
and $fj$ admit compactifications and that $fj$ is quasi-compact.
The comparisons in
[proposition-composition-open-restriction-compactifications-f--1] and
[proposition-composition-open-restriction-compactifications-f--4] give
$$
j^*f^!\simeq j^!f^!\simeq(fj)^!.
$$
In the proofs of preservation of constructibility and Tor amplitude,
Lean forms these isomorphisms on each chart and then checks the required
properties on an open covering. For bounded constructible $\Qbarl$-complexes
in the shared context, the specified composition and open-immersion
comparisons give the same restriction formula.
