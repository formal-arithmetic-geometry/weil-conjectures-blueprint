+++
id = "lem-kun-0F14a"
kind = "lemma"
title = "Kunneth formula, one proper factor, integer coefficients"
order = 6138
lean = ["AlgebraicGeometry.Etale.kunnethMap_isIso_of_properFactor"]
uses = ["def-kun-kunneth-map", "def-kun-separably-closed", "def-kun-torsion-invertible", "def-kun-rgamma-unbounded", "lem-kun-0F0E", "lem-kun-0F0F", "lem-kun-kunneth-map-agrees", "lem-kun-leray-bdd", "lem-kun-proper-stability", "lem-kun-pullback-constant", "lem-kun-tensor-sym"]
+++
Let $k$ be a separably closed field ([def-kun-separably-closed]). Let $X$
be a proper scheme over $k$ and let $Y$ be a quasi-compact and
quasi-separated scheme over $k$. If $E\in\Dplus(X_{\Et})$ has torsion
cohomology ([def-kun-torsion-invertible]) and $K\in\Dplus(Y_{\Et})$, then the
Kunneth map of [def-kun-kunneth-map] for the square
$$
 \begin{array}{ccc}
  X\times_kY&\xrightarrow{\;\operatorname{pr}_2\;}&Y\\
  \Big\downarrow{\scriptstyle \operatorname{pr}_1}&&\Big\downarrow{\scriptstyle a_Y}\\
  X&\xrightarrow{\;a_X\;}&\Spec(k)
 \end{array}
$$
$$
 \kappa_{E,K}:
 \RGamma(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z}\RGamma(Y_{\Et},K)
 \longrightarrow
 \RGamma\bigl((X\times_kY)_{\Et},
 \operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}\operatorname{pr}_2^{-1}K\bigr)
$$
is an isomorphism. (*Source:* Stacks Project, Tag
[0F14](https://stacks.math.columbia.edu/tag/0F14), part (1).)

## Proof

By [lem-kun-proper-stability] the projection
$\operatorname{pr}_2:X\times_kY\to Y$ is proper (base change of the proper
morphism $X\to\Spec(k)$). The object $\operatorname{pr}_1^{-1}E$ has torsion
cohomology and lies in $\Dplus((X\times_kY)_{\Et})$, so by [lem-kun-0F0F] the
projection formula gives
$$
 R\operatorname{pr}_{2,*}
 \bigl(\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}\operatorname{pr}_2^{-1}K\bigr)
 \cong
 R\operatorname{pr}_{2,*}\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}K .
$$
By proper base change in the bounded-below form, applied to the cartesian
square of the statement, we have
$$
 R\operatorname{pr}_{2,*}\operatorname{pr}_1^{-1}E\cong
 \underline{\RGamma(X_{\Et},E)}
$$
(the pullback of a constant object is constant by
[lem-kun-pullback-constant], and the derived global sections of
[def-kun-rgamma-unbounded] compute the sections of $Ra_{X,*}E$); here
$\RGamma(X_{\Et},E)\in\Dplus(\mathbf Z)$ is bounded below because $E$ is. By
[lem-kun-leray-bdd],
$$
 \RGamma\bigl((X\times_kY)_{\Et},
 \operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}\operatorname{pr}_2^{-1}K\bigr)
 \cong
 \RGamma\bigl(Y_{\Et},
 \underline{\RGamma(X_{\Et},E)}\otimes^{\mathbf L}_{\mathbf Z}K\bigr) .
$$
Applying [lem-kun-0F0E] (with $E:=K$ and the constant complex
$\underline{\RGamma(X_{\Et},E)}\in\Dplus(\mathbf Z)$) and then the symmetry
[lem-kun-tensor-sym] we obtain an isomorphism $\theta$ from
$\RGamma((X\times_kY)_{\Et},\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}\operatorname{pr}_2^{-1}K)$
to
$\RGamma(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z}\RGamma(Y_{\Et},K)$. By
[lem-kun-kunneth-map-agrees](a), $\theta\circ\kappa_{E,K}=\mathrm{id}$ (with
$\kappa_{E,K}$ the Kunneth map of [def-kun-kunneth-map]), so $\kappa_{E,K}$ is
an isomorphism, as desired.

Unresolved dependencies: def:weil-pbc-scheme-conventions, thm:weil-pbc-bounded-below
