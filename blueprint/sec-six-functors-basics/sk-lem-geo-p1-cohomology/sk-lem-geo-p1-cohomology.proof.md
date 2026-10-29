+++
kind = "proof"
of = "sk-lem-geo-p1-cohomology"
uses = ["sk-lem-geo-cartier", "sk-prop-sf-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-curveestimate"]
+++
By the comparisons for cohomology and proper direct image of
[sk-prop-sf-comparison] and [sk-thm-pe-direct-image-comparison], for bounded
below complexes, it suffices to prove (G2) and (G3) in
$D^+(S_{\mathrm{ét}},\Lambda)$ for Noetherian $S$.

Both components of (G2) are globally defined, the second by
[sk-lem-geo-cartier] applied to the section at infinity. By proper base change
and since geometric stalks detect isomorphisms, it suffices to check (G2) on a
geometric fibre, first for $\Lambda=\mathbf Z/\ell^r\mathbf Z$. By the genus
zero case of [sk-thm-curveestimate], the cohomology lives only in degrees $0$
and $2$, with $H^0=\mathbf Z/\ell^r\mathbf Z$ and
$H^2=(\mathbf Z/\ell^r\mathbf Z)(-1)$, and the Kummer description sends a line
bundle to its degree modulo $\ell^r$. Since $\mathcal O(1)$ has degree one, its
class generates $H^2$, and so (G2) is an isomorphism. The unit and the class of
$\mathcal O(1)$ commute with base change, and hence so do (G2), its inverse,
and (G3). For a finite $\mathbf Z/\ell^r\mathbf Z$-algebra $\Lambda$, the
projection formula
[Stacks, Tag 0GL5](https://stacks.math.columbia.edu/tag/0GL5) gives
$Rp_*\Lambda=Rp_*(\mathbf Z/\ell^r\mathbf Z)\otimes^{\mathbf L}_{\mathbf Z/\ell^r}\Lambda$,
and (G2) for $\Lambda$ is (G2) for $\mathbf Z/\ell^r\mathbf Z$ tensored with
$\Lambda$; hence it is again an isomorphism compatible with base change.
