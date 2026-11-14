+++
kind = "proof"
of = "dag-lem-pe-coefficient-tor-flat-model"
tags = ["sheaf-dag"]
+++
1. Use functorial flat covers to supply categorical flat resolutions; symmetry identifies one-sided sheaf flatness with categorical flatness. (uses `lem-pc-sites-modules-functorial-flat-cover`)
2. Identify acyclic-test K-flatness with native quasi-isomorphism-preserving K-flatness using the homotopy-category acyclic criterion and symmetry. (uses `def-pc-kflat-complex`)
3. On each K-flat representative the native derived tensor is the same total tensor in the coefficient-model test. Homology localization identifies their vanishing conditions. Apply the source theorem DerivedCategory.torAmplitudeIn_iff_exists_iso_Q_obj_flat; its proof resolves above and truncates below, proving flatness of the first opcycle by the tensor exactness criterion. (uses `def-weil-abstract-derived-category`, `def-sbc-standard-tstructure-derived-category`, `lem-weil-pbc-site-flat-opcycles-tor-criterion`)

Proof dependencies not drawn: `lem-pc-sites-modules-functorial-flat-cover`, `def-pc-kflat-complex`, `def-weil-abstract-derived-category`, `def-sbc-standard-tstructure-derived-category`, `lem-weil-pbc-site-flat-opcycles-tor-criterion`.
