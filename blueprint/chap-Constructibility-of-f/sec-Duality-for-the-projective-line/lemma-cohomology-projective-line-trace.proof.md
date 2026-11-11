+++
kind = "proof"
of = "lemma-cohomology-projective-line-trace"
order = 547
uses = ["proposition-etale-implications", "proposition-pro-etale-affines-form-basis", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "lemma-naturality-pasting-comparison", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek"]
+++
By the comparison theorems for the cohomology and the proper direct image
of bounded below complexes
(Theorems [theorem-bounded-below-cohomology-comparison] and
[theorem-comparison-direct-images]), it suffices to
prove the assertions on $\sigma_S$ and $\operatorname{Tr}_p$ in $D^+(S_{\acute{e}t},\Lambda)$
for Noetherian $S$.

Both components of $\sigma_S$ are globally defined. The second
comes from Lemma [lemma-cycle-class-cartier-divisor] applied to the
section at infinity, whose line bundle is $\mathcal O(1)$. Geometric stalks
detect isomorphisms, and by proper base change the stalk of $Rp_*\Lambda$
at a geometric point $\bar s$ is $R\Gamma(\mathbf P^1_{\bar s},\Lambda)$.
It therefore suffices to check that $\sigma_S$ is an isomorphism on a geometric fibre,
first for $\Lambda=\mathbf Z/\ell^r\mathbf Z$. By the genus zero case of
Proposition [proposition-smooth-proper-curves-torsion-prime], the
cohomology lives only in degrees $0$ and $2$, with
$H^0=\mathbf Z/\ell^r\mathbf Z$ and $H^2=(\mathbf Z/\ell^r\mathbf Z)(-1)$.
The Kummer description sends a line bundle to its degree modulo $\ell^r$.
As $\mathcal O(1)$ has degree one, its class generates $H^2$, and
$\sigma_S$ is an isomorphism. The unit and the class of
$\mathcal O(1)$ commute with base change. Therefore so do
$\sigma_S$, its inverse, and $\operatorname{Tr}_p$.

For a finite $\mathbf Z/\ell^r\mathbf Z$-algebra $\Lambda$, the projection
formula [Stacks, [0GL5](https://stacks.math.columbia.edu/tag/0GL5)] gives $Rp_*\Lambda=Rp_*(\mathbf Z/\ell^r\mathbf Z)
\otimes^{\mathbf L}_{\mathbf Z/\ell^r}\Lambda$. Under this identification,
$\sigma_S$ for $\Lambda$ is $\sigma_S$ for $\mathbf Z/\ell^r\mathbf Z$
tensored with $\Lambda$. It is therefore again
an isomorphism compatible with base change.
