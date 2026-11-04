+++
kind = "proof"
of = "proposition-nearby-cycles-commute-verdier-duality"
order = 1675
uses = ["definition-small-pro-etale-site", "lemma-quasi-finite-coordinates", "lemma-nearby-duality-proper-direct-image"]
+++
We argue by induction on $n=\dim X_{\bar\eta}$, simultaneously for all
traits $S$ as above, and show that the cone of $\delta_{X,M}$ has zero
global sections and finite support.

*Reductions.* We may assume that $X$ is projective, reduced, and flat
over $S$, by reductions none of which increases $n$. The assertion is
local and, by Lemma [lemma-nearby-duality-proper-direct-image],
compatible with restriction to opens. So we may pass to a projective
compactification and extend $M$ by zero on its generic fibre. Next we
use the compatibility with proper direct image
(E.14) for the closure of that
generic fibre, together with invariance under nilpotent thickenings.
This lets us assume that $X$ is reduced and flat over $S$.

Put $Q=\Cone(\delta_{X,M})$. It is bounded and constructible by the
finiteness theorem for nearby cycles and ordinary Verdier duality. By
(E.15), $R\Gamma(X_s,Q)=0$.

*Finite support.* By Lemma [lemma-finite-support-global-sections],
it remains to show that the support of $Q$ is finite. By
Lemma [lemma-quasi-finite-coordinates], $X_s$ is covered by
finitely many opens $V_s$ with quasi-finite coordinate maps
$V\to\mathbf A^q_S$, $q\leq n$, and $\dim V_{\bar\eta}\leq q$. As the
vanishing of $Q$ is local, we may replace each $V$ by finitely many
affine opens covering it, with the restricted coordinate maps. Then for
each coordinate map $V\to\mathbf A^1_S$ there is a closed immersion of
$V$ into some $\mathbf A^r_{\mathbf A^1_S}$ over $\mathbf A^1_S$, as
required in Lemma [lemma-nearby-duality-slice].

We claim that $Q$ vanishes over the generic point of each coordinate line
in the special fibre. The slice $V'$ has generic fibre of dimension at
most $q-1<n$. Hence the claim follows from the induction hypothesis and
Lemma [lemma-nearby-duality-slice]. The support of $Q$ therefore
lies over finitely many closed points of each coordinate line. Since the
coordinate map is quasi-finite, the support is finite. This argument
also covers $n=0$, where $q=0$ and $V_s$ is finite.

*Pro-étale formulation.* The comparison for constructible complexes
with finite coefficients transports both the pairing and this isomorphism
to the small pro-étale site.
