+++
kind = "proof"
of = "lem-pbc-h2-integral-open-extension-comparison"
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image"]
+++
For both coefficient categories, replace $j^{-1}$ by restriction to the etale site of $U$. Restriction is precomposition, so it commutes with $E$ sectionwise [def-weil-pbc-inverse-image].

Extension by zero is the left Kan extension along the inclusion of etale sites followed by sheafification [def-weil-pbc-extension-by-zero]. The equivalence $E$ preserves limits and colimits, so it commutes with left Kan extension and with sheafification. Composing these isomorphisms with the restriction comparisons gives the displayed isomorphism.
