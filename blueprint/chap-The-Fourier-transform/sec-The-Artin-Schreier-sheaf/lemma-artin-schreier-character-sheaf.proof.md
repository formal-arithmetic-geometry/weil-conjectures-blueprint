+++
kind = "proof"
of = "lemma-artin-schreier-character-sheaf"
order = 1221
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
We define $\mathcal L_\psi$ as an eigensheaf in the direct image of the
constant sheaf under an Artin–Schreier cover, and read off its
properties from the corresponding properties of the cover: addition of
roots for the first isomorphism, a fibrewise pairing for the second,
and the action of Frobenius on roots for the trace.

Fix a nontrivial character $\psi_0:\mathbf F_p\to E^\times$. Since the
trace pairing on $k_0$ is nondegenerate, there is $a\in k_0^\times$
such that $\psi(z)=\psi_0(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$.
The cover $u^p-u=ax$ of the affine line is finite étale, with group
of translations $\mathbf F_p$. Let $\mathcal L_\psi$ be the image of

$$
e_{\psi_0}=\frac1p\sum_{c\in\mathbf F_p}\psi_0(c)^{-1}\tau_c^*
$$

on the direct image of the constant sheaf $E$ under this cover. It is
lisse of rank one, since its stalk is the $\psi_0$-eigenspace in the
regular representation, and the root $u=0$ over $x=0$ specifies the
trivialization at zero. For the first isomorphism, adding roots of two
Artin–Schreier equations identifies the contracted product of the two
torsors with the torsor for the sum, and passing to the character
eigenspaces we obtain the isomorphism. For the second, the pairing on the direct image given by
summing products over the fibres is perfect and invariant under the
translations. Since, for an invariant pairing, the $\chi$- and
$\chi'$-eigenspaces of two characters are orthogonal unless
$\chi\chi'=1$, our pairing pairs the $\psi_0$-eigenspace perfectly
with the $\psi_0^{-1}$-eigenspace. Since
$\psi^{-1}(z)=\psi_0^{-1}(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$, the
$\psi_0^{-1}$-eigenspace of the same cover is $\mathcal L_{\psi^{-1}}$,
and we obtain $\mathcal L_\psi^\vee\simeq\mathcal L_{\psi^{-1}}$.

For a root $u$ above $x\in\mathbf F_{q^n}$ we have

$$
u^{q^n}=u+
\operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(ax).
$$

Geometric Frobenius acts on functions on the torsor by pullback along
this map, and hence on the chosen eigenspace by
$\psi_0(\operatorname{Tr}(ax))$. By transitivity of field traces, this is
the asserted trace. Since these scalars are roots of unity, their images
under any field embedding have absolute value one.
