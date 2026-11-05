+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--4"
order = 700009
uses = ["theorem-smooth-base-change-all-admissible--1", "theorem-smooth-base-change-all-admissible--2", "proposition-integral-constructibility-criterion", "proposition-inverting-ell", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-change-coefficients-direct-image"]
+++
The schemes $X$ and $Y'$ are Noetherian, $f$ is quasi-compact and
quasi-separated, and $\ell$ is invertible on $Y$.
By [proposition-dctf-x-qbar-2-colimit] and [proposition-inverting-ell], choose
a finite subextension $E\subset\overline{\mathbf Q}_\ell$ and an integral
model $K_0\in\Dbc(X,\mathcal O_E)$ with

$$
\overline{\mathbf Q}_\ell\otimes^{\mathbf L}_E
(E\otimes^{\mathbf L}_{\mathcal O_E}K_0)\simeq K.
$$

The scalar comparisons of [lemma-change-coefficients] for
$\mathcal O_E\to E$ and $E\to\overline{\mathbf Q}_\ell$ identify the
extension of scalars of the integral base change map with the map at this
model. Their direct-image comparisons are invertible by
[lemma-change-coefficients-direct-image]. Thus it suffices to prove the
integral map invertible; Lean packages this reduction as
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_padicAlgCl_of_integral`.

By [theorem-smooth-base-change-all-admissible--2], it is enough to prove
invertibility at $K_1=K_0\otimes^{\mathbf L}_{\mathcal O_E}\mathbf F_E$.
The integral constructibility criterion
[proposition-integral-constructibility-criterion] puts $K_1$ in the
bounded constructible category of étale origin. Since $\ell$ kills
$\mathbf F_E$ and is invertible on $Y$,
[theorem-smooth-base-change-all-admissible--1] applies. Derived Nakayama
then gives the integral isomorphism, and extension of scalars and
naturality give the asserted map at $K$.
