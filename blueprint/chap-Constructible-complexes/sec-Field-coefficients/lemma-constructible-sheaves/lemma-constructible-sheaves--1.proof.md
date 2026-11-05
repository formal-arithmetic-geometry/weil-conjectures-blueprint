+++
kind = "proof"
of = "lemma-constructible-sheaves--1"
order = 268010
uses = ["proposition-topos-functoriality", "lemma-constructible-sheaves--2", "lemma-constructible-sheaves--8"]
+++
Refine the stratifications of $F$ and $G$ by taking fibre products of
strata. Restriction is exact, so it suffices to prove the assertion on a
stratum where both sheaves are locally finitely presented. By
[lemma-constructible-sheaves--8] they are locally free of finite rank.

First the cokernel $C$ of $f$ is locally finitely presented, by
[lemma-constructible-sheaves--2] and its local presentation argument.
Thus $C$ is locally free. An epimorphism onto a finite free module splits
after a further cover: lift its finitely many basis sections. Apply this
to $G\to C$. Its kernel, the image $I$ of $f$, is locally finitely
presented, since a direct summand of a finite free module has a finite
presentation. Hence $I$ is locally free as well. Applying the same
argument to $F\to I$ makes its kernel locally finitely presented.
This kernel is $\ker f$, and [lemma-constructible-sheaves--8] makes it
lisse on the stratum. The common stratification therefore proves
constructibility.
