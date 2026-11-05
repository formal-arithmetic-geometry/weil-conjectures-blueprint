+++
kind = "proof"
of = "proposition-locally-constant-sheaves-finite-presentation--2"
order = 146005
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-stability", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image"]
+++
First separate the isomorphism types of the constant models. On a
nonempty overlap, a geometric stalk identifies the two models. For a
fixed type, take the whole space on covering members of that type and
the empty open on the others. These opens agree on overlaps and
descend by fpqc descent to an open of $X$. The resulting opens cover
$X$, and over each of them the given covering has one fixed finite
model $M$.

For a fixed model, consider the sheaf
$\mathit{Isom}(F,\underline M)$ of module-sheaf isomorphisms on the
localized sites. Isomorphisms form a sheaf by gluing maps and their
inverses. For constant finitely generated modules, a finite set of
generators permits one to lift a sheaf map locally to a module map
and to test equality after a common refinement. Applying this to an
isomorphism and its inverse identifies the isomorphism sheaf between
constant models with the constant sheaf on their module isomorphisms.
Thus $\mathit{Isom}(F,\underline M)$ is locally constant with value
$\operatorname{Aut}_\Lambda(M)$ and has sections on the given cover.
This fixed-model argument requires only finite generation of $M$ over
a discrete commutative ring.

To descend these sections, use the comparison for sheaves of sets.
A locally constant sheaf of sets is locally classical, since comparison
pullback preserves constant sheaves. Local classicality implies
continuity on affine ind-étale presentations: refine by affine objects
and use finite covering equalizers to commute sections with filtered
colimits. The affine comparison formula and
[theorem-classical-sheaves-essential-image] then make the comparison
counit invertible, so the sheaf is classical.

Write the isomorphism sheaf as $\nu_X^*H$. Its local sections make
$\nu_X^*H\to 1$ an epimorphism. Full faithfulness of $\nu_X^*$ and
its preservation of the terminal sheaf imply that $H\to 1$ is an
epimorphism. Epimorphisms of sheaves of sets are locally surjective,
so $H$, and hence the isomorphism sheaf, has sections on an étale
cover. Transporting these sections from the localized sites gives
the desired module trivializations. Finally combine the covers on the
model-type opens to obtain an étale covering of $X$. The construction
also permits the empty scheme and the empty covering.
