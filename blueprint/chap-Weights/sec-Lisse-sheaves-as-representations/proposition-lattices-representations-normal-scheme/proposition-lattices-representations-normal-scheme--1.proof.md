+++
kind = "proof"
of = "proposition-lattices-representations-normal-scheme--1"
order = 1080002
uses = ["proposition-etale-implications", "lemma-stability", "theorem-pro-etale-refinements-weakly-etale", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves"]
+++
Since $X$ is connected and locally noetherian and its local rings are
domains, it is irreducible. Choose universal profinite étale covers
$p_y:\widetilde X_y\to X$ at the geometric points $y$; these exist by
`AlgebraicGeometry.Scheme.nonempty_universalCovers`.

Every lisse sheaf becomes free of finite rank on each $\widetilde X_y$.
This is
`AlgebraicGeometry.ProEtale.IsAdicLisseSheaf.exists_iso_upperStar_universalCover_of_isIntegrallyClosed_stalk`.
To obtain it, first trivialise the sheaf on a single affine pro-étale
cover. The transition matrices and their inverses take values in a
finite extension $E/\mathbf Q_\ell$. Their cocycle acts on the discrete
quotients $\GL_r(E)/K_n$, where $K_n$ are the congruence subgroups of
$\GL_r(\mathcal O_E)$. Normality makes the resulting locally constant
sheaves trivial on $\widetilde X_y$. The construction uses the refinements
of [theorem-pro-etale-refinements-weakly-etale]. Compatible sections of
these quotients, together with completeness, trivialise the matrix
cocycle. Correcting the original trivialisation by this matrix gives
trivial descent data, so the free sheaf descends to $\widetilde X_y$.

Restriction to the chosen point of the connected cover now identifies
$\Gamma(\widetilde X_y,p_y^*L)$ with $L_y$. Transport of the universal
covers along a path gives

$$
L_y\simeq\Gamma(\widetilde X_y,p_y^*L)
\simeq\Gamma(\widetilde X_z,p_z^*L)\simeq L_z.
$$

Functoriality of restriction and pullback gives all the asserted
compatibilities, including the evaluation pairing. This is the
construction `AlgebraicGeometry.Scheme.UniversalCovers.lisseMonodromy`.

For continuity, each matrix coefficient of the action is the value of
a continuous function on $\widetilde X_t\times_X\widetilde X_t$ along the
continuous graph of a loop. For faithfulness, if a morphism vanishes on
one stalk, the inclusion of its kernel is surjective there. Kernels of
maps of lisse sheaves are lisse on the irreducible scheme $X$, and
surjectivity at one stalk implies that this inclusion is an epimorphism;
the original morphism is therefore zero. For fullness, an equivariant
linear map $L_t\to L'_t$ is an invariant vector of
$\mathcal{H}om(L,L')_t$. It descends to a global section of the internal
Hom and hence to a morphism $L\to L'$.

Finally, a continuous finite-dimensional representation defines a matrix
cocycle on $\widetilde X_t\times_X\widetilde X_t$ by evaluating the
representation on the loop determined by each pair of points. Its matrix
coefficients lie in a finite extension of $\mathbf Q_\ell$, so they are
sections of the coefficient sheaf. Descend the free sheaf along $p_t$
using this cocycle. Its stalk representation is the given one. These four
properties are assembled in
`AlgebraicGeometry.Scheme.UniversalCovers.lisseMonodromy_isEquivalenceAt_of_irreducibleSpace`.
The regular case follows because the local rings of a regular scheme
are integrally closed domains.
