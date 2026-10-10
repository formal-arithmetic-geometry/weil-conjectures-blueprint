+++
kind  = "proof"
of    = "lem-weil-pbc-grothendieck-spectral-sequence"
+++
The pair $(f_*,h_*)$ is a composable pair of left exact functors, and the
hypothesis of the Grothendieck spectral sequence theorem, that $f_*$ sends
injective sheaves to $h_*$-acyclic ones, holds because $f_*$ sends injective
sheaves to injective sheaves by [lem-weil-pbc-direct-image-preserves-injectives].
Therefore the Grothendieck spectral sequence theorem of the spectral-sequence
chapter supplies the functorial first-quadrant spectral sequence
$E_2^{p,q}=R^ph_*R^qf_*F\Longrightarrow R^{p+q}(hf)_*F$, whose $E_2$-page,
edge maps and convergence are those of the composite of left exact functors;
the compatibility with inverse image in a cartesian base change is the
naturality of its base-change form, in the dictionary of the
spectral-sequence chapter.
