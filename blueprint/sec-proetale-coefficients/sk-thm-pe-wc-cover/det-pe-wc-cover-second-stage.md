+++
id = "det-pe-wc-cover-second-stage"
kind = "lemma"
title = "Realizing a Stonean cover of the components"
uses = ["det-pe-wlocal-strict-contractible", "det-pe-wlocal-components", "det-pe-stonean-cover", "def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-ind-etale-stability"]
+++
Let $C$ be a w-strictly local ring [det-pe-wlocal-strict-contractible], let
$\pi\colon\operatorname{Spec}C\to P:=\pi_0(\operatorname{Spec}C)$ be the projection to the
profinite space of components, and let $f\colon S\to P$ be a continuous surjection from an
extremally disconnected profinite space $S$ (which exists by [det-pe-stonean-cover]).

For a closed subset $Z\subset P$ let $C_Z=\varinjlim_{U}C_{e_U}$, the colimit over the clopen
neighbourhoods $U\supset Z$ (ordered by reverse inclusion) of the localizations at the
idempotents $e_U$ with $\operatorname{Spec}C_{e_U}=\pi^{-1}(U)$. For a finite partition
$\mathcal Q$ of $S$ into nonempty clopen subsets let
$D_{\mathcal Q}=\prod_{A\in\mathcal Q}C_{f(A)}$, and for a refinement $\mathcal Q'$ of
$\mathcal Q$ let $D_{\mathcal Q}\to D_{\mathcal Q'}$ have components
$C_{f(A)}\to C_{f(A')}$ for $A'\subset A$. Put $D=\varinjlim_{\mathcal Q}D_{\mathcal Q}$. Then:

1. $C\to D$ is ind-Zariski and faithfully flat; in particular it is ind-étale.
2. The maps $\operatorname{Spec}D\to\operatorname{Spec}C$ and
   $\operatorname{Spec}D\to S$ induce a bijection
   $\operatorname{Spec}D\to\operatorname{Spec}C\times_PS$, and the local ring of $D$ at the
   point $(x,s)$ is $C_x$.
3. $\operatorname{Spec}D$ is w-local, its closed points are the points $(x,s)$ with $x$
   closed in $\operatorname{Spec}C$, and $(\operatorname{Spec}D)^c\to S$ is a
   homeomorphism.
4. $D$ is w-contractible.
