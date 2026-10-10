+++
kind  = "proof"
of    = "lem-sc-ample-tensor"
+++
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
