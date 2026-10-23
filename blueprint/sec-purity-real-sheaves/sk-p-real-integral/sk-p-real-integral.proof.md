+++
kind  = "proof"
of    = "sk-p-real-integral"
+++
We may assume that $\mathcal F$ has positive rank $r$. Let
$Y=\operatorname{Lat}(\mathcal F)$ be the lattice scheme of
[sk-lem-stratified-lattice]. On a trivializing pro-étale
object its fibre is the discrete set

$$
 S=\operatorname{GL}_r(E)/\operatorname{GL}_r(\mathcal O_E).
$$

The action of a transition matrix on a fixed lattice is locally
constant, since the stabilizer of the lattice is open. To see this in
terms of matrices, note that on a quasi-compact affine object the
entries of a matrix and of its inverse have a common denominator. After
multiplying by it, their reductions modulo a sufficiently high power of
$\pi_E$ determine the image of the fixed lattice, and these reductions
are locally constant functions with finitely many values.

Choose a quasi-compact faithfully flat trivializing atlas $U\to X$
in the affine pro-étale basis. The transition permutations define a
descent datum on $\coprod_S U$. Over each affine of $U$, this scheme
is ind-quasi-affine, being the union of its finite affine subunions,
and hence fpqc descent is effective
([Stacks `0APK`](https://stacks.math.columbia.edu/tag/0APK)). Since
separatedness and étaleness descend
([Stacks `02KU`](https://stacks.math.columbia.edu/tag/02KU),
[Stacks `02VN`](https://stacks.math.columbia.edu/tag/02VN)), we see that $Y$
is a separated surjective étale $X$-scheme with a universal lisse lattice and

$$
 Y\times_XU\simeq\coprod_S U.
$$

We check the valuative property of
[sk-lem-wrp-normal-geometric-cover]. Let $V$ be a valuation ring
with fraction field $K$, and suppose given $\operatorname{Spec}V\to X$
and a lift $\xi:\operatorname{Spec}K\to Y$. Since $U\to X$ is flat
and surjective, there are a local extension of valuation rings
$V\to V'$ and a compatible map $\operatorname{Spec}V'\to U$
([Stacks `089F`](https://stacks.math.columbia.edu/tag/089F)). The extension is
faithfully flat, because it is local and $V'$ is torsion-free, hence flat,
over $V$ ([Stacks `0539`](https://stacks.math.columbia.edu/tag/0539)). Put
$K'=\operatorname{Frac}(V')$. The pullback of $\xi$ to
$\operatorname{Spec}K'$ picks out an element of $S$, and the constant
section with this value extends it to a map
$\xi':\operatorname{Spec}V'\to Y$.

To descend $\xi'$, we first compare it with $\xi$ over
$V'\otimes_VK$. This ring is a domain and the two maps agree at its
generic point, so they are equal by separatedness. It follows that
the two pullbacks of $\xi'$ to $R=V'\otimes_VV'$ agree after base
change to $K$. Since $R$ is flat over $V$, the map $R\to R\otimes_VK$
is injective, so that $\operatorname{Spec}(R\otimes_VK)$ is
schematically dense in $\operatorname{Spec}R$. The equalizer of the
two pullbacks is closed by separatedness, and hence they agree on
$\operatorname{Spec}R$. By fpqc descent we obtain a lift
$\operatorname{Spec}V\to Y$ restricting to $\xi$. The lift is unique
by separatedness and the density of $\operatorname{Spec}K$.

By [sk-lem-wrp-normal-geometric-cover], every nonempty component
$p_1:Y_1\to X$ of $Y$ is finite étale and surjective. Fix one, and
let $\mathcal N\subseteq p_1^*\mathcal F$ be its universal lattice.
As in [sk-lem-stratified-lattice], set

$$
 \mathcal M=\operatorname{im}\bigl(
 p_{1*}\mathcal N\longrightarrow p_{1*}p_1^*\mathcal F
       \xrightarrow{\operatorname{Tr}}\mathcal F\bigr).
$$

After the cover is split into $d$ sheets, this image is the sum of
$d$ lattices. On a common pro-étale refinement their classes in $S$
are constant, and their sum is a finite free $\mathcal O_E$-lattice
spanning $E^r$. Hence $\mathcal M$ is lisse and
$\mathcal M[1/\ell]=\mathcal F$.

Consider the finite reductions
$\mathcal M_n=\mathcal M/\pi_E^n\mathcal M$. They are finite locally
constant étale sheaves by [sk-thm-pe-constructible-comparison], and
$\mathcal M=\varprojlim_n\mathcal M_n$ by [sk-prop-sfb-qlbar-colimit-x],
which we may check where $\mathcal M$ is free. Their fibres define a
continuous action of $\pi_1(X,\bar x)$ on the finite free completed fibre

$$
 M_{\bar x}:=\varprojlim_n(\mathcal M_n)_{\bar x}.
$$

The rational fibre is $M_{\bar x}\otimes_{\mathcal O_E}E$. Thus we
apply the fibre functor of finite covers to the finite reductions
first, and complete afterwards.

We claim that this fibre functor is fully faithful. A morphism of
lisse rational sheaves has a uniform denominator relative to their
lattices, as one sees by bounding the finitely many matrix entries on
a quasi-compact pro-étale atlas trivializing both lattices. An
integral multiple of the morphism is then determined by its finite
reductions. Under the fibre functor these reductions correspond
exactly to the equivariant maps between the reductions of the
completed fibres. Conversely, an equivariant rational map between the
fibres has a denominator with respect to the two finite free fibre
lattices. Its integral multiple defines a compatible system of maps on
the finite reductions, hence a map of their inverse limits. Applied to
the identity with two choices of lattice, the same argument identifies
the two resulting rational fibre representations.

It remains to prove essential surjectivity. A continuous
representation of the profinite group $\pi_1(X,\bar x)$ on $E^r$ has
compact image. Hence the $\mathcal O_E$-span of the translates of a
lattice is bounded and contains that lattice, so it is a stable finite
free lattice, as $\mathcal O_E$ is noetherian. Its reductions define
compatible finite locally constant étale sheaves. These become
constant simultaneously on the surjective pro-étale cover obtained
as the inverse limit of the finite étale covers corresponding to
their kernels. Therefore their inverse limit is lisse over
$\mathcal O_E$, and its rationalization is lisse over $E$. This
construction is inverse to the fibre functor.

*Complement.* For the curve statement, the geometric representation of a
lisse Weil sheaf is continuous and defined over a finite $E$; the
$\mathcal O_E$-span of the translates of a lattice under the compact group
$\rho(\pi_1(U))$ is a stable lattice, and its reductions are finite sets, so
the images of $\pi_1(U)$ in their automorphisms are finite
([p-real-integral]).
