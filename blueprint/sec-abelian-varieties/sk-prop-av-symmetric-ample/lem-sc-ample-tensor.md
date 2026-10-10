+++
id = "lem-sc-ample-tensor"
kind = "lemma"
title = "Tensor products of ample modules"
lean = ["AlgebraicGeometry.IsAmple.tensorObj", "AlgebraicGeometry.IsAbelianVariety.isAmple_symmetrisation", "AlgebraicGeometry.IsAbelianVariety.nonempty_iso_overPullback_inv_symmetrisation"]
order = 478
uses = ["def-sc-abelian-variety", "def-sc-ample", "lem-chow-segre"]
+++
Let $X$ be a scheme over a field $k$ and let $\mathcal L$ and
$\mathcal M$ be ample invertible
$\mathcal O_X$-modules. Then $\mathcal L\otimes\mathcal M$ is
ample. In particular, for an
abelian variety $A$ and an
invertible module $\mathcal L$ on $A$, the module
$\mathcal L\otimes[-1]^*\mathcal L$ satisfies
$[-1]^*(\mathcal L\otimes[-1]^*\mathcal L)\cong\mathcal L\otimes [-1]^*\mathcal L$,
and it is ample if $\mathcal L$ is ample.

## Proof

*Reference: Stacks Project, Properties of Schemes, Lemma
28.27.5, [Tag 0890](https://stacks.math.columbia.edu/tag/0890).*
Choose $a,b\geq1$ with $\mathcal L^{\otimes a}$ and
$\mathcal M^{\otimes b}$ very ample. The tensor product of two very
ample modules is very ample: if $\mathcal V\cong i^*\mathcal O(1)$ and
$\mathcal W\cong j^*\mathcal O(1)$ for closed immersions $i,j$ into
projective spaces over $k$, then $(i,j)$ is a closed immersion into
their product (it is the graph-type morphism
$X\to X\times_kX\to\mathbf P^N_k\times_k\mathbf P^M_k$, the diagonal
being a closed immersion because $X$, admitting the closed immersion
$i$ into a projective space, is separated over $k$), and $\mathcal V\otimes\mathcal W$ is the
pullback of $\mathcal O(1)\boxtimes\mathcal O(1)$ along it, which is
very ample by [lem-chow-segre]. By induction, positive tensor powers
of a very ample module are very ample. Hence
$\mathcal L^{\otimes ab}=(\mathcal L^{\otimes a})^{\otimes b}$ and
$\mathcal M^{\otimes ab}=(\mathcal M^{\otimes b})^{\otimes a}$ are very
ample, and so is
$(\mathcal L\otimes\mathcal M)^{\otimes ab}\cong\mathcal L^{\otimes ab}\otimes\mathcal M^{\otimes ab}$.
Hence $\mathcal L\otimes\mathcal M$ is ample. For the second part,
$[-1]$ is an automorphism of $A$, so $[-1]^*\mathcal L$ is
ample and $[-1]^*[-1]^*\mathcal L\cong\mathcal L$; therefore
$[-1]^*(\mathcal L\otimes[-1]^*\mathcal L)\cong[-1]^*\mathcal L\otimes\mathcal L\cong\mathcal L\otimes[-1]^*\mathcal L$.
