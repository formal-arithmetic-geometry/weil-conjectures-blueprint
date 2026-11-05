+++
kind = "proof"
of = "theorem-generic-constructibility-base-change-rj--1"
order = 582001
uses = ["lemma-smooth-morphisms-locally-constant-sheaves", "lemma-coordinate-projections", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "lemma-universal-homeomorphism-base", "lemma-schematic-closure-uniqueness", "lemma-finite-morphisms", "lemma-detection-proper-direct-image", "lemma-identity-pasting"]
+++
We prove bounded constructibility together with invertibility of the base
change map, for all noetherian base changes. The induction is carried out
in $D^+(-_{\acute{e}t},\Lambda)$ for locally closed immersions, with the
induction statement asserting both conclusions when the generic fibre of
the source has dimension less than $n$.

First we need the smooth case with finite coefficients. Choose a positive
integer annihilating $\Lambda$ and invertible on $S$. Dévissage by its
prime factors reduces a finite locally constant sheaf to sheaves killed
by a prime $p$ invertible on $S$. Such a sheaf, after forgetting its
$\Lambda$-module structure, is an $\mathbf F_p$-sheaf, to which
[lemma-smooth-morphisms-locally-constant-sheaves] applies. Forgetting
coefficients detects constructibility and isomorphisms and is compatible
with direct image and base change. Short exact sequences give
distinguished triangles, so the conclusions pass back through the
dévissage after intersecting finitely many nonempty opens. This is
`AlgebraicGeometry.Etale.smoothGenericDirectImage`.

For $n=0$, the generic fibre is empty. The image of the source is a
constructible subset missing the generic point of $S$, so it misses a
nonempty open. Over that open every base-changed source is empty, and
both conclusions follow.

For the induction step, first work with a projective target. The
coordinate projections of [lemma-coordinate-projections] lower the
generic fibre dimension over $\mathbf A^1_S$. Apply the induction
hypothesis over this base to each coordinate and glue over the resulting
finite family of opens. After shrinking $S$, their complement is finite
over $S$. If the source is smooth and the sheaf finite locally constant,
the smooth case and [lemma-extension-across-finite-subset] extend both
conclusions across this complement. Finite affine covers and schematic
closures [lemma-schematic-closure-uniqueness] give the result for an
arbitrary target. Closed direct images are exact and satisfy base change
[lemma-finite-morphisms], so this also treats locally closed immersions.

For a general constructible sheaf, [lemma-generic-smooth-open] gives,
after shrinking and a finite universal homeomorphism of the base, a
smooth open $v:V\hookrightarrow X_{\mathrm{red}}$ on which the sheaf is
finite locally constant and whose complement has smaller generic fibre
dimension. Work on this reduction and write the pulled-back sheaf again
as $F$. Apply the smooth case just established to $v$ and $jv$, and
complete the unit to a distinguished triangle

$$
F\longrightarrow Rv_*v^*F\longrightarrow D\longrightarrow F[1].
$$

The complex $D$ is bounded constructible, and its restriction to $V$
vanishes. If $i$ is the closed complement, localization, as in
[lemma-detection-proper-direct-image], identifies $D$ with $i_*i^*D$.
Apply the induction hypothesis to the finitely many nonzero cohomology
sheaves of $i^*D$, intersect their opens, and use truncation triangles.
This gives both conclusions for $Rj_*D$. Applying $Rj_*$ to the displayed
triangle gives bounded constructibility for $Rj_*F$; compatibility of base
change with the unit and with composition [lemma-identity-pasting] gives
invertibility on its first term from invertibility on the other two.
This is `AlgebraicGeometry.Etale.exists_hasDirectImageBaseChangeOnPlus_of_dense_smooth`.

Finally descend from the reduction by its surjective closed immersion,
then along the finite universal homeomorphism
[lemma-universal-homeomorphism-base], and pass from the shrunken base to
$S$. This proves the induction step. The generic fibre has finite
dimension, so some $n$ applies; the compatibility of bounded below and
unbounded derived direct images gives the stated conclusion.
