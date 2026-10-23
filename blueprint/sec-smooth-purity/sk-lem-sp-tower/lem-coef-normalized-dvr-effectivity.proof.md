+++
kind  = "proof"
of    = "lem-coef-normalized-dvr-effectivity"
+++
Fix $n$, and discard the finitely many indices $m<n$.
The coefficient complex

$$
C_{m,n}=A_m\otimes^{\mathbf L}_{\mathcal O_E} A_n
=[A_m\xrightarrow{\pi_E^n}A_m]
$$

is in degrees $[-1,0]$. Its augmentation to $A_n$ has
fiber $(\pi_E^{m-n}A_m)[1]\cong A_n[1]$, as an object of
$D(A_m)$, because $\mathcal O_E$ is $\pi_E$-torsion free. This identification uses multiplication by
$\pi_E^{m-n}$; its inverse on the fiber is determined by the
single nonzero cohomology module. For $m'\geq m\geq n$,
coefficient reduction sends the generator $\pi_E^{m'-n}$ to
$\pi_E^{m'-m}\pi_E^{m-n}$. Thus the fiber transition, expressed
in these copies of $A_n[1]$, is multiplication by
$\pi_E^{m'-m}$.

Tensor this coefficient triangle with $M_m$ over $A_m$.
The normalization isomorphisms, which are compatible with composition because
they are induced by the transition maps of one object of the tower category,
give a tower of triangles

$$
M_n[1]\longrightarrow M_m\otimes^{\mathbf L}_{A_m} C_{m,n}
\longrightarrow M_n\longrightarrow .
$$

The right-hand tower is constant, with identity transitions. The
left-hand transition for $m'\to m$ is multiplication by
$\pi_E^{m'-m}$: this follows by tensoring the just computed
coefficient map and using the same normalization isomorphisms. The
calculation is made in strict coefficient complexes and their
derived tensor products, so these are compatible triangles of
towers, not independently chosen cones.

Every $n$ successive left-hand transitions compose to zero.
In the defining triangle
$R\varprojlim\to\prod\xrightarrow{1-s}\prod$ of [sk-prop-pe-milnor], the
shift $s$ on the derived product therefore satisfies $s^n=0$.
The inverse of $1-s$ is $1+s+\cdots+s^{n-1}$, so this
fiber tower has zero derived limit. The quotient $A_n$ has
the bounded finite-free $\mathcal O_{E,T}$-resolution
$[\mathcal O_{E,T}\xrightarrow{\pi_E^n}\mathcal O_{E,T}]$, and
$M_m\otimes^{\mathbf L}_{\mathcal O_{E,T}}A_n\simeq M_m\otimes^{\mathbf L}_{A_m}C_{m,n}$. Tensoring with this resolution commutes
with derived products and fibers, hence with the derived limit
in that triangle. Taking limits in the displayed triangles
now proves

$$
M\otimes^{\mathbf L}_{\mathcal O_{E,T}} A_n
\cong R\varprojlim_m(M_m\otimes^{\mathbf L}_{\mathcal O_{E,T}} A_n)
\xrightarrow{\sim}M_n.
$$

Every map is induced by the tower projections and coefficient
augmentations, so these isomorphisms have the stated cocycle.
They identify the original tower with the quotient tower of
$M$; its limit is $M$, so $M$ is derived $\pi_E$-complete
([def-pe-derived-complete]).
For the coefficient tower itself, $(A_n)_T$ with the quotient maps, the
derived limit is $\mathcal O_{E,T}$ in degree zero: the ordinary limit is
$\mathcal O_{E,T}$ by [sk-prop-sfb-qlbar-colimit-x], and
$R^1\varprojlim$ vanishes because on a weakly contractible quasi-compact
pro-étale basis object sections are exact and the transition maps are
surjective on sections.
