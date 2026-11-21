+++
kind = "proof"
of = "dag-det-pe-hypercover-single-affine"
tags = ["sheaf-dag"]
uses = ["dag-det-pe-hypercover-formal-wcontractible", "dag-det-pe-hypercover-representable-epi-cover", "dag-det-pe-hypercover-finite-coproduct-spectrum", "dag-det-pe-hypercover-spectrum-replacement"]
+++
1. Apply the formal w-contractible hypercover theorem. Realize every finite family by a scheme coproduct using the qcqs finite-family geometry theorem. Its sheaf coproduct mapping property defines the augmentation and all simplicial maps; the coproduct universal property proves the functor laws. The existing affine-hypercover geometry proof supplies the proved sheaf realization finite-limit preservation, finite proper-face categories, comparison of canonical matching arrows, and universe-lowering of representable epimorphisms. Apply those proofs to the formal hypercover to obtain epimorphisms of represented sheaves. Construct actual proper-face limits in the qcqs slice and preserve them under its inclusion, so the targets remain quasi-separated. The representable epi covering criterion turns these epimorphisms into singleton covers, since the terms are finite coproducts of qcqs affines. Identify each finite coproduct with a w-contractible spectrum and apply spectrum replacement, retaining all matching equations and covering assertions. (uses [dag-det-pe-hypercover-formal-wcontractible], [dag-det-pe-hypercover-representable-epi-cover], [dag-det-pe-hypercover-finite-coproduct-spectrum], [dag-det-pe-hypercover-spectrum-replacement], `lem-weil-pbc-proetale-qcqs-finite-family-geometry`)

Proof dependencies not drawn: `lem-weil-pbc-proetale-qcqs-finite-family-geometry`, `def-weil-pbc-proetale-qcqs-subsite`.
