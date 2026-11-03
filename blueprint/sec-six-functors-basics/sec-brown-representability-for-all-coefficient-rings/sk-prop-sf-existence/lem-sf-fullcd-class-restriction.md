+++
id = "lem-sf-fullcd-class-restriction"
kind = "lemma"
title = "The coefficient class is stable under restriction to a pro-étale base change"
lean = ["AlgebraicGeometry.ProEtale.etaleOrigin_upperStar_obj"]
order = 2578
uses = ["def-sf-fullcd-used-class", "def-weil-pbc-etale-sheaves", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-pullback"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$, $A=A_{E,n}$, $k=\Fbar$, a finite-type $k$-scheme
$\overline X$ and a scheme $Y$. Let $V\to Y$ be a weakly étale
$Y$-scheme, that is, an object of the small pro-étale site $Y_{\Proet}$
of
[def-weil-pbc-proetale-site], and put

$$
W=\overline X\times_YV,\qquad
q:W\longrightarrow\overline X,
$$

so that $W$ is a scheme, $q$ is weakly étale and the square is
cartesian. Let $\mathcal F$ be a coefficient sheaf of the blueprint's
class on $\overline X_{\Proet}$, that is,
$\mathcal F\cong\nu_{\overline X}^*\mathcal G$ for a sheaf $\mathcal G$
of $A$-modules on $\overline X_{\Et}$ in the sense of
[def-weil-pbc-etale-sheaves], the comparison morphism being that of
[def-weil-pbc-site-comparison-morphism]. Then the restriction
$q_{\Proet}^{-1}\mathcal F$ of $\mathcal F$ to $W_{\Proet}$ is again of
étale origin,

$$
q_{\Proet}^{-1}\mathcal F\cong
\nu_W^*\bigl(q_{\Et}^{-1}\mathcal G\bigr),
$$

so it is a coefficient sheaf of the same class on the base-changed source.
