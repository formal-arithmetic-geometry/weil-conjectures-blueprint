+++
id = "lem-weil-pbc-grothendieck-spectral-sequence"
kind = "lemma"
title = "Grothendieck spectral sequence for a composite"
order = 1233
uses = ["def-sp-composite-acyclicity", "def-sp-etale-dictionary", "def-weil-pbc-direct-image", "lem-weil-pbc-direct-image-preserves-injectives", "thm-sp-grothendieck", "thm-sp-grothendieck-base-change"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{h}Z$ be morphisms of schemes and let $F$ be
a sheaf on $X_{\Et}$. There is a functorial first-quadrant spectral sequence

$$
 E_2^{p,q}=R^ph_*R^qf_*F
 \Longrightarrow R^{p+q}(hf)_*F.
$$

No acyclicity hypothesis on $F$ is needed: the construction is via an
injective resolution of $F$, and $f_*$ preserves injectives because $f^{-1}$
is exact (the standard Grothendieck spectral sequence for the left exact
functors $f_*$, $h_*$; for bounded-below complexes with torsion cohomology the
same statement holds for the derived pushforwards by the same argument). It is
compatible with inverse image in a cartesian base change.
