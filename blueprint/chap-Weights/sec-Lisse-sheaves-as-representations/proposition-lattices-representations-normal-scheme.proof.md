+++
kind = "proof"
of = "proposition-lattices-representations-normal-scheme"
order = 1081
uses = ["proposition-etale-implications", "lemma-stability", "theorem-pro-etale-refinements-weakly-etale", "lemma-global-lattice-normal-scheme"]
+++
Let $M\subset L$ be as in the statement, with reductions $M_n=M/\pi_E^nM$.
The fibres of these reductions define a continuous action of
$\pi_1(X,\bar x)$ on the finite free completed fibre

$$
M_{\bar x}:=\varprojlim_n(M_n)_{\bar x}.
$$

The fibre functor of the proposition takes $L$ to the rational fibre
$M_{\bar x}\otimes_{\mathcal O_E}E$; in other words, we apply the fibre functor of finite
covers to the finite reductions and complete the result.

Full faithfulness comes from
the Galois theory of finite étale covers of the connected scheme $X$. It says that
taking the fibre at $\bar x$ is an equivalence between finite locally
constant sheaves on $X_{\acute{e}t}$ and finite sets with continuous
$\pi_1(X,\bar x)$-action, compatible with module structures.
To pass from the finite reductions to $L$ we need to clear denominators.
Let $M\subseteq L$ and $M'\subseteq L'$
be lattices in two lisse $E_X$-modules. Then a morphism
$\phi:L\to L'$ has a uniform denominator: $\pi_E^c\phi$ maps $M$ into $M'$
for some $c\geq0$. To see this, bound the finitely many matrix entries on a
quasi-compact pro-étale covering trivializing both lattices.

For faithfulness, suppose the fibre of $\phi$ vanishes. Then the fibres of all
the reductions of $\pi_E^c\phi$ vanish, so these reductions vanish by the Galois
correspondence. Since $M'=\varprojlim_nM'_n$, it follows that $\pi_E^c\phi=0$.
For fullness, take an equivariant map between the rational fibres. After
multiplication by some $\pi_E^c$, it maps $M_{\bar x}$ into $M'_{\bar x}$. Its
reductions are then equivariant maps of finite fibres, so by the Galois
correspondence they come from compatible maps $M_n\to M'_n$. The
inverse limit of these is a map $M\to M'$ whose rationalization,
divided by $\pi_E^c$, has the given fibre.

The same uniform denominator, applied to the identity of $L$, shows that
the rational fibre does not depend on the lattice. Indeed, if $M_1$ and $M_2$ are
two lattices in $L$, then $\pi_E^c\,\mathrm{id}_{L}$ sends
$M_1$ into $M_2$ for some $c\geq0$, and symmetrically.
On fibres these maps, divided by $\pi_E^c$, therefore give mutually inverse
equivariant isomorphisms between the two rational fibres.

For essential surjectivity we build a stable lattice and glue its
reductions. A continuous
representation of the profinite group $\pi_1(X,\bar x)$ on $E^r$ has
compact image. Hence the $\mathcal O_E$-span of the translates of a
lattice is bounded and contains that lattice. As $\mathcal O_E$ is
noetherian, this span is a stable finite free lattice, and its reductions define
compatible finite locally constant étale sheaves. These sheaves become
constant simultaneously on the surjective pro-étale cover obtained
as the inverse limit of the finite étale covers corresponding to
their kernels. Their inverse limit is therefore lisse over
$\mathcal O_E$, and its rationalization is lisse over $E$. Finally, this
construction is inverse to the fibre functor.
