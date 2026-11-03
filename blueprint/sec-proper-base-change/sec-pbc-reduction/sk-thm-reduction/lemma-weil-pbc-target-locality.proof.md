+++
kind  = "proof"
of    = "lemma-weil-pbc-target-locality"
uses = ["lem-weil-pbc-etale-cover-detects-iso", "lem-weil-pbc-qcqs-higher-direct-image"]
+++
Fix a cartesian square with $f$ on the right and $g:Y'\to Y$ at the bottom, and
$K\in\Dplus(X_{\Et},\Lambda)$ with torsion cohomology sheaves. The opens
$g^{-1}(U)$, $U\subseteq Y$ affine, cover $Y'$. A morphism in
$\Dplus(Y'_{\Et},\Lambda)$ is an isomorphism if its restrictions to the members of
an open cover are: apply [lem-weil-pbc-etale-cover-detects-iso] to the induced maps
of cohomology sheaves, restriction to an open being exact. The restriction of the
exchange morphism of the square to $g^{-1}(U)$ is the exchange morphism of the
restricted cartesian square with $f|_U$ on the right and
$g|_{g^{-1}(U)}:g^{-1}(U)\to U$ at the bottom, applied to $K|_{f^{-1}(U)}$:
restriction to an open commutes with derived direct image (higher direct images
are the sheafifications of $V\mapsto H^q(X\times_YV,-)$, by
[lem-weil-pbc-qcqs-higher-direct-image]) and with inverse images, compatibly with
the units and counits defining the exchange. The restricted complex again has
torsion cohomology sheaves, so the hypothesis on $f|_U$ applies.
