+++
kind = "proof"
of = "dag-lem-pe-coefficient-fp-local-system-etale-cover"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-locally-constant-etale-sections"]
+++
1. Apply the local-model hypothesis at the terminal AsSmall object. Index its covering sieve by pairs (U, arrow U to the terminal object in the sieve). This produces a coefficient-sized family U_i covering the final object, with finitely presented constant models M_i and slice isomorphisms e_i. No conversion to a scheme covering or index shrinking is needed.
2. Construct the set sheaf H_i of slice isomorphisms from F to constant M_i by gluing maps and inverses in sheafHom. Iterated slices identify its restriction to U_j with the Isom sheaf between constant M_j and constant M_i. The private fixedConstantHom helpers prove local injectivity using a finite generating set and local surjectivity by lifting its images and using injectivity of the constant-sheaf unit away from empty covers. Lift both maps of an isomorphism and refine by the two inverse equations; sheafification then identifies this Isom sheaf with constant (M_j isomorphic to M_i). Finite presentation supplies finite generation for both models. Hence every H_i is locally constant. All these assertions are proved by private helpers in the delivered Lean, in an arbitrary small-site universe. (uses `def-sc-finitely-presented-module`, `lem-weil-pbc-site-constant-restriction`)
3. The family H_i is jointly locally inhabited: on U_j use e_j followed by the constant-sheaf restriction isomorphism as a section of H_j. Apply coefficientLocallyConstant_etaleSections to obtain etale objects whose pro-etale images cover and which each have a section of some H_i. This only requires local constancy of set sheaves, and it permits the empty isomorphism sets that occur between different model types. (uses [dag-lem-pe-coefficient-locally-constant-etale-sections])
4. Each resulting section is an isomorphism F.over i(V_j) to the restriction of constant M_i. Compose with the inverse constant-sheaf restriction isomorphism. Retain the previously chosen finite-presentation proof of M_i; these are exactly the required charts. (uses `lem-weil-pbc-site-constant-restriction`)

Proof dependencies not drawn: `def-sc-finitely-presented-module`, `lem-weil-pbc-site-constant-restriction`.
