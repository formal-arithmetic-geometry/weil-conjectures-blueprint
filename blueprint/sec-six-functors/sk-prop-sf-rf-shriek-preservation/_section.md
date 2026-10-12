+++
id = "sk-prop-sf-rf-shriek-preservation"
kind = "proposition"
title = "Preservation for the exceptional inverse image"
order = 2363
uses = ["sk-def-sf-admissible", "sk-def-sf-operations", "sk-def-sf-setting", "sk-lem-sf-mate", "sk-prop-sf-existence"]
lean = ["AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isOpenImmersion", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isFinite_of_etale", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isClosedImmersion", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_smoothOfRelativeDimension", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $A=A_{E,n}$ and let $f:X\to Y$ be a separated finite-type morphism of
finite-type $k$-schemes ($k=\overline{\mathbf F}_q$ as in
[sk-def-sf-setting]; the dimension bounds below are those of these
schemes), and let $Rf^!$ be the constructible exceptional adjoint of
[sk-def-sf-operations] (vi). Write $D_c^{[a,b]}$ for the bounded constructible
complexes with cohomology concentrated in $[a,b]$ and Tor amplitude in
$[a,b]$. Then $Rf^!$ preserves these interval categories, and hence the
finite-Tor subcategory, in the following cases: (i) $f$ an open immersion or
finite étale, with the same interval; (ii) $f=i:Z\hookrightarrow T$ a closed
immersion, $D_c^{[a,b]}\mapsto D_c^{[a,b+2d+1]}$ for a target $T$ of dimension
$\le d$ (a bound in terms of the dimension of the *target*, not of the
codimension of $Z$); (iii) $f$ smooth of pure relative dimension $d$, with the
shift $-2d$, $D_c^{[a,b]}\mapsto D_c^{[a-2d,b-2d]}$; (iv) *every* separated
finite-type $f$, with $D_c^{[a,b]}\mapsto D_c^{[a-2D,\,b+2\dim Y+1]}$, where
$D$ is the maximal embedding dimension of the affine charts
$U\hookrightarrow\mathbf A^{d_U}_V$ of $f$ — the sum of the shifts of (ii) and
(iii), chart by chart. The constants in (iv) depend only on $f$, not on $n$.

No admissibility datum is assumed. No bound of the form
$2\operatorname{codim}(Z,T)+1$ holds in (ii) for arbitrary closed immersions
(see the proof); the sharper codimension statement
$Ri^!\Lambda_T\cong\Lambda_Z(-c)[-2c]$ of [sk-thm-regular] is a separate
theorem, with regularity hypotheses ($Z$ regular and $T$ smooth, a regular
pair, not merely a regular immersion) and a coefficient hypothesis (the unit
object). Clause (iv) proves, for the unconditional $Rf^!$, the two
preservation clauses (2)–(3) of [sk-def-sf-admissible] with explicit
constants, for every separated finite-type morphism of finite-type
$k$-schemes and with constants independent of $n$. In particular every such
morphism satisfies the constructible analogue of exceptional-adjoint
admissibility at every finite stage, and wherever a morphism is required to
carry the admissibility datum in this constructible sense, the requirement
is met by this clause and [sk-prop-sf-existence] (c).
