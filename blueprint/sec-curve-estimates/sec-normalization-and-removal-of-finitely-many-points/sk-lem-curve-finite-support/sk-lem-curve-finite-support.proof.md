+++
kind = "proof"
of = "sk-lem-curve-finite-support"
uses = ["sk-prop-sf-comparison", "sk-lem-pbc-finite"]
+++
We first work on the étale sites. By Lemma [sk-lem-pbc-finite], $h_*$
is exact, its stalks are finite products of stalks of $G$, and its
formation commutes with arbitrary base change, because over a strict
localization of $C$ a finite scheme is a finite disjoint union of
strictly henselian local schemes, on which taking global sections is
exact. Since $h_*$ is exact, the Leray spectral
sequence gives $H^q(C,h_*G)=H^q(Y,G)$. A sheaf supported on finitely
many closed points is $h_*$ of a sheaf on a finite disjoint union of
copies of $\operatorname{Spec}k$, where taking sections is exact
because $k$ is algebraically closed, and the sections of such a sheaf
are the product, here a finite direct sum, of its stalks, which do not
change under extension of $k$. This proves the first two assertions. Using
the comparison of classical direct images and
Theorem [sk-prop-sf-comparison], we transport these statements to
the pro-étale site. See [Stacks, Tag 03QP](https://stacks.math.columbia.edu/tag/03QP), [Stacks, Tag 0959](https://stacks.math.columbia.edu/tag/0959).
