+++
id = "sbc-lem-integral-etale-direct-image-exact"
kind = "lemma"
title = "Étale direct image is exact for integral morphisms"
order = 5127
lean = ["AlgebraicGeometry.Etale.pushforward_exact_of_isIntegralHom"]
+++
Let $\pi:T'\to T$ be an integral morphism of schemes. Then the direct image
$\pi_*:\Ab(T'_{\Et})\to\Ab(T_{\Et})$ is exact; consequently $R^q\pi_*=0$ for
$q>0$ and $R\pi_*=\pi_*$ on $\Dplus(T'_{\Et})$. If $\pi$ is finite, this is
the finite-direct-image exactness lemma of the proper-base-change chapter.

(*Stacks Project, Étale Cohomology, Lemma 59.43.5, [Tag
04C2](https://stacks.math.columbia.edu/tag/04C2).*)

## Proof

This is the recorded classical input named in the statement, Stacks Project,
Étale Cohomology, Lemma 59.43.5 ([Tag
04C2](https://stacks.math.columbia.edu/tag/04C2)): for an integral morphism
the direct image of étale abelian sheaves is exact, so the higher direct
images vanish and the derived direct image is the underived one on
bounded-below complexes. The finite case is the corresponding lemma of the
proper-base-change chapter; no separate proof of the general case is given.

Unresolved dependencies: lem:weil-pbc-finite-direct-image-exact, def:weil-pbc-scheme-conventions, def:weil-pbc-direct-image
