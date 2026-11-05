+++
kind = "proof"
of = "lemma-kunneth-formula-compact-supports--2"
order = 1222002
uses = ["proposition-construction-independence-rf-shriek", "proposition-proper-direct-image-constructible-complexes", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Choose a compactification $g=r\circ j$, with $j$ an open immersion
and $r$ proper, and pull it back along $f$. Proper base change for
$r$ and base change for extension by zero along $j$ are isomorphisms.
Pasting them gives the comparison for this compactification. This is
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekOfCompactificationBaseChangePasting_padicAlgCl`.
Independence of compactification then identifies its target with the
chosen $Rp_{1!}$. Evaluating the inverse at $L$, tensoring with $K$
and applying $Rf_!$ gives the asserted isomorphism.
