+++
kind  = "proof"
of    = "sk-p-real-integral"
+++
We reduce to a finite extension $E$ of $\Ql$, prove the statement for
lisse $E_X$-modules by means of a lattice, and pass back to $\Qlb$.

*Step 1: reduction to a finite $E$.* Let $L$ be a lisse
$\QbarX$-module. By [sk-lem-lisse-finite-descent], which
applies since $X$ is noetherian, hence quasi-compact and
quasi-separated, there are a finite extension $E/\Ql$ and a lisse
$E_X$-module $L_E$ with $L\simeq L_E\otimes_{E_X}\QbarX$. Indeed, $L$ is
free on a quasi-compact pro-étale covering, and the finitely many
entries of its transition matrices lie in a single $E_X$, because
$\QbarX=\varinjlim_EE_X$ and sections over quasi-compact objects commute
with filtered colimits. We call $L_E$ a *model* of $L$ over $E$.

*Step 2: the case of a finite $E$.* Now let $E/\Ql$ be finite and
let $L$ be a lisse $E_X$-module. We show that $L$ contains a lisse
$\mathcal O_{E,X}$-submodule $M$ with $M[1/\ell]=L$, whose finite
reductions are finite locally constant étale sheaves, with

$$
 M\simeq\varprojlim_nM/\pi_E^nM,
$$

and that the fibre functor
$L\mapsto\bigl(\varprojlim_n(M/\pi_E^nM)_{\bar x}\bigr)\otimes_{\mathcal O_E}E$
is an equivalence between lisse $E_X$-modules and finite-dimensional
continuous $E$-representations of $\pi_1(X,\bar x)$.

We may assume that $L$ has positive rank $r$. Let
$Y$ be the $X$-scheme representing lattices in $L$
([sk-lem-stratified-lattice]), a separated surjective étale
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
[sk-lem-wrp-normal-geometric-cover]. Let $V$ be a valuation ring
with fraction field $K$, and suppose given $\operatorname{Spec}V\to X$
and a lift $\xi:\operatorname{Spec}K\to Y$. Since $U\to X$ is flat
and surjective, there are a local extension of valuation rings
$V\to V'$ and a compatible map $\operatorname{Spec}V'\to U$
(Stacks [089F](https://stacks.math.columbia.edu/tag/089F)). The extension is faithfully flat, because it is local
and $V'$ is torsion-free, hence flat, over $V$ (Stacks [0539](https://stacks.math.columbia.edu/tag/0539)). The
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

By [sk-lem-wrp-normal-geometric-cover], every nonempty component
$p_1:Y_1\to X$ of $Y$ is finite étale and surjective. Fix one, and
let $N\subseteq p_1^*L$ be its universal lattice.
As in [sk-lem-stratified-lattice], set

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
[sk-thm-pe-constructible-comparison], and
$M=\varprojlim_nM_n$ by
[sk-prop-sfb-qlbar-colimit-x], which we may check where
$M$ is free. Their fibres define a continuous action of
$\pi_1(X,\bar x)$ on the finite free completed fibre

$$
 M_{\bar x}:=\varprojlim_n(M_n)_{\bar x}.
$$

The rational fibre is $M_{\bar x}\otimes_{\mathcal O_E}E$. This is the
fibre functor of Step 2: the fibre functor of finite
covers is applied to the finite reductions, and the result is completed.

We claim that this fibre functor is fully faithful. The fact we use is
the Galois theory of finite étale covers of the connected scheme $X$:
taking the fibre at $\bar x$ is an equivalence between finite locally
constant sheaves on $X_{\mathrm{ét}}$ and finite sets with continuous
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

*Step 3: back to $\Qlb$.* For a finite extension $E'/E$, the
lattice $M\otimes_{\mathcal O_E}\mathcal O_{E'}$ of $L\otimes_EE'$ has
completed fibre $M_{\bar x}\otimes_{\mathcal O_E}\mathcal O_{E'}$, since
$M_{\bar x}$ is finite free. Hence the fibre functor of Step 2 commutes
with extension of scalars: the rational fibre of $L\otimes_EE'$ is
$V\otimes_EE'$, where $V$ is the rational fibre of $L$. For a lisse
$\QbarX$-module $L$ with a model $L_E$ as in Step 1 we define its fibre
at $\bar x$ as $V_E\otimes_E\Qlb$, where $V_E$ is the rational fibre of
$L_E$.

Let $L$ and $L'$ be lisse $\QbarX$-modules with models $L_E$ and $L'_E$,
which we may take over a common $E$. A morphism $\phi:L\to L'$ is given,
on a quasi-compact pro-étale covering trivializing both models, by a
matrix with entries in $\QbarX$. As in Step 1, these entries lie in
$E'_X$ for a finite extension $E'/E$, and since $E'_X\to\QbarX$ is
injective on sections, $\phi$ is the extension of scalars of a unique
morphism $L_E\otimes_EE'\to L'_E\otimes_EE'$. Hence

$$
 \Hom(L,L')=\varinjlim_{E'}\Hom(L_E\otimes_EE',L'_E\otimes_EE').
$$

On the side of representations,

$$
 \Hom_{\pi_1(X,\bar x)}(V_E\otimes_E\Qlb,V'_E\otimes_E\Qlb)
 =\varinjlim_{E'}\Hom_{\pi_1(X,\bar x)}(V_E\otimes_EE',V'_E\otimes_EE'),
$$

because in the finite-dimensional space $\Hom_E(V_E,V'_E)$ the invariant
vectors are the intersection of the kernels of finitely many maps $g-1$,
and extension of scalars is exact. By Step 2 over each $E'$ and the
compatibility with extension of scalars, the fibre functor induces a
bijection between the two colimits, so it is fully faithful. Applied to
the identity of $L$ and two models of $L$, this shows that two models
become isomorphic after a finite extension of scalars, so that the fibre
of $L$ does not depend on the model up to canonical isomorphism.

It remains to prove essential surjectivity. Let
$\rho:\pi_1(X,\bar x)\to\GL_r(\Qlb)$ be continuous, for the valuation
topology on $\Qlb$. Each finite extension $E$ of $\Ql$ in $\Qlb$ is
complete, hence closed in $\Qlb$, and there are only countably many of
them, since $\Ql$ has only finitely many extensions of each degree in
$\Qlb$. Thus the compact group $\pi_1(X,\bar x)$ is the countable union
of the closed subgroups $\rho^{-1}(\GL_r(E))$, and by the Baire category
theorem one of them has nonempty interior. It is therefore open, hence of
finite index. Adjoining to $E$ the entries of $\rho(g)$ for $g$ in a set
of coset representatives, we obtain a finite extension $E'$ with
$\rho(\pi_1(X,\bar x))\subseteq\GL_r(E')$. By Step 2 this
$E'$-representation is the fibre of a lisse $E'_X$-module $L_{E'}$, and
$\rho$ is the fibre of $L_{E'}\otimes_{E'_X}\QbarX$.
