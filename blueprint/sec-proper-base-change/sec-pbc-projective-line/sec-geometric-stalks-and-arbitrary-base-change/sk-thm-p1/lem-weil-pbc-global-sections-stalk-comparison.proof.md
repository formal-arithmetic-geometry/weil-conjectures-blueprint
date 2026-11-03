+++
kind = "proof"
of = "lem-weil-pbc-global-sections-stalk-comparison"
uses = ["lem-weil-pbc-inverse-image-stalk-germ"]
+++
Take the inverse-image stalk isomorphism and its germ compatibility. Evaluate it at the identity étale neighbourhood. The definition of globalSectionsUpperStarMap evaluates the adjunction unit at the chosen terminal object and then restricts along its base-change terminal isomorphism. Transport terminal evaluations to the identity objects by the unique terminal isomorphisms; naturality of evaluation and the point-colimit relation toPresheafFiber_w identify the induced germ with the identity-neighbourhood germ. Apply inverseImage_stalk_germ to obtain the displayed equality. ([lem-weil-pbc-inverse-image-stalk-germ]).
