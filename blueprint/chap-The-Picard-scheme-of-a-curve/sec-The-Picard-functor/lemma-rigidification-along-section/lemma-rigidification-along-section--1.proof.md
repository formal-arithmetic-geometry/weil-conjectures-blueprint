+++
kind = "proof"
of = "lemma-rigidification-along-section--1"
order = 1520005
uses = ["lemma-rigidification-along-section--2", "lemma-rigidification-along-section--4"]
+++
The normalized classes form an fpqc sheaf. Indeed, choose representatives
of compatible classes on an fpqc cover and trivializations of their
pullbacks along the sections. Rescale the isomorphisms on overlaps by
units pulled back from the base so that they preserve these
trivializations. Condition $(\ast)$ implies surjectivity on global
functions, so [lemma-rigidification-along-section--2] makes the rescaled
isomorphisms unique. They therefore satisfy the cocycle condition.
Effective fpqc descent gives an invertible sheaf $\mathcal M$ on $C_T$.
Normalize it as in [lemma-rigidification-along-section--4]; the twist is
trivial on each member of the cover, so the normalized sheaf still
represents the prescribed local classes.

For uniqueness, two global classes agreeing on the cover differ by a
sheaf pulled back from $T$, by
`AlgebraicGeometry.exists_iso_tensorObj_of_pic_map_eq`. Its proof descends
the transition functions of their locally trivial ratio to $T$ using
$(\ast)$. The uniqueness statement in
[lemma-rigidification-along-section--4] then identifies the normalized
classes. This proves
`AlgebraicGeometry.isSheaf_fpqc_picardFunctorNormalized`, and hence the
fppf sheaf property used below.

The inclusion of normalized classes into $T\mapsto\operatorname{Pic}(C_T)$
is injective and locally surjective: trivialize $\sigma_T^*\mathcal L$ on
a Zariski cover of $T$. Composing this inclusion with the sheafification
map gives a locally bijective map of fppf sheaves, hence an isomorphism.
Its map on sections over every $T$ is the required bijection.

To compare this with rigidified pairs, choose a trivialization of
$\sigma_T^*\mathcal L$. Any two choices differ by a unit on $T$, and
pulling that unit back along $f_T$ gives an isomorphism of the resulting
pairs. Thus forgetting the trivialization identifies their isomorphism
classes with normalized classes; [lemma-rigidification-along-section--2]
also gives uniqueness of an isomorphism preserving the trivializations.
