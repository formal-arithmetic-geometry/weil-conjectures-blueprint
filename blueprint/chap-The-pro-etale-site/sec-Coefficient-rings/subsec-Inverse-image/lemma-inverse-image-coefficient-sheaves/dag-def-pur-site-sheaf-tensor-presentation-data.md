+++
id = "dag-def-pur-site-sheaf-tensor-presentation-data"
kind = "dag-definition"
title = "The sectionwise and monoidal tensor presentation isomorphisms"
name_showing = false
order = 187514
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "def-pur-site-sheaf-tensor-presentation-data"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.siteTensorRightIso", "SheafOfModules.tensorRightPresentation", "SheafOfModules.siteSheafTensorRightIso"]
+++
On a site $(\mathcal C,J)$ essentially small in the coefficient universe, let $R$ be a commutative ring sheaf and $M,N$ module sheaves `def-weil-sheaf-of-modules-category`. The sheafified sectionwise tensor and its monoidal localization are those of [dag-def-pur-sheaf-tensor-product]. Define siteTensorRightIso to be the identity on sectionwise pure tensors from the explicit presheaf tensor functor to the monoidal presheaf tensor functor. Define tensorRightPresentation by the monoidal module-sheafification comparison and its invertible counit on sheaves. Define siteSheafTensorRightIso as sheafification of the sectionwise comparison followed by the inverse presentation, giving a natural isomorphism $(-\otimes_{\mathrm{site}} M)\cong(-\otimes_{\mathrm{mon}} M)$. These are the existing canonical isomorphisms, not an assertion of tensor colimit preservation.

(SHEAF DAG node `def-pur-site-sheaf-tensor-presentation-data`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: definition. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `lem-weil-pbc-module-tensor-symmetric-monoidal`.
