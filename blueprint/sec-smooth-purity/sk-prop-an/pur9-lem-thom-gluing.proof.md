+++
kind = "proof"
of = "pur9-lem-thom-gluing"
uses = ["pur9-def-vector-bundle", "pur9-lem-hom-from-constant", "pur9-lem-orientation-open-restriction", "pur9-lem-upper-shriek-composition-assoc"]
+++
By Lemmas [pur9-lem-thom-concentration] and [pur9-lem-hom-from-constant], morphisms of the displayed type are global sections of the sheaf $\mathcal H^0$ on $Z_{\Proet}$, compatibly with restriction. For two trivializations over $U\cap U'$, the two local sections differ by $a_g$ for the transition matrix $g$ (Definition [pur9-def-vector-bundle]) and agree by Input [pur9-input-linear-invariance-thom]. The construction of $\mathrm{th}_c$ is compatible with restriction to opens of the base by Lemma [pur9-lem-orientation-open-restriction], the associativity of Lemma [pur9-lem-upper-shriek-composition-assoc] and naturality of $\tau$; hence the local sections are compatible, and the sheaf axiom gives a unique global section.
