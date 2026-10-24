+++
kind  = "proof"
of    = "sk-p-real-integral"
+++
This is [thm-lisse-qlbar-representations]; we sketch the argument. A
lisse $\overline{\mathbf Q}_{\ell,X}$-module is
$\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}\mathcal F$ for a lisse
$E_X$-module $\mathcal F$ over some finite $E/\Ql$, and two such models
become isomorphic after a finite extension of $E$. We may assume that
$\mathcal F$ has positive rank $r$.

*A lattice.* Since $X$ is regular, it is normal; being Noetherian and
connected, it is integral, with generic point $\eta$. By
[sk-lem-stratified-lattice], $\mathcal F$ has a lattice on some stratum of
a finite stratification, hence on a dense open $U\subseteq X$. Let
$q:T=\operatorname{Lat}(\mathcal F)\to X$ be the separated étale lattice
scheme of [sk-lem-stratified-lattice]; the lattice on $U$ is a section
$s:U\to T\times_XU$, an open and closed immersion. Since $T$ is étale over
the normal $X$, it is normal and its connected components are integral.
The component $T'$ containing $s(U)$ therefore satisfies
$T'\times_XU=s(U)\simeq U$. At a geometric point $\bar y$ of $X$, the
strict henselization $X^{\mathrm{sh}}$ is a normal domain, hence
irreducible. The étale surjective $T\times_XX^{\mathrm{sh}}\to X^{\mathrm{sh}}$
has a section, so $\mathcal F$ is constant on $X^{\mathrm{sh}}$ and
$T\times_XX^{\mathrm{sh}}$ is a disjoint union of copies of
$X^{\mathrm{sh}}$, one for each lattice in $E^r$. Exactly one of them lies
in $T'$, because $T'$ has a single point over $\eta$. So $T'\to X$ is
étale, surjective and universally injective, hence an isomorphism, and
its inverse is a lattice $\mathcal M\subseteq\mathcal F$ on all of $X$,
with $\mathcal M[1/\ell]=\mathcal F$. Regularity is used only through
normality: to make $X$ and the components of $T$ integral, and the strict
henselizations of $X$ irreducible.

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
the two resulting rational fibre representations. Over
$\overline{\mathbf Q}_\ell$, morphisms are the colimit of the morphisms over
finite extensions of $E$, and on the representation side invariants of a
finite-dimensional space commute with the flat extension of scalars.

*Stable lattices.* Let a compact group $G$ act continuously on $E^r$ and
let $L_0\subset E^r$ be a lattice. Its stabilizer is the preimage of the
open subgroup $\operatorname{Aut}(L_0)$, hence open, hence of finite index
in the compact $G$. So the $\mathcal O_E$-span of the translates of $L_0$
is a finite sum of lattices, a $G$-stable lattice.

It remains to prove essential surjectivity. A continuous
$\overline{\mathbf Q}_\ell$-representation of the profinite group
$\pi_1(X,\bar x)$ is defined over a finite $E$: $\overline{\mathbf Q}_\ell$
is an increasing union of finite extensions $E_m$ of $\Ql$, the closed
subgroups of elements acting through $\operatorname{GL}_r(E_m)$ cover the
compact group, so by the Baire category theorem one of them is open, and
adjoining the matrix entries at finitely many coset representatives gives
$E$. The image of $\pi_1(X,\bar x)$ is compact, so it stabilizes a finite
free lattice. Its reductions define compatible finite locally constant
étale sheaves. These become constant simultaneously on the surjective
pro-étale cover obtained as the inverse limit of the finite étale covers
corresponding to their kernels. Therefore their inverse limit is lisse
over $\mathcal O_E$, its rationalization is lisse over $E$, and its
extension of scalars is lisse over $\overline{\mathbf Q}_\ell$. This
construction is inverse to the fibre functor, and the fibre functor on
$\overline{\mathbf Q}_{\ell,X}$-modules does not depend on the model over
$E$, since two models agree after a finite extension of scalars.

*Complement.* For the curve statement, the geometric representation of a
lisse Weil sheaf is continuous and defined over a finite $E$; the
$\mathcal O_E$-span of the translates of a lattice under the compact group
$\rho(\pi_1(U))$ is a stable lattice, and its reductions are finite sets, so
the images of $\pi_1(U)$ in their automorphisms are finite
([p-real-integral]).
