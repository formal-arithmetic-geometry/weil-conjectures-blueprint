+++
id = "lem-weil-pbc-grothendieck-spectral-sequence"
kind = "lemma"
title = "Grothendieck spectral sequence for a composite"
lean = ["AlgebraicGeometry.Etale.exists_grothendieckSpectralSequence_lowerStar"]
order = 2046
uses = ["def-sp-composite-acyclicity", "def-sp-etale-dictionary", "def-weil-pbc-direct-image", "lem-weil-pbc-direct-image-preserves-injectives", "thm-sp-grothendieck"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{h}Z$ be morphisms of schemes, let $\Lambda$ be
a commutative ring and let $F$ be a sheaf of $\Lambda$-modules on $X_{\Et}$. There
is a first-quadrant cohomological spectral sequence

$$
 E_2^{p,q}=R^ph_*R^qf_*F
 \Longrightarrow R^{p+q}(h_*\circ f_*)F=R^{p+q}(hf)_*F.
$$

No acyclicity hypothesis on $F$ is needed: $f_*$ preserves injectives because
$f^{-1}$ is exact [lem-weil-pbc-direct-image-preserves-injectives], which is the
hypothesis of the Grothendieck spectral sequence for the left exact functors
$f_*$ and $h_*$.
