+++
id = "det-pe-wc-cover-second-stage"
kind = "lemma"
title = "Realizing a Stonean cover of the components"
lean = ["WContractification.PullbackProfinite", "WContractification.Restriction", "LocallyConstant.homeomorphPrimeSpectrum", "WContractification.PullbackProfinite.indZariski", "WContractification.PullbackProfinite.isPullback", "WContractification.PullbackProfinite.faithfullyFlat", "RingHom.IndZariski.bijectiveOnStalks", "ConnectedComponents.wlocalSpace_of_isPullback", "ConnectedComponents.preimage_closedPoints_eq_closedPoints_of_isPullback", "ConnectedComponents.isHomeomorph_lift_of_isPullback", "exists_isWContractibleRing_of_isWStrictlyLocal"]
order = 946
uses = ["det-pe-wlocal-strict-contractible", "det-pe-wlocal-components", "det-pe-stonean-cover", "def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-ind-etale-stability"]
+++
Let $C$ be a w-strictly local ring [det-pe-wlocal-strict-contractible], let
$\pi\colon\operatorname{Spec}C\to P:=\pi_0(\operatorname{Spec}C)$ be the projection to the
profinite space of components, and let $f\colon S\to P$ be a continuous surjection from an
extremally disconnected compact Hausdorff space $S$ (which exists by [det-pe-stonean-cover]).

Let $L$ be the ring of locally constant functions $S\to C$; its spectrum is
$S\times\operatorname{Spec}C$. The graph
$\Gamma=\{(s,x):f(s)=\pi(x)\}\subset S\times\operatorname{Spec}C$ is closed and is a union of
connected components; let $Z\subset\pi_0(\operatorname{Spec}L)$ be the closed set of these
components. Let $D=L_Z=\varinjlim_{U}L_{e_U}$, the colimit over the clopen subsets
$U\supset\Gamma$ of $\operatorname{Spec}L$ (ordered by reverse inclusion) of the
localizations at the idempotents $e_U$ with $\operatorname{Spec}L_{e_U}=U$. Then:

1. $C\to D$ is ind-Zariski and faithfully flat; in particular it is ind-étale and identifies
   local rings.
2. The maps $\operatorname{Spec}D\to\operatorname{Spec}C$ and $\operatorname{Spec}D\to S$
   induce a homeomorphism $\operatorname{Spec}D\cong\operatorname{Spec}C\times_PS$.
3. $\operatorname{Spec}D$ is w-local, its closed points are the points $(s,x)$ with $x$
   closed in $\operatorname{Spec}C$, and the induced map $\pi_0(\operatorname{Spec}D)\to S$ is a
   homeomorphism; hence so is $(\operatorname{Spec}D)^c\to S$.
4. $D$ is w-contractible.
