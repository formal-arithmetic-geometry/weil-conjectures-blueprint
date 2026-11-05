+++
kind = "proof"
of = "lemma-global-lattice-normal-scheme"
order = 1078
uses = ["definition-small-pro-etale-site", "lemma-geometric-coverings-normal-scheme"]
+++
The scheme of lattices satisfies the valuative condition of
Lemma [lemma-geometric-coverings-normal-scheme], so it has a finite étale
surjective component, and we push the universal lattice of this component down to
$X$ by the trace.

We may assume that $L$ has positive rank $r$. Let
$Y$ be the $X$-scheme representing lattices in $L$
(Lemma [lemma-lattices-lisse-e-sheaves]), a separated surjective étale
$X$-scheme with a universal lattice. Pro-étale locally on $X$, the scheme $Y$ is constant: the proof of that lemma shows that, for a
quasi-compact pro-étale covering $U\to X$, with $U$ a pro-étale
affine on which $L$ is free,

$$
Y\times_XU\simeq
\coprod_{\GL_r(E)/\GL_r(\mathcal O_E)} U,
$$

where $\GL_r(E)/\GL_r(\mathcal O_E)$ is the
discrete set of lattices in $E^r$.

We check the valuative property of
Lemma [lemma-geometric-coverings-normal-scheme]. Let $V$ be a valuation ring
with fraction field $K$, and suppose given $\operatorname{Spec}V\to X$
and a lift $\xi:\operatorname{Spec}K\to Y$. Since $U\to X$ is flat
and surjective, there are a local extension of valuation rings
$V\to V'$ and a compatible map $\operatorname{Spec}V'\to U$
[Stacks, [089F](https://stacks.math.columbia.edu/tag/089F)]. This extension is faithfully flat, because it is local
and $V'$ is torsion-free, hence flat, over $V$ [Stacks, [0539](https://stacks.math.columbia.edu/tag/0539)]. By the
displayed description of $Y\times_XU$, the
pullback of $\xi$ to the spectrum of the fraction field of $V'$ picks out a
lattice in $E^r$, and the constant
section with this value extends it to a map
$\xi':\operatorname{Spec}V'\to Y$.

We descend $\xi'$ by fpqc descent, which needs its two pullbacks to
$R=V'\otimes_VV'$ to agree. Over the domain $V'\otimes_VK$, the maps $\xi'$
and $\xi$ agree at the generic point, hence everywhere by separatedness,
so the two pullbacks agree after base change to $K$. This suffices: since $R$ is flat
over $V$, the map $R\to R\otimes_VK$ is injective, and therefore
$\operatorname{Spec}(R\otimes_VK)$ is schematically dense in
$\operatorname{Spec}R$. As the equalizer of the two pullbacks is closed
by separatedness, they agree on $\operatorname{Spec}R$. Descent then gives a lift
$\operatorname{Spec}V\to Y$ restricting to $\xi$, which is unique
by separatedness and the density of $\operatorname{Spec}K$.

By Lemma [lemma-geometric-coverings-normal-scheme], every nonempty component
$p_1:Y_1\to X$ of $Y$ is therefore finite étale and surjective. We fix one, and
let $N\subseteq p_1^*L$ be its universal lattice.
As in Lemma [lemma-lattices-after-finite-stratification], set

$$
M=\operatorname{im}\bigl(
p_{1*}N\longrightarrow p_{1*}p_1^*L
\xrightarrow{\operatorname{Tr}}L\bigr).
$$

The sheaf $M$ is lisse with $M[1/\ell]=L$. Indeed, after the cover is
split into $d$ sheets, this image is the sum of $d$ lattices. On a
common pro-étale refinement these become constant lattices in $E^r$, and their sum is a
finite free $\mathcal O_E$-lattice spanning $E^r$.

By Theorem [theorem-comparison-constructible-sheaves] the finite reductions
$M_n=M/\pi_E^nM$ are finite locally constant étale sheaves, and
$M=\varprojlim_nM_n$ by
Lemma [lemma-comparison-completed-coefficients], which we may check where
$M$ is free.
