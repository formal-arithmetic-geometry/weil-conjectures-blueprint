+++
id = "lem-sc-ga-cohomology"
kind = "lemma"
title = "Etale and Zariski cohomology agree for quasi-coherent sheaves"
lean = ["AlgebraicGeometry.etale_zariski_cohomology_agree", "AlgebraicGeometry.etale_ga_cohomology_agree", "AlgebraicGeometry.subsingleton_etale_ga_and_structure_cohomology"]
order = 1456
uses = ["def-sc-curves", "def-sc-etale-qcoherent-module", "pqf-lem-affine-vanishing", "lem-sc-affine-open-proper", "lem-sc-cech-spectral", "lem-sc-compactification", "lem-sc-etale-affine-qcoherent"]
+++
Let $C$ be a curve and $\mathcal F$ a
quasi-coherent module. For the
associated etale sheaf,

$$
H^q(C_{\mathrm{et}},\mathcal F_{\mathrm{et}})
\cong H^q(C_{\mathrm{Zar}},\mathcal F)\quad(q\geq0).
$$

In particular $H^q(C_{\mathrm{et}},\mathbf G_a)=H^q(C,\mathcal O_C)$,
and these groups vanish for $q\geq2$ when $C$ is a smooth connected curve.
