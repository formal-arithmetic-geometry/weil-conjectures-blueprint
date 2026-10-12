+++
kind = "proof"
of = "lem-weil-pbc-finite-idempotent-factor-transfer"
+++
Choose a unit v with value α. The relation bd = αd gives d = b(α⁻¹d), hence b divides d. Apply Localization.awayMap_bijective_of_dvd to obtain the isomorphism D[1/d] → B[1/e]. The map D → D[1/d] is surjective by Away.algebraMap_surjective_of_isIdempotentElem. Therefore F:D → B[1/e] is surjective, and Algebra.IsIntegral.of_surjective transfers integrality of the finite A-algebra D.

Define s:D → A/I as the first projection of Φ after quotient. It is an A-algebra map and s(d)=1. Extend s over D[1/d], then transport along the isomorphism to a map ρ:B[1/e] → A/I. The ideal IB[1/e] is in its kernel, since ρ fixes A-scalars. Hence ρ induces a left inverse of the quotient structure map, proving injectivity.

For surjectivity, represent an element of B[1/e]/IB[1/e] by F(x), using the surjectivity of F. Lift the first coordinate of Φ(x mod ID) to a∈A. Then Φ(d(x-a) mod ID)=(1,0)(Φ(x)-(a,scalar(a)))=0. Thus d(x-a)∈ID; mapping by F, for which F(d)=1, gives F(x)-a∈IB[1/e]. The quotient element is therefore the image of a mod I.
