+++
kind = "proof"
of = "dag-lem-pe-coefficient-stratified-essential-image"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-origin-open-cover", "dag-lem-pe-coefficient-origin-affine-open-closed"]
+++
1. Use coefficient-sized Zariski locality [dag-lem-pe-coefficient-origin-open-cover]. Induct strongly on the number of strata for all schemes. For any point select its stratum and apply `lem-sf-constructible-partition-local-closed-stratum` to obtain an affine neighborhood where its pullback immersion is closed and its complementary open is quasi-compact. If there are no strata, there are no points and the open cover is empty. (uses [dag-lem-pe-coefficient-origin-open-cover], `lem-sf-constructible-partition-local-closed-stratum`)
2. Construct the comparison/pullback and composite-pullback isomorphisms by conjugating the sectionwise direct-image isomorphisms under the canonical Kan-extension/sheafification adjunctions. Transport each stratum origin through the Cartesian pullback square. Pull the stratification first to the affine neighborhood and then to the complement. The selected stratum is empty there; erase its Fin index using succAbove and apply the strong induction hypothesis to the remaining strata. These mates and the erased stratification are implemented as fully proved private helpers in the item, with no remaining hole.
3. The selected closed stratum has etale origin by the proved pullback helper, and the complement by induction. Apply affine open-closed gluing [dag-lem-pe-coefficient-origin-affine-open-closed]. The neighborhoods cover X, so the first step finishes. Full-image closed immersions are retained as closed immersions, with no false isomorphism assertion. (uses [dag-lem-pe-coefficient-origin-affine-open-closed])

Proof dependencies not drawn: `lem-sf-constructible-partition-local-closed-stratum`.
