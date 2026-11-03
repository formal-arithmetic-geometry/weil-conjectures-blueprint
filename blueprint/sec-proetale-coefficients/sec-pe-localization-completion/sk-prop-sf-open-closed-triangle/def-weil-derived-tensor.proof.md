+++
kind  = "proof"
of    = "def-weil-derived-tensor"
uses  = ["det-def-sfb-sheaf-tensor-closed", "lem-sfb-derived-monoidal"]
+++
The small pro-étale site is essentially small, so $\Sh(Y_{\mathrm{proét}},\mathcal A)$ is a
Grothendieck abelian category, and with the sheaf tensor product it is closed symmetric
monoidal [det-def-sfb-sheaf-tensor-closed]. It has functorial flat resolutions because
$\mathcal A$ does: the sheafified free objects on representables, tensored with a flat
separator of $\mathcal A$, form a flat separator. Hence [lem-sfb-derived-monoidal] applies,
and its derived tensor product is computed by replacing either argument by a K-flat
resolution, which gives the concrete description.
