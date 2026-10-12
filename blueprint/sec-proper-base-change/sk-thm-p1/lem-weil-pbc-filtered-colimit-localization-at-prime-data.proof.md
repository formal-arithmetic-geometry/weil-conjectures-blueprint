+++
kind = "proof"
of = "lem-weil-pbc-filtered-colimit-localization-at-prime-data"
+++
Set q_i = comap (colimit.ι F i) p. The colimit cocone identity gives q_i = comap (F.map a) q_j. Define D on objects by Localization.AtPrime q_i and on arrows by Localization.localRingHom. IsLocalization.ringHom_ext reduces the functor laws to the corresponding laws for F.

Define κ_i : D_i → Localization.AtPrime p by Localization.localRingHom applied to colimit.ι F i. The localRingHom_to_map identity proves the required algebraMap compatibility; ringHom_ext and colimit.w prove naturality, producing the stated cocone c.

Given a cocone s over D, compose its legs with the stage algebraMaps to obtain a cocone U(s) over F. Let f_s = colimit.desc F U(s). For y outside p, Types.jointly_surjective_of_isColimit, applied after isColimitOfPreserves (forget CommRingCat), supplies x in some F_i with ι_i(x)=y. Then x is outside q_i, so IsLocalization.map_units and its image under s_i show f_s(y) is a unit.

Define the induced map from Localization.AtPrime p to s.pt by IsLocalization.lift of f_s with the preceding unit proof. Its factorization equations follow by ringHom_ext at each q_i, localRingHom_to_map, lift_eq, and colimit.ι_desc. For uniqueness first restrict any competing map to colimit F; colimit.hom_ext and the given cocone equations identify this restriction with f_s. Then ringHom_ext at p identifies the competing localization map with the constructed lift. These data form IsColimit c.
