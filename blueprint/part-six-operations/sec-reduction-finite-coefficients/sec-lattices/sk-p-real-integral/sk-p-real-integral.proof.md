+++
kind = "proof"
of = "sk-p-real-integral"
uses = ["sk-lem-lattice-atlas"]
+++
We may assume that $L$ has positive rank $r$. Let
$Y$ be the $X$-scheme representing lattices in $L$
(Lemma [sk-lem-lattice-atlas]), a separated surjective étale
$X$-scheme with a universal lattice. Its proof shows that, for a
quasi-compact pro-étale covering $U\to X$ in the affine
pro-étale basis on which $L$ is free,

$$
Y\times_XU\simeq
\coprod_{\GL_r(E)/\GL_r(\mathcal O_E)} U,
$$

where $\GL_r(E)/\GL_r(\mathcal O_E)$ is the
discrete set of lattices in $E^r$.

We check the valuative property of
Lemma [sk-lem-wrp-normal-geometric-cover]. Let $V$ be a valuation ring
with fraction field $K$, and suppose given $\operatorname{Spec}V\to X$
and a lift $\xi:\operatorname{Spec}K\to Y$. Since $U\to X$ is flat
and surjective, there are a local extension of valuation rings
$V\to V'$ and a compatible map $\operatorname{Spec}V'\to U$
[Stacks, Tag 089F](https://stacks.math.columbia.edu/tag/089F). The extension is faithfully flat, because it is local
and $V'$ is torsion-free, hence flat, over $V$ [Stacks, Tag 0539](https://stacks.math.columbia.edu/tag/0539). The
pullback of $\xi$ to the spectrum of the fraction field of $V'$ picks out a lattice in $E^r$, and the constant
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

By Lemma [sk-lem-wrp-normal-geometric-cover], every nonempty component
$p_1:Y_1\to X$ of $Y$ is finite étale and surjective. Fix one, and
let $N\subseteq p_1^*L$ be its universal lattice.
As in Lemma [sk-lem-stratified-lattice], set

$$
M=\operatorname{im}\bigl(
p_{1*}N\longrightarrow p_{1*}p_1^*L
\xrightarrow{\operatorname{Tr}}L\bigr).
$$

After the cover is split into $d$ sheets, this image is the sum of
$d$ lattices. On a common pro-étale refinement the lattices in $E^r$
they define are constant, and their sum is a finite free $\mathcal O_E$-lattice
spanning $E^r$. Hence $M$ is lisse and
$M[1/\ell]=L$.

Consider the finite reductions
$M_n=M/\pi_E^nM$. They are finite locally
constant étale sheaves by
Theorem [sk-thm-pe-constructible-comparison], and
$M=\varprojlim_nM_n$ by
Lemma [sk-prop-sfb-qlbar-colimit-x], which we may check where
$M$ is free. Their fibres define a continuous action of
$\pi_1(X,\bar x)$ on the finite free completed fibre

$$
M_{\bar x}:=\varprojlim_n(M_n)_{\bar x}.
$$

The rational fibre is $M_{\bar x}\otimes_{\mathcal O_E}E$. This is the
fibre functor of the proposition: the fibre functor of finite
covers is applied to the finite reductions, and the result is completed.

We claim that this fibre functor is fully faithful. The fact we use is
the Galois theory of finite étale covers of the connected scheme $X$:
taking the fibre at $\bar x$ is an equivalence between finite locally
constant sheaves on $X_{\acute{e}t}$ and finite sets with continuous
$\pi_1(X,\bar x)$-action, and it is compatible with module structures.
Let $M\subseteq L$ and $M'\subseteq L'$
be lattices in two lisse $E_X$-modules. A morphism
$\phi:L\to L'$ has a uniform denominator, that is,
$\pi_E^c\phi$ maps $M$ into $M'$ for some $c\geq0$, as
one sees by bounding the finitely many matrix entries on a quasi-compact
pro-étale covering trivializing both lattices. For faithfulness, if the
fibre of $\phi$ vanishes, then the fibres of all the reductions of
$\pi_E^c\phi$ vanish, so these reductions vanish by the Galois
correspondence, and hence $\pi_E^c\phi=0$ because
$M'=\varprojlim_nM'_n$. For fullness, an equivariant map
between the rational fibres has, after multiplication by some $\pi_E^c$,
image of $M_{\bar x}$ in $M'_{\bar x}$. Its reductions are equivariant maps
of finite fibres, hence come from compatible maps
$M_n\to M'_n$ by the Galois correspondence, and their
inverse limit is a map $M\to M'$ whose rationalization,
divided by $\pi_E^c$, has the given fibre.

The rational fibre representation does not depend on the choice of
lattice. If $M_1$ and $M_2$ are two lattices in
$L$, then by the uniform denominator applied to the identity
of $L$, the map $\pi_E^c\,\mathrm{id}_{L}$ sends
$M_1$ into $M_2$ for some $c\geq0$, and symmetrically.
On fibres these maps, divided by $\pi_E^c$, give mutually inverse
equivariant isomorphisms between the two rational fibres.

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
