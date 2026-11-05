+++
kind = "proof"
of = "proposition-proper-base-change-complete-integral--1"
order = 417005
uses = ["corollary-finite-quotients-their-transition-maps", "definition-derived-adic-completeness", "definition-projection-formula-map", "lemma-inverse-image-coefficient-sheaves", "proposition-topos-functoriality"]
+++
For every $n\geq1$, inverse image commutes with derived reduction modulo
$\pi_E^n$. The coefficient comparison of
[lemma-inverse-image-coefficient-sheaves] and the scalar adjunction units
identify this isomorphism with the canonical comparison. Its adjoint is
the finite projection map of [definition-projection-formula-map].

The two-term resolution in
[corollary-finite-quotients-their-transition-maps] makes the finite
coefficient object dualizable. Its projection formula, together with the
scalar and geometric adjunctions, identifies the specified finite projection
map with an isomorphism. After restriction of scalars to $\mathcal O_E$,
the resulting comparison extends the identity maps on $Rp_*K$ to a morphism
of distinguished reduction triangles, retaining the connecting maps. The
third component is therefore invertible. Restriction of scalars is exact
and conservative, so this also detects invertibility before forgetting the
finite coefficient action. Taking $n=1$ gives the asserted residue comparison.

Write $K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}
(\mathcal O_E/\pi_E^n)_X$. The finite projection isomorphisms identify
$Rp_*K_n$ with the reductions of $Rp_*K$, compatibly with both the quotient
transition maps and the canonical maps from $Rp_*K$. If $K$ is complete,
its reduction tower gives a distinguished derived limit triangle

$$
K\longrightarrow\prod_{n\geq1}K_n
\xrightarrow{1-\mathrm{shift}}\prod_{n\geq1}K_n
\longrightarrow K[1].
$$

The functor $Rp_*$ is triangulated and, as a right adjoint, preserves these
products. Applying it to this triangle and using the compatible finite
projection isomorphisms gives the derived limit triangle for the reductions
of $Rp_*K$. The characterization of completeness by this triangle shows
that its canonical completion map is invertible, as required by
[definition-derived-adic-completeness].
