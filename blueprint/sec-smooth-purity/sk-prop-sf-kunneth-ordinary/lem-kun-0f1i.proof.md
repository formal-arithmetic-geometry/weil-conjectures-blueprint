+++
kind  = "proof"
of    = "lem-kun-0f1i"
+++
*Reduction to affine $X$.* The question is local on $X$
([lem-kun-stalk-faithful-derived] and
[lem-kun-bc-base-change]), hence we may assume $X$ is affine.

*Reduction to $\kunZn$-coefficients.* Similarly, we may
write $F=\varinjlim_{n\in I_K}F[n]$
([def-kun-torsion-invertible] and
[lem-kun-invertible-orders-colimit]); since both sides of the exchange
morphism commute with filtered colimits in $F$
([lemma-weil-pbc-direct-image-filtered-colimit] for the
quasi-compact quasi-separated $g,h$, and exactness of the
inverse images), the same argument reduces us to the case where
$F$ is a sheaf of $\kunZn$-modules for some $n$ invertible in
$K$, which has orders invertible in $K$ by
[lem-kun-zn-sheaf-invertible-orders].

*Passage to the algebraic closure.* We may replace $K$ by
its algebraic closure $\bar K$: formation of the direct image
commutes with base change to $\bar K$ by [lem-kun-0f1c]
(this works for both $g$ and $h$), the exchange morphism is
compatible with this base change
([lem-kun-bc-base-change]), and it suffices to prove the
agreement after restriction to $X'_{\bar K}$ by
[lem-kun-sep-closure-conservative].

*Reduction of $X$.* Next, we may replace $X$ by its
reduction, because étale cohomology is invariant under universal
homeomorphisms ([thm-weil-pbc-universal-homeomorphism-invariance]).
After this replacement the morphism $X\to\Spec(K)$ is flat, of
finite presentation, with geometrically reduced fibres, and the same
holds for any base change, in particular for $X'\to S'$
([lem-kun-geometric-reduced-perfect], where $K$ is
algebraically closed hence perfect). Hence
$f^{-1}g_*F\to h_*e^{-1}F$ is an isomorphism by
[lem-kun-0eys]; in the notation of
[def-kun-bc-property] this is $BC(f',n,0)$, the identification
of the sheaf-level map with the zeroth cohomology sheaf of the derived
exchange morphism being [lem-kun-unbounded-exchange-agrees].

*Conclusion by contraposition.* Suppose for contradiction
that the derived exchange morphism is not an isomorphism for some
$F$ as above. By the spectral sequences of
[thm-sp-truncation-e2] (and
[lem-kun-bc-base-change] together with
[lem-kun-bc-map-on-cohomology], which identify the induced maps on
$\mathcal H^q$ with the maps of
[def-kun-bc-property]), there is a minimal $q\ge1$ such that
$BC(f',n,q)$ fails while $BC(f',n,q-1)$ holds. At this point we
may apply [lem-kun-0f1d] to see that it suffices to prove:
given a commutative diagram

$$
\begin{array}{ccccc}
X&\longleftarrow&X'&\longleftarrow&Y\\
\Big\downarrow{\scriptstyle f}&&\Big\downarrow{}&&\Big\downarrow{\scriptstyle h}\\
\Spec(K)&\longleftarrow&S'&\longleftarrow&\Spec(L)
\end{array}
$$

with both squares cartesian, where $S'$ is affine, integral, and
normal with algebraically closed function field $L$, then
$R^qh_*\underline{\mathbf Z/d\mathbf Z}=0$ for $q>0$ and
$d\mid n$. (Indeed, if some $BC(f',n,q)$ failed,
[lem-kun-0f1d] would produce such a diagram with
$R^qh_*\underline{\mathbf Z/d\mathbf Z}\ne0$; note that
$X''=X'\times_{S'}S''=X\times_KS''$ since
$X'=X\times_KS'$.) But this vanishing is exactly
[lem-kun-0f1i-normal], which is already proved. This
contradiction shows that the derived exchange morphism is an
isomorphism for every $F$, as desired.
