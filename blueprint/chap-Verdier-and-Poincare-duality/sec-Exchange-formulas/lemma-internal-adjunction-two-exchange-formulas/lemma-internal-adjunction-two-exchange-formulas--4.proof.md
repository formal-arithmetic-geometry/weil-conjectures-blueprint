+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--4"
order = 830008
uses = ["definition-derived-base-change-map", "definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "proposition-forgetting-supports-composition--3", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
The exchange comparison used below is clause [lemma-internal-adjunction-two-exchange-formulas--2].

The comparison of double-dual maps is used in the proof of biduality for
$f=a_X$, where it identifies $R\Gamma(X,\delta_K)$
with the double-dual map of the perfect complex $R\Gamma(X,K)$. Both
maps are determined by pairings, and we compare the pairings.
For proper $f$ we have
$Rf_!=Rf_*$, and the isomorphism (10.3) is adjoint
to the pairing

$$
Rf_*K\otimes^{\mathbf L}Rf_*\mathbb D_XK
\longrightarrow Rf_*(K\otimes^{\mathbf L}\mathbb D_XK)
\longrightarrow Rf_*\omega_X\longrightarrow\omega_Y.
$$

Using (10.3) for $K$ and for $\mathbb D_XK$, we
view both $Rf_*\delta_K$ and $\delta_{Rf_*K}$ as maps
$Rf_*K\to\mathbb D_YRf_*\mathbb D_XK$. Up to the symmetry of the
tensor product, both are adjoint to this pairing. For
$\delta_{Rf_*K}$ this holds because under (10.3) for
$K$ evaluation on $Y$ corresponds to the pairing. For
$Rf_*\delta_K$ it holds because $\delta_K$ is adjoint to evaluation
on $X$ and (10.3) for $\mathbb D_XK$ is adjoint
to the analogous pairing.

*Source:* the proof of Lemma [lemma-internal-adjunction-two-exchange-formulas].
