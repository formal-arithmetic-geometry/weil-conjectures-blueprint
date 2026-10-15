+++
kind = "proof"
of = "sk-lem-geo-p1-cohomology"
uses = ["sk-lem-geo-cartier", "sk-prop-sf-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-curveestimate"]
+++
Use the bounded-below cohomology and proper direct-image comparisons of
[sk-prop-sf-comparison] and [sk-thm-pe-direct-image-comparison]. They reduce
(G2) and (G3) to the following calculation in $D^+(S_{\mathrm{ét}},\Lambda)$,
also in the Noetherian generality of the lemma.

Both components of (G2) are globally defined, the second by
[sk-lem-geo-cartier] applied to the section at infinity. By proper base
change and since geometric stalks detect isomorphisms, it suffices to check
(G2) on a geometric fibre, first for $\Lambda=\mathbf Z/\ell^r\mathbf Z$. There
the genus-zero case of [sk-thm-curveestimate] gives cohomology only in
degrees $0$ and $2$, with $H^0=\mathbf Z/\ell^r\mathbf Z$ and
$H^2=(\mathbf Z/\ell^r\mathbf Z)(-1)$, and its Kummer description sends a line
bundle to its degree modulo $\ell^r$. Since $\mathcal O(1)$ has degree one, its
class generates $H^2$, and (G2) is an isomorphism. The unit and the class of
$\mathcal O(1)$ commute with base change, hence so do (G2), its inverse, and
(G3). For a finite $\mathbf Z/\ell^r\mathbf Z$-algebra $\Lambda$, the case
$\mathbf Z/\ell^r\mathbf Z$ and the projection formula (Stacks, Tag
[0GL5](https://stacks.math.columbia.edu/tag/0GL5)) give the assertion.
