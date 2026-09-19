+++
id = "lemma-nagata-elimination-indeterminacy"
kind = "lemma"
title = "Elimination of indeterminacy, [stacks-project]"
order = 378
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap"]
uses = ["def-nagata-elimination-indeterminacy", "lemma-nagata-flattening-ideal"]
+++
The morphism $X^{\mathrm{el}}(q,U)\to X$ is $U$-admissible, and the
constructed strict-transform projection
$q^{\mathrm{el}}\colon Z^{\mathrm{el}}(q,U)\to X^{\mathrm{el}}(q,U)$ is
an open immersion.

This is exactly the formalised statement: the identification of the
restriction of $q^{\mathrm{el}}$ over $U$ with the original chosen
isomorphism $q^{-1}(U)\cong U$ is *not* asserted here, because it is
already supplied to every consumer by
[lemma-nagata-strict-transform-over-complement], which identifies the
part of any strict transform lying over the preserved open with the ordinary
base change.

## Proof

By [lemma-nagata-flattening-ideal], the selected ideal is finite type,
is the unit ideal on $U$, and has open strict-transform projection. The
first two properties make its blow-up $U$-admissible; the last property and
the selected comparison over $U$ identifies the restriction of
$q^{\mathrm{el}}$ with $e_U$, so the named construction has exactly the
open-immersion and prescribed-over-$U$ fields asserted above.
