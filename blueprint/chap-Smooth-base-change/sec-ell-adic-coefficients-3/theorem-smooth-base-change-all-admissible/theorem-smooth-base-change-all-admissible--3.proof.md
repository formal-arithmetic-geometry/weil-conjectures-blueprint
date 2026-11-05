+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--3"
order = 700007
uses = ["proposition-inverting-ell", "theorem-smooth-base-change-all-admissible--1", "theorem-smooth-base-change-all-admissible--2", "proposition-integral-constructibility-criterion", "lemma-change-coefficients", "lemma-change-coefficients-direct-image"]
+++
The displayed consequence follows from the same ingredients as the Lean
proof. Choose an embedding $E\hookrightarrow\overline{\mathbf Q}_\ell$.
By [proposition-inverting-ell], choose an integral model
$K_0\in\Dbc(X,\mathcal O_E)$ with
$E\otimes^{\mathbf L}_{\mathcal O_E}K_0\simeq K$.
Its first reduction is of bounded constructible étale origin, so
[theorem-smooth-base-change-all-admissible--1] and
[theorem-smooth-base-change-all-admissible--2] make the integral base change
map invertible. The comparison for $\mathcal O_E\to E$ in
[lemma-change-coefficients], using [lemma-change-coefficients-direct-image],
identifies the extension of scalars of this map with the map at
$E\otimes^{\mathbf L}_{\mathcal O_E}K_0$. Naturality transports the result
to $K$.

Lean uses
`AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToRational`
as an intermediate scalar comparison. It composes this comparison with
the one for $E\to\overline{\mathbf Q}_\ell$ in the proof of
[theorem-smooth-base-change-all-admissible--4]; the separate conclusion
above is not called there.
