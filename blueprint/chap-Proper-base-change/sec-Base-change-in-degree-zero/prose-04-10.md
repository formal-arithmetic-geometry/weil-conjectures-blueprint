+++
id = "prose-04-10"
kind = "hidden"
title = "Base change in degree zero (2)"
order = 329
+++
The theorem is [Stacks, [0A0C](https://stacks.math.columbia.edu/tag/0A0C)]. At heart it is a statement about
connectedness: every irreducible closed subset of a scheme proper
over a henselian pair meets the closed fibre in a nonempty connected subset.
This follows from Stein factorization and the
connectedness properties of henselian pairs [Stacks, [0A0B](https://stacks.math.columbia.edu/tag/0A0B)]; over a general
affine base, Stein factorization only produces an algebra integral over
$R$, but that suffices. A topological argument on spectral spaces then turns
connectedness into bijectivity of restriction for Zariski sheaves.

Passing to étale sheaves uses finite covers, which are harmless here: a
finite cover of $Z$ remains proper over $R$, so the connectedness statement also holds after
every finite cover. Given an étale covering of $Z$, we choose a finite surjection
$Z'\to Z$ that factors through the covering Zariski locally on $Z'$, and
sections then descend along $Z'\times_ZZ'\rightrightarrows Z'$
[Stacks, [09ZF](https://stacks.math.columbia.edu/tag/09ZF)].
