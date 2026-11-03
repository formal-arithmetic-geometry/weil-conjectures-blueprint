+++
kind  = "proof"
of    = "lem-sc-ample-tensor"
uses = ["lem-chow-segre"]
+++
*Reference: Stacks Project, Properties of Schemes, Lemma
28.27.5, [Tag 0890](https://stacks.math.columbia.edu/tag/0890).*

**Very ample modules.** The tensor product of two very ample modules is very
ample: if $\mathcal V\cong i^*\mathcal O(1)$ and
$\mathcal W\cong j^*\mathcal O(1)$ for closed immersions
$i\colon X\to\mathbf P^{n}_k$ and $j\colon X\to\mathbf P^{m}_k$ over $k$, then
by [lem-chow-segre] (with $S=\Spec k$) the composite of
$(i,j)\colon X\to\mathbf P^{n}_k\times_k\mathbf P^{m}_k$ with the Segre
embedding is a closed immersion $X\to\mathbf P^{n\times m}_k$ over $k$ along
which $\mathcal O(1)$ pulls back to $\mathcal V\otimes\mathcal W$. Hence,
by induction ($\mathcal V^{\otimes1}\cong\mathcal V$ and
$\mathcal V^{\otimes(r+2)}\cong\mathcal V\otimes\mathcal V^{\otimes(r+1)}$),
every positive tensor power of a very ample module is very ample.

**Ample modules.** Choose $a,b\geq1$ with $\mathcal L^{\otimes a}$ and
$\mathcal M^{\otimes b}$ very ample. Then
$\mathcal L^{\otimes ab}\cong(\mathcal L^{\otimes a})^{\otimes b}$ and
$\mathcal M^{\otimes ab}\cong(\mathcal M^{\otimes b})^{\otimes a}$ are very
ample, and so is
$(\mathcal L\otimes\mathcal M)^{\otimes ab}\cong\mathcal L^{\otimes ab}\otimes\mathcal M^{\otimes ab}$.
As $\mathcal L\otimes\mathcal M$ is invertible and $ab\geq1$, it is ample.

**The abelian variety case.** Let $f\colon A\to\Spec k$ be the structure
morphism. The restriction of an ample module along a closed immersion
$g\colon Z\to A$ is ample with respect to $f\circ g$: if
$\mathcal L^{\otimes r}\cong i^*\mathcal O(1)$ for a closed immersion $i$,
then $(g^*\mathcal L)^{\otimes r}\cong g^*(\mathcal L^{\otimes r})\cong(i\circ g)^*\mathcal O(1)$
and $i\circ g$ is a closed immersion. The inversion $[-1]$ is an automorphism
of $A$ over $k$, in particular a closed immersion with $f\circ[-1]=f$, so
$[-1]^*\mathcal L$ is ample, and $\mathcal L\otimes[-1]^*\mathcal L$ is ample
by the first part. Finally, for any invertible $\mathcal L$, since
pullback commutes with tensor products and $[-1]\circ[-1]=\mathrm{id}_A$,

$$
[-1]^*(\mathcal L\otimes[-1]^*\mathcal L)\cong[-1]^*\mathcal L\otimes[-1]^*[-1]^*\mathcal L
\cong[-1]^*\mathcal L\otimes\mathcal L\cong\mathcal L\otimes[-1]^*\mathcal L .
$$
