+++
kind  = "proof"
of    = "lem-kun-0f14a"
+++
By [lem-kun-proper-stability] the projection
$\operatorname{pr}_2:X\times_kY\to Y$ is proper (base change of the
proper morphism $X\to\Spec(k)$). The object
$\pr_1^{-1}E$ has torsion cohomology and lies in
$\Dplus((X\times_kY)_{\Et})$, so by [lem-kun-0f0f] the
projection formula gives

$$
R\operatorname{pr}_{2,*}
\bigl(\pr_1^{-1}E\kunotimes{\mathbf Z}\pr_2^{-1}K\bigr)
\cong
R\operatorname{pr}_{2,*}\pr_1^{-1}E\kunotimes{\mathbf Z}K .
$$

By proper base change in the form of
[thm-weil-pbc-bounded-below], applied to the cartesian square of
the statement, we have

$$
R\operatorname{pr}_{2,*}\pr_1^{-1}E\cong
\underline{\RGamma(X_{\Et},E)}
$$

(the pullback of a constant object is constant by
[lem-kun-pullback-constant], and the derived global sections of
[def-kun-rgamma-unbounded] compute the sections of
$Ra_{X,*}E$); here $\RGamma(X_{\Et},E)\in\Dplus(\mathbf Z)$ is
bounded below because $E$ is. By [lem-kun-leray-bdd],

$$
\RGamma\bigl((X\times_kY)_{\Et},
\pr_1^{-1}E\kunotimes{\mathbf Z}\pr_2^{-1}K\bigr)
\cong
\RGamma\bigl(Y_{\Et},
\underline{\RGamma(X_{\Et},E)}\kunotimes{\mathbf Z}K\bigr) .
$$

Applying [lem-kun-0f0e] (with $E:=K$ and the constant complex
$\underline{\RGamma(X_{\Et},E)}\in\Dplus(\mathbf Z)$) and then the
symmetry [lem-kun-tensor-sym] we obtain an isomorphism $\theta$
from
$\RGamma((X\times_kY)_{\Et},\pr_1^{-1}E\kunotimes{\mathbf Z}\pr_2^{-1}K)$
to
$\RGamma(X_{\Et},E)\kunotimes{\mathbf Z}\RGamma(Y_{\Et},K)$. By
[lem-kun-kunneth-map-agrees](a),
$\theta\circ\kappa_{E,K}=\mathrm{id}$ (with $\kappa_{E,K}$ the
Kunneth map of [def-kun-kunneth-map]), so $\kappa_{E,K}$ is an
isomorphism, as desired.
