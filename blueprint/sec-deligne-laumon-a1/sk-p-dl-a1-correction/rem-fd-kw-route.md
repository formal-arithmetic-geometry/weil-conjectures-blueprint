+++
id = "rem-fd-kw-route"
kind = "remark"
title = "The extension-by-zero Fourier route"
order = 3026
uses = ["lem-fd-transform-concentration", "lem-fd-transform-hc0-vanishing", "lem-wf-l2-constructible-rigidity"]
+++
For a geometrically irreducible, nonexceptional pure input,
[lem-fd-transform-concentration] makes its extension-by-zero
Fourier transform a sheaf.
[lem-fd-transform-hc0-vanishing] excludes punctual subsheaves,
and [thm-fd-transform-mixed] gives a finite pure filtration.
The sheaf dictionary [lem-wf-l2-constructible-rigidity] and
the Plancherel bound [prop-fd-l2-upper-weight-shift] therefore
bound every stalk; at the origin this is
[cor-fd-origin-hc1-bound].
This route by itself does not identify the generic parts of the
transforms of $j_!\mathcal M$ and $j_*\mathcal M$.
A boundary skyscraper transforms to a nonzero generic rank-one
sheaf, so such an identification requires a separate argument; it is
the zero-extension comparison [prop-fd-zero-extension-comparison],
where these boundary contributions form the lisse correction.
Through this comparison [thm-fd-generic-fourier-sheaf-pure] passes
from the $\iota$-reality of the zero-extension side to the purity of the
generic part $\mathcal M'$ of the middle-extension transform.
