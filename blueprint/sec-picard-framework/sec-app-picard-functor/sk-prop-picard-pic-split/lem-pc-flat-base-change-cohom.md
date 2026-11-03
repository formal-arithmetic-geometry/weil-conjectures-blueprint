+++
id = "lem-pc-flat-base-change-cohom"
kind = "lemma"
title = "Cohomology and flat base change"
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_derivedGlobalSectionsOver_baseChange_iso", "AlgebraicGeometry.Scheme.Modules.derivedGlobalSectionsOver", "AlgebraicGeometry.Scheme.Modules.homologyDerivedGlobalSectionsOverLinearEquiv", "AlgebraicGeometry.Scheme.Modules.nonempty_H_baseChange_linearEquiv", "AlgebraicGeometry.Scheme.Modules.finrankH_pullback", "AlgebraicGeometry.Scheme.Modules.nonempty_H_pullback_linearEquiv"]
order = 643
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-morphism-conventions", "def-pc-scheme", "lem-pc-affine-morphism-hi", "lem-pc-cech-computes", "lem-sc-cech-spectral"]
+++
Let

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\[-2pt]
\downarrow{\scriptstyle f'} & & \downarrow{\scriptstyle f}\\[-2pt]
S' & \xrightarrow{g} & S
\end{array}
$$

be a cartesian diagram of schemes with $S=\operatorname{Spec}(A)$ and
$S'=\operatorname{Spec}(B)$ affine, let $\mathcal{F}$ be a quasi-coherent
$\mathcal{O}_X$-module with $\mathcal{F}'=(g')^*\mathcal{F}$, and assume $g$ is flat and $f$
is quasi-compact and quasi-separated. Regard $R\Gamma(X,\mathcal F)$ as an
object of $D(A)$ through $f$ and $R\Gamma(X',\mathcal F')$ as an object of
$D(B)$ through $f'$. Then

$$
R\Gamma(X,\mathcal{F})\otimes_AB\;\cong\;R\Gamma(X',\mathcal{F}')\qquad\text{in }D(B),
$$

where, $B$ being flat over $A$, the derived tensor product $-\otimes^{L}_AB$ is
the functor induced by the exact functor $-\otimes_AB$. Taking cohomology,

$$
H^i(X,\mathcal{F})\otimes_AB\;\cong\;H^i(X',\mathcal{F}')\qquad\text{for all }i\ge0
$$

as $B$-modules. In particular, for a quasi-compact quasi-separated scheme $X$
over a field $k$, a field extension $K/k$ and $X_K=X\times_{\operatorname{Spec} k}\operatorname{Spec} K$,

$$
\dim_KH^i(X_K,\mathcal F_K)=\dim_kH^i(X,\mathcal F)\qquad\text{for all }i\ge0 .
$$
