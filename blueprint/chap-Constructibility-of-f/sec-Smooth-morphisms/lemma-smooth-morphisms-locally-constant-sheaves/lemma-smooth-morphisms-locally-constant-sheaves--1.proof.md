+++
kind = "proof"
of = "lemma-smooth-morphisms-locally-constant-sheaves--1"
order = 564002
uses = ["definition-relative-dualizing-complex", "theorem-nagata-s-compactification-theorem", "theorem-existence-exceptional-inverse-image", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism--3", "proposition-exceptional-inverse-image-smooth-morphism--4", "proposition-exceptional-inverse-image-smooth-morphism--6", "proposition-exceptional-inverse-image-smooth-morphism--7", "theorem-results-from-etale-theory--3", "proposition-composition-base-change-rf-shriek"]
+++
The schemes $S$ and $X$ are Noetherian. Put
$\omega_f=f^!\Fell_S$. Cover $X$ by opens on which $f$ has constant
relative dimension. On these opens, the chart description
[proposition-exceptional-inverse-image-smooth-morphism--3] and the rank
statement [proposition-exceptional-inverse-image-smooth-morphism--4]
make $\omega_f$ invertible and bounded constructible of finite Tor
amplitude. Invertibility is local, and a finite subcover gives common
cohomological and Tor bounds on $X$. This is the step called
`modelSmoothDualizing` in Lean.

Set

$$
N=\cHom_X(L,\omega_f).
$$

Over $\Fell$, the finite locally constant sheaf $L$ is locally free of
finite rank. Its coefficient dual is again of this kind, and
$N\simeq\cHom_X(L,\Fell_X)\otimes^{\mathbf L}\omega_f$.
Thus $N\in\Dctf(X,\Fell)$ is dualizable, and evaluation gives
$L\simeq\cHom_X(N,\omega_f)$. These are the assertions of
`AlgebraicGeometry.Etale.finiteLisseRelativeDual`.

Choose a compactification using
[theorem-nagata-s-compactification-theorem], and put $C=Rf_!N$.
Finiteness for compact support [theorem-results-from-etale-theory--3]
makes $C$ bounded constructible. The compact adjunction of
[theorem-existence-exceptional-inverse-image], together with the
projection formula, gives

$$
Rf_*\cHom_X(N,f^!\Fell_S)
\simeq\cHom_S(Rf_!N,\Fell_S).
$$

Lean uses `AlgebraicGeometry.Etale.isIso_projectionMap_of_finite`
and `AlgebraicGeometry.Etale.derivedHomLowerShriekIsoOfAdjunction`
for this step.

Apply the same construction after restriction to $U$ and after base
change to a Noetherian $T$. Compact base change
[proposition-composition-base-change-rf-shriek] identifies the compact
images with $C_U$ and $v^*C_U$. Exceptional base change
[proposition-exceptional-inverse-image-smooth-morphism--6] and
[proposition-exceptional-inverse-image-smooth-morphism--7], applied on
the smooth charts and then descended, identifies the relative dualizing
complexes. Pullback preserves the dualizability of $N$, so the relative
duality presentations also pull back. This constructs $\delta_U$ and
$\delta_T$.

Finally, internal compact adjunction is compatible with the cartesian
square: transpose the pairing given by the ordinary counit and
evaluation, and use naturality of compact base change and of the
coefficient-unit identification. This is
`AlgebraicGeometry.Etale.compactInternalAdjunctionExchange`.
It gives precisely
$\delta_T\circ b_{v,L_U}=\gamma_{v,C_U}\circ v^*\delta_U$,
which is the `exchange` field of the constructed
`AlgebraicGeometry.Etale.SmoothCompactDualModel`.
