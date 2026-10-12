+++
kind = "proof"
of = "lem-weil-pbc-compatible-pullback-sheaf-system"
uses = ["lem-weil-pbc-inverse-image-composition"]
+++
For the identity arrow use the left unit law upperStarComp_id_left from [lem-weil-pbc-inverse-image-composition]. The fully proved private helper upperStarComp_inv_of_eq_id performs equality induction on an endomorphism h equal to the identity and evaluates the inverse of this unit law at G. Applying it with h = D.map (identity at op i), the equality D.map_id and wv i i (identity at i) gives exactly the transported identity comparison. All hypotheses and equality transports are retained.

Evaluate the existing component associativity law upperStarComp_hom_app_map_upperStarComp_inv_app (WeilConjectures.SixFunctors.BaseChange.Pasting, a proved rearrangement of the coherence in [lem-weil-pbc-inverse-image-composition]) on D.map g.op, D.map f.op and v i, with named composites D.map (f followed by g).op, v j and v k. Supply D.map_comp, wv i j f and wv i k (f followed by g). The law says the forward comparison for the first pair followed by the pullback of phi f is phi (f followed by g) followed by the forward comparison for g. Cancel that last isomorphism using Iso.eq_comp_inv and reassociate to obtain precisely the cocycle equation.

Apply the same component associativity law from [lem-weil-pbc-inverse-image-composition] to the cone leg at j, D.map f.op and v i, with named composites the cone leg at i, v j and vLimit. Supply the reversed cone equation d.w f.op, wv i j f and wLimit i. Compose the resulting equality on the left with eS i hom and on the right with eS j inverse. Associativity and the hom-inverse identities cancel both comparisons, leaving the identity of the pullback along vLimit. This is S.map f because S is the constant functor.
