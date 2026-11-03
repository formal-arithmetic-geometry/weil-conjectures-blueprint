+++
kind  = "proof"
of    = "lem-weil-pbc-grothendieck-spectral-sequence"
+++
The pair $(f_*,h_*)$ is a composable pair of left exact functors between
categories of sheaves of $\Lambda$-modules, which have enough injectives, and the
hypothesis of the Grothendieck spectral sequence theorem, that $f_*$ sends
injective sheaves to $h_*$-acyclic ones, holds because $f_*$ sends injective
sheaves to injective sheaves by [lem-weil-pbc-direct-image-preserves-injectives].
Therefore the Grothendieck spectral sequence theorem supplies the first-quadrant
spectral sequence $E_2^{p,q}=R^ph_*R^qf_*F\Longrightarrow R^{p+q}(h_*f_*)F$, and
$h_*f_*=(hf)_*$.
