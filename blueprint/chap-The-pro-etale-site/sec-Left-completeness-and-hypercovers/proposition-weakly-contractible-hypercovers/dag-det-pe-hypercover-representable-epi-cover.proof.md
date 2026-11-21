+++
kind = "proof"
of = "dag-det-pe-hypercover-representable-epi-cover"
tags = ["sheaf-dag"]
uses = ["dag-def-weil-pbc-proetale-covering"]
+++
1. Apply local lifting to the identity of B, obtaining a covering sieve of arrows factoring through mu. Choose a covering presieve inside it using the stable-composition precoverage criterion. The underlying family is jointly surjective on points. Lift each such arrow through mu and apply it to a point above an arbitrary point of B, proving that mu is surjective. A morphism from a quasi-compact scheme to a quasi-separated scheme is quasi-compact. Cancellation against the weakly etale structure map of B shows that mu is weakly etale. A surjective quasi-compact weakly etale map is a singleton pro-etale cover. The argument includes empty schemes. (uses [dag-def-weil-pbc-proetale-covering], `lem-weil-pbc-proetale-representable-epi-local-lifting`)

Proof dependencies not drawn: `lem-weil-pbc-proetale-representable-epi-local-lifting`.
