+++
id = "def-nagata-global-blowup-glue-data"
kind = "definition"
title = "Raw global blow-up gluing datum"
order = 302
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupGluingData"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-global-blowup-overlap-id-symm", "lemma-nagata-global-blowup-overlap-independent", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
Fix an affine cover $(V_i)_i$ of $X$. Define
$\mathsf G(X,\mathcal I,(V_i))$ to consist of the local schemes
$\mathsf B_{V_i}(\mathcal I)$, their inverse images of $V_i\cap V_j$, and
the overlap maps obtained by gluing the maps $\omega_{ij,s}$ on a chosen
basic affine cover of every intersection. The equality on intersections
required to glue these local maps is
[lemma-nagata-global-blowup-overlap-independent].
